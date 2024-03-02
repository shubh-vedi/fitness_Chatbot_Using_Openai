import pandas as pd
import streamlit as st
import os
from dotenv import load_dotenv
from streamlit_chat import message
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)

load_dotenv()  
openai_api_key = os.environ["OPENAI_API_KEY"]

# --- Dataset Loading ---
def load_exercise_data(csv_file):
    df = pd.read_csv(csv_file)
    # Data cleaning or preprocessing can be added here if needed
    return df

exercise_data = load_exercise_data('megaGymDataset.csv')  # Replace with your dataset file

# --- User Preferences ---
def gather_user_preferences():
    st.sidebar.title("User Preferences")
    goal = st.sidebar.selectbox("What's your main fitness goal?", ["Weight Loss", "Build Muscle", "Endurance", "General Fitness"])
    experience = st.sidebar.radio("What's your experience level?", ["Beginner", "Intermediate", "Advanced"])
    restrictions = st.sidebar.checkbox("Any injuries or limitations?")
    return {'goal': goal, 'experience': experience, 'restrictions': restrictions}

# --- Conversation Setup ---
def craft_fitness_prompt(query, exercise_data, history, user_preferences):
    history_summary = ""
    if history:
        history_summary = "You previously mentioned the following: "
        for past_query, past_response in history:
            history_summary += f" - You asked: {past_query}. I responded: {past_response}\n"

    preferences_str = f"Your goals are {user_preferences['goal']}, your experience level is {user_preferences['experience']}, and you noted the following restrictions: {user_preferences['restrictions']}. "

    relevant_exercises = []  # Placeholder for now
    if exercise_data is not None:
        # Add your keyword matching or semantic search logic here
        pass

    prompt = f"You are a helpful fitness expert. {history_summary} {preferences_str} Please answer the following question: {query}."

    if relevant_exercises:
        prompt += "\nHere are some potentially relevant exercises from the dataset: {}".format(", ".join(relevant_exercises))

    return prompt

def initialize_chat():
    system_msg_template = SystemMessagePromptTemplate.from_template(template="Answer the question as truthfully as possible, even if you don't have all the information to provide a perfect solution. If the answer is not apparent, provide guidance on how the user might rephrase the question or find more information.")
    human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")
    prompt_template = ChatPromptTemplate.from_messages([system_msg_template, MessagesPlaceholder(variable_name="history"), human_msg_template])

    chat = ConversationChain(
        memory=ConversationBufferWindowMemory(k=3, return_messages=True),
        prompt=prompt_template,
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key) # Insert your OpenAI API key
    )
    return chat

# --- Main Chat Logic ---
def process_query(query, exercise_data, user_preferences, chat, history):
    try:
        prompt = craft_fitness_prompt(query, exercise_data, history, user_preferences)
        response = chat.predict(input=prompt)
        history.append((query, response))
        return response, history
    except Exception as e:
        return f"An error occurred: {e}. Please try rephrasing your question.", history

# --- Streamlit UI ---
st.title("Fitness Knowledge Bot")

# Gather preferences
user_preferences = gather_user_preferences()

# Initialize chat state
if 'chat' not in st.session_state:
    st.session_state.chat = initialize_chat()
    st.session_state.history = []

# Chat Input
user_input = st.text_input("Ask me about workouts or fitness...", key="input")

# Display Chat History
history_container = st.container()

# Chat Interaction
if user_input:
    with st.spinner("Thinking..."):
        response, st.session_state.history = process_query(
            user_input, exercise_data, user_preferences, st.session_state.chat, st.session_state.history
        )

    # Display history with Streamlit Chat
    with history_container:
        for idx, (user_msg, bot_msg) in enumerate(st.session_state.history):
            message(user_msg, is_user=True, key=f"user_msg_{idx}")
            message(bot_msg, key=f"bot_msg_{idx}")
