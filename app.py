from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        data = request.get_json()

        valor_original = float(data.get("valor_original"))
        dias_em_atraso = int(data.get("dias_em_atraso"))
        tipo_pagamento = data.get("tipo_pagamento")
        quantidade_parcelas = int(data.get("quantidade_parcelas", 0))

        if tipo_pagamento not in ["avista", "parcelado"]:
            return jsonify({"erro": "Tipo de pagamento inválido."}), 400

        if tipo_pagamento == "parcelado" and (quantidade_parcelas < 2 or quantidade_parcelas > 24):
            return jsonify({"erro": "Parcelamento deve ser entre 2x e 24x."}), 400


        juros_diario = 0.005
        juros_total = valor_original * juros_diario * dias_em_atraso
        valor_com_juros = valor_original + juros_total

        desconto = 0
        if 60 <= dias_em_atraso <= 99:
            if tipo_pagamento == "avista":
                desconto = 10
        elif 100 <= dias_em_atraso <= 150:
            if tipo_pagamento == "avista":
                desconto = 15
            elif tipo_pagamento == "parcelado":
                desconto = 5

        valor_desconto = valor_com_juros * (desconto / 100)
        valor_final = valor_com_juros - valor_desconto

        resposta = {
            "valor_original": valor_original,
            "dias_em_atraso": dias_em_atraso,
            "tipo_pagamento": tipo_pagamento,
            "juros_total": round(juros_total, 2),
            "percentual_desconto": desconto,
            "valor_desconto": round(valor_desconto, 2),
            "valor_final": round(valor_final, 2)
        }

        if tipo_pagamento == "parcelado":
            entrada = round(valor_final * 0.10, 2)
            restante = valor_final - entrada
            valor_parcela = round(restante / quantidade_parcelas, 2)

            resposta["parcelamento"] = {
                "entrada": entrada,
                "quantidade_parcelas": quantidade_parcelas,
                "valor_parcela": valor_parcela
            }

        return jsonify(resposta)

    except Exception as e:
        return jsonify({"erro": "Dados inválidos ou incompletos."}), 400

if __name__ == '__main__':
    app.run(port=5001, debug=True)
