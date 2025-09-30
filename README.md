Restaurant Name Suggestor with Menu Items (LangChain)
A Streamlit application that uses LangChain and a Hugging Face model to generate unique restaurant names and menu items based on selected cuisines.
Table of Contents

Prerequisites
Installation
Running the Application
Usage
Project Structure
Contributing
License

Prerequisites

Python 3.7+
Git (for cloning the repository)
GitHub Account (to access the repository)
Required Python packages:
streamlit
langchain_huggingface
python-dotenv


A Hugging Face API token (for the model inference)

Installation

Clone the Repository
git clone https://github.com/IshaHulgeri/Resaurant_Name_Suggestor_with_menuitems_Langchain.git
cd Resaurant_Name_Suggestor_with_menuitems_Langchain


Set Up a Virtual Environment (recommended)
python -m venv venv
venv\Scripts\activate  # On Windows


Install Dependencies
pip install -r requirements.txt


If requirements.txt doesn’t exist, create it with:pip freeze > requirements.txt


Typical packages to install manually:pip install streamlit langchain_huggingface python-dotenv




Configure Environment Variables

Create a .env file in the project root:HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here


Replace your_huggingface_api_token_here with your actual Hugging Face API token (get it from Hugging Face).



Running the Application

Activate the Virtual Environment (if not already active)
venv\Scripts\activate  # On Windows


Run the Streamlit App
streamlit run app.py


This will start the app, and a browser window should open automatically (e.g., http://localhost:8501).
If it doesn’t open, manually navigate to that URL.



Usage

Select a cuisine from the sidebar dropdown (e.g., Indian, Italian, Mexican, etc.).
The app will generate a unique restaurant name and five diverse menu items using the Hugging Face model.
Refresh or change the cuisine to see new suggestions.

Project Structure
Resaurant_Name_Suggestor_with_menuitems_Langchain/
│
├── app.py              # Main Streamlit application file
├── langchain_helper.py # Helper functions for LangChain integration
├── .env                # Environment variables (e.g., API token)
├── README.md           # This file
├── requirements.txt    # Python dependencies (if created)
└── venv/               # Virtual environment (optional, not tracked)

Contributing

Fork the repository.
Create a new branch: git checkout -b feature-branch.
Make changes and commit: git commit -m "Describe your changes".
Push to the branch: git push origin feature-branch.
Submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details (create a LICENSE file if desired).
