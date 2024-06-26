import RPi.GPIO as GPIO
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json

# Set up GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Custom MQTT message callback
def customCallback(client, userdata, message):
    payload = json.loads(message.payload)
    if payload.get("message") == "turn on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED turned on")
    if (payload.get("message") == "turn off"):
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED turned off")

# Configure MQTT Client
myMQTTClient = AWSIoTMQTTClient("MyClientID")
myMQTTClient.configureEndpoint("a1r3wztg7a6ycq-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/ibminterns/Desktop/AWS/newcerts/AmazonRootCA1.pem",
                                  "/home/ibminterns/Desktop/AWS/newcerts/6e9d3d2b0dd3364ccc7ba3e716aca0f183ef0be38aad17b95c1a65f2b21c7288-private.pem.key",
                                  "/home/ibminterns/Desktop/AWS/newcerts/6e9d3d2b0dd3364ccc7ba3e716aca0f183ef0be38aad17b95c1a65f2b21c7288-certificate.pem.crt")

# Configure the MQTT connection
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myMQTTClient.connect()
myMQTTClient.subscribe("myHome/light", 1, customCallback)  # Replace with your actual topic

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
