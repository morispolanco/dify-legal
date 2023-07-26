import streamlit as st
import requests
import time

API_KEY = 'app-cGt4ZVQJ94qGNMthIXMPQj1l'

conversation_id = '1c7e55fb-1ba2-4e10-81b5-30addcea2276' 

def get_response(query):
  
  headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json' 
  }

  data = {
    'inputs': {},
    'query': query,
    'response_mode': 'streaming',
    'conversation_id': conversation_id,  
    'user': 'abc-123'
  }

  try:
    response = requests.post('https://api.dify.ai/v1/chat-messages', headers=headers, json=data)
    response.raise_for_status()
    output = response.json()
  except requests.exceptions.RequestException as e:
    print('API call failed:', e)
    output = {'message': 'Sorry, I am having trouble connecting right now. Please try again later.'}

  time.sleep(1) # add delay between API calls
  
  return output['message']

if 'generated' not in st.session_state:
  st.session_state['generated'] = []

if 'past' not in st.session_state:
  st.session_state['past'] = []
  
def get_text():
  input_text = st.text_input("You: ", "Hello!", key="input")
  return input_text

user_input = get_text()

if user_input:
  output = get_response(user_input)
  
  st.session_state.past.append(user_input)
  st.session_state.generated.append(output)

if st.session_state['generated']:

  for i in range(len(st.session_state['generated'])-1, -1, -1):
    message = st.session_state['generated'][i]
    st.write(f"Bot: {message}")
    
  for i in range(len(st.session_state['past'])-1, -1, -1):
    message = st.session_state['past'][i]
    st.write(f"You: {message}")
    
st.text("Press Enter to send message")
