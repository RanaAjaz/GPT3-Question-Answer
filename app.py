
import streamlit as st
import os
import openai
openai.api_key = ""

api_key = st.sidebar.text_input("APIkey", type="password")
os.environ["OPENAI_API_KEY"] = api_key
openai.api_key = api_key

st.header("Ask me anything")
context  = st.text_area("Enter Customer Review")
question = st.text_input("Enter your Question" )

button = st.button("Answer the Question")

def generate_reply(review):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"Read the following text and answer the question given at the end.\n\nTex:\n{context}\n\nQuestion:{question}?\n\nAnswer:",
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    st.write(response)
    return response.choices[0].text

if button and question:
    with st.spinner("Generating Reply..."):
        reply = generate_reply(question)
    st.write(reply)