from crewai import Crew, Process
from src.agentic_trip_adviser.tasks.travel_planning_tasks import TravelPalanningTasks
from src.agentic_trip_adviser.agents.travel_agents import TravelAgent

class TravelPlanningCrew:
    def __init__(self, from_city, destination_city, date_from, date_to,interests, api_key):
        self.agents = TravelAgent(api_key).get_agents()
        self.tasks = TravelPalanningTasks(from_city, destination_city, date_from, date_to,interests, api_key).get_tasks()
        self.from_city = from_city
        self.destination_city = destination_city
        self.date_from = date_from
        self.date_to = date_to
        self.interests = interests

    def get_travel_planning_crew(self):
        try:
            travel_planning_crew = Crew(
                agents=self.agents,
                tasks=self.tasks,
                process=Process.sequential,
                full_output=True,
                share_crew=False,
                verbose=True
            )
        except Exception as e:
            raise ValueError(f"Error: Error occured with Exception: {e}")

        return travel_planning_crew