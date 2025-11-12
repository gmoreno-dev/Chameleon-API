from fastapi import FastAPI, HTTPException, Request, UploadFile, File, Header, Depends
from fastapi.responses import StreamingResponse, FileResponse
import weasyprint
import io
import base64
import fitz
from PIL import Image
import os

app = FastAPI()

API_KEY = os.getenv("CHAMELEON_API_KEY", "chameleonv2Ncod4ulFdSgrbDrYpedbGuHBhnHqAL")

def verify_api_key(x_api_key: str = Header(..., alias="X-API-Key")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

@app.get("/")
async def read_root():
    return FileResponse("index.html")

@app.post("/convert/html-to-pdf")
async def convert_html_to_pdf(request: Request, page_size: str = 'A4', margin_top: float = 10, margin_bottom: float = 10, margin_left: float = 10, margin_right: float = 10, api_key: str = Depends(verify_api_key)):
    try:
        html = (await request.body()).decode('utf-8')
        css = f"""
@page {{
    size: {page_size};
    margin: {margin_top}mm {margin_right}mm {margin_bottom}mm {margin_left}mm;
}}
"""
        pdf_bytes = weasyprint.HTML(string=html).write_pdf(stylesheets=[weasyprint.CSS(string=css)])
        pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
        return {"pdf": pdf_base64}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/convert/pdf-to-png")
async def convert_pdf_to_png(file: UploadFile = File(...), api_key: str = Depends(verify_api_key)):
    try:
        pdf_bytes = await file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        page = doc.load_page(0)
        pix = page.get_pixmap(dpi=150)  # Melhorar a qualidade (DPI alto)
        png_bytes = pix.tobytes("png")
        return StreamingResponse(io.BytesIO(png_bytes), media_type="image/png", headers={"Content-Disposition": "attachment; filename=output.png"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/convert/png-to-pdf")
async def convert_png_to_pdf(file: UploadFile = File(...), border_width: int = 0, border_color: str = 'black', api_key: str = Depends(verify_api_key)):
    try:
        png_bytes = await file.read()
        image = Image.open(io.BytesIO(png_bytes))
        if border_width > 0:
            from PIL import ImageOps
            image = ImageOps.expand(image, border=border_width, fill=border_color)
            output = io.BytesIO()
            image.save(output, format='PNG')
            png_bytes = output.getvalue()
        doc = fitz.open()
        page = doc.new_page(width=image.width, height=image.height)
        pix = fitz.Pixmap(png_bytes)
        page.insert_image(fitz.Rect(0, 0, image.width, image.height), pixmap=pix)
        pdf_bytes = doc.tobytes()
        pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
        return {"pdf": pdf_base64}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/convert/png-to-jpeg")
async def convert_png_to_jpeg(file: UploadFile = File(...), api_key: str = Depends(verify_api_key)):
    try:
        png_bytes = await file.read()
        image = Image.open(io.BytesIO(png_bytes))
        if image.mode != 'RGB':
            image = image.convert('RGB')
        output = io.BytesIO()
        image.save(output, format='JPEG')
        jpeg_bytes = output.getvalue()
        return StreamingResponse(io.BytesIO(jpeg_bytes), media_type="image/jpeg", headers={"Content-Disposition": "attachment; filename=output.jpg"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/convert/jpeg-to-png")
async def convert_jpeg_to_png(file: UploadFile = File(...), api_key: str = Depends(verify_api_key)):
    try:
        jpeg_bytes = await file.read()
        image = Image.open(io.BytesIO(jpeg_bytes))
        output = io.BytesIO()
        image.save(output, format='PNG')
        png_bytes = output.getvalue()
        return StreamingResponse(io.BytesIO(png_bytes), media_type="image/png", headers={"Content-Disposition": "attachment; filename=output.png"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/convert/pdf-to-jpeg")
async def convert_pdf_to_jpeg(file: UploadFile = File(...), api_key: str = Depends(verify_api_key)):
    try:
        pdf_bytes = await file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        page = doc.load_page(0)
        pix = page.get_pixmap(dpi=150)
        jpeg_bytes = pix.tobytes("jpeg")
        return StreamingResponse(io.BytesIO(jpeg_bytes), media_type="image/jpeg", headers={"Content-Disposition": "attachment; filename=output.jpg"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/convert/jpeg-to-pdf")
async def convert_jpeg_to_pdf(file: UploadFile = File(...), border_width: int = 0, border_color: str = 'black', api_key: str = Depends(verify_api_key)):
    try:
        jpeg_bytes = await file.read()
        image = Image.open(io.BytesIO(jpeg_bytes))
        if border_width > 0:
            from PIL import ImageOps
            image = ImageOps.expand(image, border=border_width, fill=border_color)
            output = io.BytesIO()
            image.save(output, format='JPEG')
            jpeg_bytes = output.getvalue()
        doc = fitz.open()
        page = doc.new_page(width=image.width, height=image.height)
        pix = fitz.Pixmap(jpeg_bytes)
        page.insert_image(fitz.Rect(0, 0, image.width, image.height), pixmap=pix)
        pdf_bytes = doc.tobytes()
        pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
        return {"pdf": pdf_base64}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))