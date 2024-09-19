import mercadopago
import json

def gerar_link_pagamento(carrinho):
    sdk = mercadopago.SDK("TEST-5681657146715670-081318-eb11f9263016a5b083edfbb85dcaa990-337437991")

    request_options = mercadopago.config.RequestOptions()
    request_options.custom_headers = {
        'x-idempotency-key': 'unique-key'
    }

    items = []
    for pizza_id, item in carrinho.items():
        items.append({
            "id": pizza_id,
            "title": item['title'],
            "description": item.get('description', ''),
            "quantity": item['quantity'],
            "currency_id": "BRL",
            "unit_price": item['price'],
            "picture_url": item.get('picture_url', '')
        })

    pizza_data = {
        "items": items,
        "back_urls": {
            "success": "http://127.0.0.1:5000/sucesso",
            "pending": "http://127.0.0.1:5000/pendente",
            "failure": "http://127.0.0.1:5000/negado"
        },
        "auto_return": "all"
    }

    try:
        result = sdk.preference().create(pizza_data, request_options)
        print("Resposta da API:", json.dumps(result, indent=4))  # Exibe a resposta formatada

        payment = result.get("response", {})
        link_iniciar_pagamento = payment.get("init_point") or payment.get("sandbox_init_point") or payment.get("redirect_url")

        if link_iniciar_pagamento:
            return link_iniciar_pagamento
        else:
            raise KeyError("'init_point', 'sandbox_init_point', ou 'redirect_url' não encontrado na resposta da API")
    except Exception as e:
        print("Erro ao gerar link de pagamento:", str(e))
        raise
