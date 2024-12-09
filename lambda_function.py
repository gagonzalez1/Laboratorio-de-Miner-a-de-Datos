import json
import boto3
import csv
import io

def lambda_handler(event, context):
    # Configuración
    runtime = boto3.client('sagemaker-runtime')
    endpoint_name = 'linear-learner-2024-12-08-15-44-17-941'
    
    # Usar los valores proporcionados en el evento (prueba de ejemplo)
    test_sample = event.get("data", [30, 50090, 20000, 50, 400, 70, 1, 10, 30, 5])

    # Convertir a CSV
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(test_sample)
    payload = buf.getvalue()
    
    try:
        # Realizar la predicción
        response = runtime.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='text/csv',
            Body=payload
        )
        
        # Leer la respuesta y extraer la predicción
        result = response['Body'].read().decode()
        result_json = json.loads(result)  # Decodificar la respuesta en formato JSON
        
        # Acceder a la predicción y al 'predicted_label'
        predicted_class = result_json['predictions'][0]['predicted_label']  # Asumimos que hay una única predicción
        
        # Usamos condicionales if para asignar las etiquetas correspondientes
        if predicted_class == 0:
            predicted_label = 'high_value'
        elif predicted_class == 1:
            predicted_label = 'low_value'
        elif predicted_class == 2:
            predicted_label = 'medium_value'
        else:
            predicted_label = 'Unknown'

        # Preparar la respuesta final con las etiquetas
        response_body = {
            'input': test_sample,
            'predicted_class': predicted_class,
            'predicted_label': predicted_label
        }
        
        # Retornar la respuesta en formato JSON
        return {
            'statusCode': 200,
            'body': json.dumps(response_body)
        }
    
    except Exception as e:
        # Manejo de errores
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
