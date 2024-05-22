import streamlit as st
import requests

# Definición de la API Key y la URL del servicio
API_KEY = "r8_c2sKv2h0SdplTsDk47wV2Eom8BFuNAc2TC5hH"
API_URL = "https://api.openai.com/v1/chat/completions"

# Función para obtener respuesta del chatbot
def get_llama2_response(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    data = {
        "model": "llama-2",
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code != 200:
        return {"error": "Request failed"}
    return response.json()

# Interfaz de usuario con Streamlit
st.title("Llama 2 Chatbot")
user_input = st.text_input("Tú: ", "")

if st.button("Enviar"):
    response = get_llama2_response(user_input)
    if "error" in response:
        st.error(response["error"])
    elif "choices" in response:
        bot_reply = response["choices"][0]["message"]["content"]
        st.write(f"Bot: {bot_reply}")
    else:
        st.error("Unexpected response format")
        st.json(response)  # Para mostrar la respuesta completa y ayudar en la depuración
