import streamlit as st
import requests
from datetime import datetime

secret_key = 'app-OZw6qix4wsjQl4MUTmlpEukZ'  # Reemplace con su clave secreta

def send_data(user, message):
    url = 'https://api.dify.ai/v1/chat-messages'
    headers = {
        'Authorization': f'Bearer {secret_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "inputs": {},
        "query": "eh",
        "response_mode": "streaming",
        "conversation_id": "", 
        "user": "Moris"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['content']
    else:
        return f'Error (Código {response.status_code}): {response.text}'

def run_chat():
    st.title('Aplicación de Chat Streamlit')
    st.subheader('Ingrese su nombre de usuario y mensajes')
    user = st.text_input('Nombre de usuario')
    message = st.text_input('Mensaje')
    if st.button('Enviar'):
        response = send_data(user, message)
        st.write(response)
    st.text('Historial de Chat')

if __name__ == "__main__":
    run_chat()
