from crewai import LLM
from langchain_openai import ChatOpenAI

class OllamaLLM:
    def get_llm_model(self):
        try:
            llm = LLM(
                model="ollama/lamma3.2:1b",
                base_url="http://localhost:11434"
            )
        except Exception as e:
            raise ValueError(f"Error: Error occured with Exception: {e}")
        return llm
    