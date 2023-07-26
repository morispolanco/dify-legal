import streamlit as st
import requests
import json

def send_message(query):
    url = 'https://api.dify.ai/v1/chat-messages'
    headers = {
        'Authorization': 'Bearer app-OZw6qix4wsjQl4MUTmlpEukZ',
        'Content-Type': 'application/json',
    }
    payload = {
        "inputs": {},
        "query": query,
        "response_mode": "streaming",
        "user": "abc-123"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        response_json = json.loads(response.text)
        return response_json
    except requests.exceptions.HTTPError as e:
        return f'Error (Código {e.response.status_code}): {e.response.text}'
    except json.JSONDecodeError as e:
        return f'Error al decodificar la respuesta JSON: {response.text}'

def main():
    st.title("Aplicación de Chat")

    user_input = st.text_input("Ingrese un mensaje:")

    if st.button("Enviar"):
        st.write("Usted:", user_input)
        response = send_message(user_input)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
