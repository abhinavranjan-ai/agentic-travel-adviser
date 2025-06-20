---
title: AI Travel Planner with Multi-Agent System
emoji: 🐨
colorFrom: blue	
colorTo: red
sdk: streamlit
sdk_version: 1.42.0
app_file: app.py	
pinned: false	
license: apache-2.0
short_description: AI travel planner with multi-agent recommendations.
---

# Agentic Trip Adviser

Agentic Trip Adviser is an AI-powered travel planner built with **Python**, **CrewAI**, **LangChain**, **OpenAI**, and **Streamlit**. It leverages multiple specialized agents to deliver a seamless travel planning experience.

## Features

- **Location Expert Agent**: Provides travel-related information such as accommodations, cost of living, visa requirements, transportation, weather, and local events.
- **Travel Guide Agent**: Recommends attractions, food, and events tailored to user interests.
- **Trip Planner Agent**: Combines all information into a well-structured, personalized itinerary.

## Try It Out

Test the live demo: [Hugging Face Space](https://huggingface.co/spaces/abhinavranjan-ai/agentic-trip-planner)

## Getting Started Locally

1. **Clone the repository:**
    ```bash
    git clone https://github.com/abhinavranjan-ai/agentic-travel-adviser.git
    cd agentic-travel-planner
    ```
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the app:**
    ```bash
    streamlit run app.py
    ```

- `agents/`: Contains agent logic for location, guide, and trip planning.
- `components/`: UI or Streamlit component definitions.
- `utils/`: Utility functions and helpers.
- `assets/`: Static files such as images or icons.
- `app.py`: Main Streamlit application.
- `requirements.txt`: Python dependencies.
- `.env.example`: Example environment variables.

## License

MIT License

---

Made with ❤️ using CrewAI, LangChain, OpenAI, and Streamlit.

---

> **Note:** If you find this project helpful, feel free to [follow me on LinkedIn](https://www.linkedin.com/in/abhinav-ranjan-ai/)!