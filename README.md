# Chameleon API 🦎

Uma API em desenveolvimento para conversão de arquivos, desenvolvida com FastAPI. Transforme seus arquivos, mudando de forma como um camaleão!

## Funcionalidades

- **HTML para PDF**: Converta código HTML em documentos PDF de alta qualidade usando WeasyPrint
- **PDF para PNG**: Extraia a primeira página de um PDF como imagem PNG usando PyMuPDF

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/chameleon-api.git
cd chameleon-api
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando

```bash
uvicorn app:app --reload
```

Acesse `http://127.0.0.1:8000` para usar a interface web ou `http://127.0.0.1:8000/docs` para a documentação interativa.

## Uso da API

### HTML para PDF
```bash
curl -X POST "http://127.0.0.1:8000/convert/html-to-pdf" \
     -H "Content-Type: text/plain" \
     -d "<html><body><h1>Olá!</h1></body></html>" \
     --output output.pdf
```

### PDF para PNG
```bash
curl -X POST "http://127.0.0.1:8000/convert/pdf-to-png" \
     -F "file=@arquivo.pdf" \
     --output output.png
```

## Tecnologias

- **FastAPI**: Framework web moderno e rápido
- **WeasyPrint**: Para conversão HTML → PDF
- **PyMuPDF**: Para conversão PDF → PNG
- **Uvicorn**: Servidor ASGI

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.