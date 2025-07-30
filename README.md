# 🧮 Microsserviço - Calculadora de Descontos CobAle

Este microsserviço faz parte do sistema de cobrança **CobAle**. Ele é responsável por calcular o valor final de acordos com base no valor original do débito, dias em atraso, tipo de pagamento e quantidade de parcelas.

---

## 📋 Regras de Negócio

- **Juros diário**: 0,5% ao dia sobre o valor original do débito.
- **Descontos aplicáveis**:
  - **60 a 99 dias de atraso**:
    - **À vista**: 10% de desconto
    - **Parcelado**: sem desconto
  - **100 a 150 dias de atraso**:
    - **À vista**: 15% de desconto
    - **Parcelado**: 5% de desconto
- **Parcelamentos válidos**:
  - Apenas entre **2x** e **24x**
  - Requer uma **entrada de 10%** do valor final (com desconto e juros)

---

## 📦 Estrutura da Requisição

### Endpoint

```
POST /calcular
```

### Corpo (JSON)
```json
{
  "valor_original": 450.75,
  "dias_em_atraso": 75,
  "tipo_pagamento": "parcelado",
  "quantidade_parcelas": 4
}
```

---

## 📤 Estrutura da Resposta

### Pagamento à vista:
```json
{
  "valor_original": 450.75,
  "dias_em_atraso": 75,
  "tipo_pagamento": "avista",
  "juros_total": 169.03,
  "percentual_desconto": 10,
  "valor_desconto": 61.98,
  "valor_final": 557.8
}
```

### Pagamento parcelado:
```json
{
  "valor_original": 450.75,
  "dias_em_atraso": 75,
  "tipo_pagamento": "parcelado",
  "juros_total": 169.03,
  "percentual_desconto": 0,
  "valor_desconto": 0,
  "valor_final": 619.78,
  "parcelamento": {
    "entrada": 61.98,
    "quantidade_parcelas": 4,
    "valor_parcela": 139.45
  }
}
```

---

## ▶️ Como rodar localmente

1. **Acesse a pasta do microsserviço**
   ```bash
   cd microservico
   ```

2. **(Opcional) Crie e ative um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   ```

3. **Instale o Flask**
   ```bash
   pip install flask
   ```

4. **Rode o microsserviço**
   ```bash
   python app.py
   ```

Ele estará disponível em:
```
http://127.0.0.1:5001/calcular
```
**OBS:** Este microsserviço pode ser usado individualmente
Porém foi criado para ser usado junto com a minha API CobAle, disponivel em:
[CobAle](https://github.com/Guilherme-alexandr/Cob_Ale)
---

## 📌 Autor

Desenvolvido por **Guilherme Alexandre**  
💻 [GitHub](https://github.com/Guilherme-alexandr)
