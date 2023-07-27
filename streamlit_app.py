import streamlit as st
import requests
from datetime import datetime

secret_key = 'app-OZw6qix4wsjQl4MUTmlpEukZ'  # Reemplace con su clave secreta

def send_data(user, message):
    # Existing code...
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        if response.content:  # Check if response contains data
            return response.json()['content']
        else:
            return "Response does not contain data."
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
