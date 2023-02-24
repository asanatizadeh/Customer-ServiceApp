
import streamlit as st
import os
import openai
openai.api_key = (st.secrets["OPENAI_API_KEY"])

st.header("Hotel AI-Customer Service")
review = st.text_area("Enter Customer Review")
button = st.button("Generate Reply")

def generate_repy(review):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt= f"write a reply to the give review. If the customer has any concers, address them. \n\nReview: {review}\n\nreply:",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response.choices[0].text

if button and review:
  with st.spinner("Generating Reply..."):
    reply= generate_repy(review)
  st.write(reply)
