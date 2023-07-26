import streamlit as st
import requests

API_KEY = 'app-cGt4ZVQJ94qGNMthIXMPQj1l'


def get_response(query):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'inputs': {},
        'query': query,
        'response_mode': 'streaming',
        'conversation_id': '1c7e55fb-1ba2-4e10-81b5-30addcea2276',
        'user': 'abc-123'
    }

    response = requests.post('https://api.dify.ai/v1/chat-messages', headers=headers, json=data)
    return response.json()


# Rest of Streamlit app code

if user_input:
    output = get_response(user_input)
    bot_response = output['message']

    st.session_state.past.append(user_input)
    st.session_state.generated.append(bot_response)
