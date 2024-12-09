# Proyecto: Modelo de Clasificación de Clientes
**Materia:** Laboratorio de Minería de Datos

## Integrantes del Grupo
- **Octavio Moya**
- **Cesar Nieto**
- **Gabriel Gonzalez**
- **Damian Pylinski**

## Video explicaion
https://drive.google.com/file/d/1puW_w_biNk51NcIa0J6Oleu8m5j5yLsZ/view

## API
Accede a la API del proyecto en el siguiente enlace:  
[API de Clasificación de Clientes](https://tf6nqvt3m2.execute-api.us-east-1.amazonaws.com/developer/predic)

## Datos de Prueba
Para realizar las pruebas, se utilizó el siguiente JSON:

```json
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
```
## resultado
```json
{
    "statusCode": 200,
    "body": "{\"input\": [56, 65648, 49624.93, 17, 467.73, 52.53, 0, 235, 61, 2], \"predicted_class\": 1, \"predicted_label\": \"low_value\"}"
}
```
