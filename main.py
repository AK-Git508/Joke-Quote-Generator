# Joke/Quote Generator with Styling

import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Joke/Quote Generator", page_icon="🎉", layout="centered")

st.title("- Joke/Quote Generator -")
st.write("---")  

# Joke button
if st.button("😂 Click for a Joke"):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke_data = response.json()
    st.markdown(f"**{joke_data['setup']}**")  
    st.write(" ")
    st.markdown(f"*{joke_data['punchline']}*")  
    st.write("---")  

# Quote button
if st.button("💡 Click for a Quote"):
    quote_response = requests.get("https://zenquotes.io/api/random")
    quote_data = quote_response.json()[0]
    st.markdown(f"**\"{quote_data['q']}\"**")  
    st.write(" ")
    st.markdown(f"~ *{quote_data['a']}*")  
    st.write("---") 

st.write(" ")
st.write("Made by Aariz Khan on 15/Aug/2025")

