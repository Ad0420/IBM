def lambda_handler(event, context):
    # Initialize the IoT client
    client = boto3.client('iot-data', region_name='us-east-1')  # Replace with your actual region

    # Publish a message to the specified MQTT topic
    response = client.publish(
        topic='myHome/light',  # Replace with your actual topic
        qos=1,
        payload=json.dumps({"message": "turn on"})
    )
    
    # Create a response for Alexa
    return {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'Turning on the light.'
            },
            'shouldEndSession': True
        }
    }

