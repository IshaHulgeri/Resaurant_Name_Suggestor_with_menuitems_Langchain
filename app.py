import streamlit as st
from dotenv import load_dotenv
import os

# Import the helper function from the other file
from langchain_helper import generate_restaurant_name_and_items

# Load the environment variables from the .env file
# This will load HUGGINGFACEHUB_API_TOKEN
load_dotenv()

st.title("🍽️ Restaurant Name & Menu Generator (Hugging Face Model)")
st.markdown("---")

# Use st.sidebar for the input
cuisine = st.sidebar.selectbox(
    "1. Pick a Cuisine:",
    ("Indian", "Italian", "Mexican", "Chinese", "Japanese", "Thai")
)

# Only run the logic if a cuisine is selected
if cuisine:
    # 2. Call the LangChain helper function
    with st.spinner(f"Generating restaurant ideas for **{cuisine}** cuisine using a FREE Hugging Face Model..."):
        response = generate_restaurant_name_and_items(cuisine)

    # 3. Display the Results
    st.header(f"✨ Restaurant Suggestion: **{response['restaurant_name']}**")
    st.subheader(f"Suggested Menu Items for **{response['restaurant_name']}**")

    # Split the comma-separated string of menu items into a list and display them
    menu_items_list = [item.strip() for item in response['menu_items'].split(",")]

    # Display items as a list
    for item in menu_items_list:
        if item: # Ensure empty strings are not displayed
            st.write(f"- {item}")