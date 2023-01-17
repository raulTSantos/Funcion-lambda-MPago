import json
import os
import mercadopago

def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    evento = json.loads(event["body"])
    
    payment_data = {
        "transaction_amount": float(evento["transaction_amount"]),
        "token": evento["token"],
        "installments": int(evento["installments"]),
        "payment_method_id": evento["payment_method_id"],
        "issuer_id": evento["issuer_id"],
        "payer": {
            "email": evento["payer"]["email"],
            "identification": {
                "type": evento["payer"]["identification"]["type"],
                "number": evento["payer"]["identification"]["number"]
            }
        }
    }

    payment_response = sdk.payment().create(payment_data)


    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
        },
        "body": json.dumps(
            payment_response["response"]
        ),
        "isBase64Encoded": False,
        
    }