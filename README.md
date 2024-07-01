# IBM
Work done as part of IBM internship

# Voice-Controlled IoT Automation with Alexa and Raspberry Pi 4

## Project Overview

This project demonstrates how to control LEDs using voice commands with an Alexa device and a Raspberry Pi 4. The setup leverages AWS services, including AWS Lambda and AWS IoT Core, to bridge the communication between the Alexa device and the Raspberry Pi.

## Requirements

- **Alexa Device**: Provides voice control functionality.
- **Alexa Developer Console**: Used to create and manage Alexa skills.
- **AWS Lambda**: Executes backend code in response to events.
- **AWS IoT Core**: Connects and manages IoT devices.
- **Raspberry Pi 4**: Serves as the central processing unit.
- **Breadboard, Wires, LEDs, Resistors**: For building the hardware interface.

## Setup Instructions

For detailed setup instructions, please refer to the comprehensive [article](link-to-article).

### Summary of Key Steps

1. **AWS Lambda Setup**:
   - Create a Lambda function, add the Alexa Skills Kit trigger, and deploy the provided code.

2. **Alexa Skill Configuration**:
   - Create or update an Alexa skill, define intents and utterances, and link it to the Lambda function.

3. **Raspberry Pi Setup**:
   - Install the operating system, connect hardware, and run the provided script on the Raspberry Pi.

4. **Testing**:
   - Ensure all components are updated and synced, enable the skill in the Alexa app, and test with voice commands.

## Repository Contents

- **Lambda_Code**: Directory containing the final Lambda function code.
- **RaspberryPi4_Code.py**: Final code to be run on the Raspberry Pi 4.
- **intent.JSON**: JSON configuration for Alexa skill intents.
- **README.md**: This file.

## Workflow Diagram + Architecture

<img width="1274" alt="Screenshot 2024-07-01 at 12 49 34 PM" src="https://github.com/Ad0420/IBM/assets/132739176/d8d3a927-12ca-47ce-b70e-87eb1b61975a">

This diagram illustrates the interaction between the user, Alexa device, Alexa Developer Console, AWS Lambda, AWS IoT Core, and Raspberry Pi 4 to control LEDs via voice commands.


