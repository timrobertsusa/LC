import os
import streamlit as st
from streamlit_chat import message

import openai
from langchain.chat_models import AzureChatOpenAI

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

openai.api_type = "azure"
openai.api_base = os.environ['OPENAI_API_BASE']
openai.api_key = os.environ['OPENAI_API_KEY']
openai.api_version = os.environ['OPENAI_API_VERSION']


from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

def main():
    st.set_page_config(
        page_title="Bat Chat",
        page_icon=""
    )    


    
    st.title("Welcome to Bat Chat!")
    st.header("Chat with Batman!🦇")

    #batchat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2, max_tokens=1024)
    #deployment_name = "gpt-4"
    deployment_name = "TimTurbo"    

    #batchat = AzureChatOpenAI(deployment_name=deployment_name, model_name="gpt-4", temperature=0)
    batchat = AzureChatOpenAI(deployment_name=deployment_name, model_name="gpt-35-turbo", temperature=0)
    # add messages to session state to keep track of the conversation; do not reinitialize messages
    if "messages" not in st.session_state:
        st.session_state.messages = [
            #instruction for LLM
            SystemMessage(content="You are the superhero Batman.Please limit your responses to 30 words."),
            ]
    
    with st.sidebar:
        user_input = st.text_input("Enter your message or question to Batman here", key="user_input")

    #if there is user input, add it to the messages list, is_user=True means it is a user message
        if user_input:
            #message(user_input, is_user=True)
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("Thinking..."):
                response = batchat(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))
            #message(response.content, is_user=False)

    #grab all messages from session state and set empty default if no messages exist.
    messages = st.session_state.get("messages", [])
    #for loop to display all messages start from index1, index0 is the instruction for LLM
    for position, msg in enumerate(messages[1:]):
        if position % 2 == 0:
            message(msg.content, is_user=True, key=str(position) + '_user' )
        else:
            message(msg.content, is_user=False, key=str(position) + '_bot')
       
if __name__ == "__main__":
    main()