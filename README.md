# Binary Conversor API

API REST para conversão de números decimais em representação binária IEEE 754 (32 bits), utilizando a lógica do repositório [binary_conversor_IEEE](https://github.com/adhrianom/binary_conversor_IEEE).

## Funcionalidade

Recebe um número decimal via requisição POST e retorna sua representação binária IEEE 754 (sinal, expoente e mantissa).

## Instalação

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
   pip install -r requirements.txt
   ```

4. **Execute as migrações do Django:**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

## Uso

### Endpoint

```
POST /core/converter/
```

### Exemplo de requisição

```json
{
  "number": 5.75
}
```

### Exemplo de resposta

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

## Referência

- Lógica de conversão: [binary_conversor_IEEE](https://github.com/adhrianom/binary_conversor_IEEE)

## Licença

Este projeto segue a licença do repositório original.