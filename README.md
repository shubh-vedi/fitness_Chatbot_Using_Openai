# Fitness Chatbot

A personalized AI fitness companion providing exercise descriptions, tailored workout recommendations, and answers to your fitness-related questions.

## Introduction

The Fitness Chatbot leverages a  comprehensive exercise database and the power of large language models (LLMs) to facilitate your fitness journey. Whether you're a beginner or a seasoned athlete, this chatbot has something for you.

**Key Features**

* **Exercise Descriptions:** Get clear instructions and form tips for a wide range of exercises.
* **Workout Recommendations:** Receive personalized workout plans based on your goals (weight loss, muscle building, endurance), experience level, and equipment availability.
* **Fitness Q&A:**  Ask questions  about training principles, nutrition, or anything fitness-related and get informative responses. 

## Technologies Used

* **Python:** Core programming language.
* **OPENAI:** Large language model for workout generation and understanding fitness queries.
* **Streamlit:**  Web framework for building the user interface.
* **Pandas:** Data manipulation and analysis (for managing the exercise database).
* **Streamlit**:** Deployment platform.




# Streamlit Deployment Link :

Streamlit link : ([http://34.200.246.244:8503](https://fitnesschatbotllm-qzkaqgpjwra5276zqhwa9g.streamlit.app/)/)

# Screenshot of UI

![HomepageUI](Screenshot.JPG)

## How to Run Locally

1. **Clone the Repository:**
   ```bash
   git clone (https://github.com/shubh-vedi/fitness_chatbot_LLM.git)

2.  **cd Fitness-Chatbot
    ```bash
    pip install -r requirements.txt

3. **Set Environment Variables:

*Obtain your Cohere API Key and create a .env file in the project's root directory with the following content:

**OPENAI_API_KEY=YOUR_API_KEY
**Load the environment variables using a library like dotenv.

4. **Run the Streamlit App:
    ```bash
    streamlit run app.py


## License

[State your chosen license - MIT, Apache 2.0, etc.]

## Get Involved!

Contributions, suggestions, and feedback are welcome! Feel free to open issues or submit pull requests.


