from crewai import Agent
from src.agentic_trip_adviser.llms.ollama_llms import OllamaLLM
from src.agentic_trip_adviser.tools.travel_tools import get_websearch_tool
from crewai import LLM
from langchain.llms import Ollama
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq


import os
from dotenv import load_dotenv

load_dotenv()

class TravelAgent:
    def __init__(self, api_key):
        # self.llm = OllamaLLM().get_llm_model()
        # self.llm = Ollama(model="ollama/llama3.2:1b")

        self.llm = ChatOpenAI(api_key=api_key, model="o3-mini")

    def get_guide_expert_agent(self):
        try:
            """
            Agent Resercher
            """
            guide_expert_agent = Agent(
                role="City Local Guide Expert",
                goal="Provides information on things to do in the city based on the user's interest.",
                llm=self.llm,
                backstory="""A local expert with a passion for sharing best experiences and hidden gems of their city.""",
                tools=[get_websearch_tool],
                verbose=True,
                max_iter=5,
                allow_delegation=False,
            )
        except Exception as e:
            raise ValueError(f"Error: Error occured with exception: {e}")

        return guide_expert_agent
    
    def get_location_expert_agent(self):
        try: 
            location_expert_agent = Agent(
                role="Travel Trip Expert",
                goal="Provides travel logistics and essential information.",
                backstory="""A seasonal traveler who has explored various destinations and knows the ins and outs of travel logistics.""",
                llm=self.llm,
                tools=[get_websearch_tool],
                verbose=True,
                max_iter=5,
                allow_delegation=False,
            )
        except Exception as e:
            raise ValueError(f"Error: Error occured with Exception: {e}")

        return location_expert_agent

    def get_trip_planner_expert_agent(self):
        try:
            trip_planner_expert_agent = Agent(
                role="Travel Planning Expert",
                goal="Compiles all gathered information to provide a comprehensive travel plan.",
                backstory="""
                You are a professional guide with a passion for travel.
                An organizational wizard who can turn a list of possibilities into a seamless itenary.
                """,
                tools=[get_websearch_tool],
                llm=self.llm,
                verbose=True,
                max_iter=5,
                allow_delegation=False
            )
        except Exception as e:
            raise ValueError(f"Error: Error occured with Exception: {e}")

        return trip_planner_expert_agent
    
    def get_agents(self):
        try:
            agents = [self.get_guide_expert_agent(), self.get_location_expert_agent(), self.get_trip_planner_expert_agent()]
        except Exception as e:
            raise ValueError(f"Error: Error occured with Exception {e}")
        return agents