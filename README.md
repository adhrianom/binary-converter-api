# Binary Conversor API

API REST para conversão de números decimais em representação binária IEEE 754 (32 bits), utilizando a lógica do repositório [binary_conversor_IEEE](https://github.com/adhrianom/binary_conversor_IEEE).

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

```
binary_conversor_API/
├── backend/         # Todo o código do backend (Django)
│   ├── manage.py
│   ├── binary_conversor/
│   └── core/
├── templates/       # (Opcional) Templates globais do projeto
├── venv/            # Ambiente virtual Python
├── README.md
└── ...
```

- **backend/**: Contém toda a implementação do backend em Django, incluindo o arquivo `manage.py`, as configurações do projeto e os apps (`core`, etc).
- **templates/**: Caso utilize templates compartilhados, mantenha-os aqui.
- **venv/**: Ambiente virtual Python (não versionar no Git).
- **README.md**: Este arquivo de documentação.

## Backend (Django)

O backend é responsável por receber requisições HTTP e realizar a conversão de números decimais para a representação binária IEEE 754.

### Principais pontos da implementação:

- **Framework:** Django
- **Endpoint principal:**  
  `POST /core/converter/`  
  Recebe um JSON com o campo `number` e retorna a representação IEEE 754.

### Exemplo de uso

#### Requisição

```json
{
  "number": 5.75
}
```

#### Resposta

```json
{
  "number_received": 5.75,
  "ieee754": {
    "signal": 0,
    "exponent": "10000001",
    "mantissa": "01110000000000000000000"
  }
}
```

### Como rodar o backend

1. **Clone este repositório:**
   ```bash
   git clone <URL-DESTE-REPOSITORIO>
   cd binary_conversor_API
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Execute as migrações do Django:**
   ```bash
   cd backend
   python manage.py migrate
   ```

5. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

## Frontend

> **Atenção:** O frontend ainda não foi modificado e não faz parte desta documentação.  
> Quando houver alterações ou implementação do frontend, este README será atualizado com as instruções correspondentes.

## Referência

- Lógica de conversão: [binary_conversor_IEEE](https://github.com/adhrianom/binary_conversor_IEEE)

## Licença

Este projeto segue a licença do repositório original.