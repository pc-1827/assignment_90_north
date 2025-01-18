def lambda_handler(event, context):
    try:
        number1 = event.get('number1')
        number2 = event.get('number2')
        if number1 is None or number2 is None:
            return {
                'statusCode': 400,
                'body': 'Both number1 and number2 are required.'
            }
        result = number1 + number2
        return {
            'statusCode': 200,
            'body': {'result': result}
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
