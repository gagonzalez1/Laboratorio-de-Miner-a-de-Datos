# Laboratorio-de-Miner-a-de-Datos

Inegrantes del grupo: Octavio Moya, Cesar Nieto, Gabriel Gonzalez, Damian Pylinski.

Proyecto modelo de clasificacion de clientes

API: https://tf6nqvt3m2.execute-api.us-east-1.amazonaws.com/developer/predic

JSON usado para hacer el test: 
{
  "data": [
    56,
    65648,
    49624.93,
    17,
    467.73,
    52.53,
    0,
    235,
    61,
    2
  ]
}

Respuesta:
{
    "statusCode": 200,
    "body": "{\"input\": [56, 65648, 49624.93, 17, 467.73, 52.53, 0, 235, 61, 2], \"predicted_class\": 1, \"predicted_label\": \"low_value\"}"
}
