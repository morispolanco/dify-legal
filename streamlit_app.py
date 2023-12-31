# Importing necessary libraries
import streamlit as st
import requests
import json

# API configuration, should be secured
API_ENDPOINT = "https://api.dify.ai/v1/chat-messages"
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer app-OZw6qix4wsjQl4MUTmlpEukZ'  # Add Bearer before the key
}

# Function to send a message to the API
def send_message(message):
    data = {"inputs": message}  # replace "message" with "inputs"
    try:
        response = requests.post(API_ENDPOINT, headers=HEADERS, json=data)  # replace data=json.dumps(data) with json=data
        response.raise_for_status()  # raise exception if status is not 200
    except requests.exceptions.HTTPError as errh:
        st.write("HTTP Error:", errh)
        st.write("Response Body:", response.text)
        return False
    except requests.exceptions.ConnectionError as errc:
        st.write("Error Connecting:", errc)
        return False
    except requests.exceptions.Timeout as errt:
        st.write("Timeout Error:", errt)
        return False
    except requests.exceptions.RequestException as err:
        st.write("Something went wrong:", err)
        return False
    else:
        return response.json()

# Title
st.title("Chatbot")

# User input
user_input = st.text_input("Enter a message")

# When the user clicks the 'Send' button,
# the message is sent to the API and the response is displayed.
if st.button('Send'):
    response = send_message(user_input)
    if response:
        st.write('Chatbot response:', response.get('response', 'No response available'))
