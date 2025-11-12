# Chameleon API 🦎

Uma API em desenveolvimento para conversão de arquivos, desenvolvida com FastAPI. Transforme seus arquivos, mudando de forma como um camaleão!

## Funcionalidades

- **HTML para PDF**: Converta código HTML em documentos PDF de alta qualidade usando WeasyPrint, com opções de tamanho de página e margens
- **PDF para PNG**: Extraia a primeira página de um PDF como imagem PNG usando PyMuPDF
- **PDF para JPEG**: Extraia a primeira página de um PDF como imagem JPEG usando PyMuPDF
- **PNG para PDF**: Converta imagens PNG em documentos PDF, com opções de bordas
- **PNG para JPEG**: Converta imagens PNG em JPEG
- **JPEG para PDF**: Converta imagens JPEG em documentos PDF, com opções de bordas
- **JPEG para PNG**: Converta imagens JPEG em PNG

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

4. Configure a chave API (opcional):
```bash
# Defina a variável de ambiente
export CHAMELEON_API_KEY="sua_chave_secreta_aqui"
```
Se não definida, a chave padrão é `chameleon_secret_key_2025`.

## Executando

```bash
uvicorn app:app --reload
```

Acesse `http://127.0.0.1:8000` para usar a interface web ou `http://127.0.0.1:8000/docs` para a documentação interativa.

## Segurança

A API utiliza autenticação baseada em chave API para proteger os endpoints de conversão. Todas as requisições devem incluir o header `X-API-Key` com uma chave válida.

- **Chave padrão**: `chameleon_secret_key_2025` (para desenvolvimento)
- **Configuração**: Defina a variável de ambiente `CHAMELEON_API_KEY` para uma chave personalizada
- **Interface web**: A chave API é inserida automaticamente no campo dedicado

## Uso da API

### HTML para PDF
```bash
curl -X POST "http://127.0.0.1:8000/convert/html-to-pdf?page_size=A4&margin_top=10&margin_bottom=10&margin_left=10&margin_right=10" \
     -H "Content-Type: text/plain" \
     -H "X-API-Key: chameleon_secret_key_2025" \
     -d "<html><body><h1>Olá!</h1></body></html>" \
     --output output.pdf
```

**Parâmetros:**
- `page_size` (opcional): Tamanho da página (A4, A3, Letter, Legal). Padrão: A4
- `margin_top`, `margin_bottom`, `margin_left`, `margin_right` (opcional): Margens em mm. Padrão: 10

### PDF para PNG
```bash
curl -X POST "http://127.0.0.1:8000/convert/pdf-to-png" \
     -H "X-API-Key: chameleon_secret_key_2025" \
     -F "file=@arquivo.pdf" \
     --output output.png
```

### PDF para JPEG
```bash
curl -X POST "http://127.0.0.1:8000/convert/pdf-to-jpeg" \
     -H "X-API-Key: chameleon_secret_key_2025" \
     -F "file=@arquivo.pdf" \
     --output output.jpg
```

### PNG para PDF
```bash
curl -X POST "http://127.0.0.1:8000/convert/png-to-pdf?border_width=5&border_color=red" \
     -H "X-API-Key: chameleon_secret_key_2025" \
     -F "file=@imagem.png" \
     --output output.pdf
```

**Parâmetros:**
- `border_width` (opcional): Largura da borda em pixels. Padrão: 0
- `border_color` (opcional): Cor da borda (nome ou hex). Padrão: black

### PNG para JPEG
```bash
curl -X POST "http://127.0.0.1:8000/convert/png-to-jpeg" \
     -H "X-API-Key: chameleon_secret_key_2025" \
     -F "file=@imagem.png" \
     --output output.jpg
```

### JPEG para PDF
```bash
curl -X POST "http://127.0.0.1:8000/convert/jpeg-to-pdf?border_width=5&border_color=blue" \
     -H "X-API-Key: chameleon_secret_key_2025" \
     -F "file=@imagem.jpg" \
     --output output.pdf
```

**Parâmetros:**
- `border_width` (opcional): Largura da borda em pixels. Padrão: 0
- `border_color` (opcional): Cor da borda (nome ou hex). Padrão: black

### JPEG para PNG
```bash
curl -X POST "http://127.0.0.1:8000/convert/jpeg-to-png" \
     -H "X-API-Key: chameleon_secret_key_2025" \
     -F "file=@imagem.jpg" \
     --output output.png
```

## Tecnologias

- **FastAPI**: Framework web moderno e rápido
- **WeasyPrint**: Para conversão HTML → PDF
- **PyMuPDF**: Para conversão PDF → imagem
- **Pillow (PIL)**: Para manipulação de imagens e conversões
- **Uvicorn**: Servidor ASGI

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.