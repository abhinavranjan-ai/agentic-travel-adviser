from datetime import datetime
from crewai import Task
from src.agentic_trip_adviser.agents.travel_agents import TravelAgent
# from src.agentic_trip_adviser.agents import get_guide_expert_agent, get_location_expert_agent, get_trip_planner_expert_agent

class TravelPalanningTasks:
    def __init__(self, from_city, destination_city, date_from, date_to,interests, api_key):
        obj_travel_agent = TravelAgent(api_key)
        self.get_guide_expert_agent = obj_travel_agent.get_guide_expert_agent()
        self.get_location_expert_agent = obj_travel_agent.get_location_expert_agent()
        self.get_trip_planner_expert_agent = obj_travel_agent.get_trip_planner_expert_agent()
        self.from_city = from_city
        self.destination_city = destination_city
        self.date_from = date_from
        self.date_to = date_to
        self.interests = interests

    def get_location_task(self):
        try:
            location_task = Task(
                description=f"""
                Provide travel-related information including accommodations, cost of living,
                visa requirements, transportation, weather, and local events.

                Traveling from: {self.from_city}
                Destination: {self.destination_city}
                Arrival Date: {self.date_from}
                Departure Date: {self.date_to} 
                """,
                agent=self.get_location_expert_agent,
                expected_output="""A detailed markdown report with relevant travel data.""",
                output_file="city_report.md",
            )
        except Exception as e:
            raise ValueError(f"Error: Error occured with exception {e}")
        return location_task
    
    def get_guide_task(self):
        try: 
            guide_task = Task(
                description=f"""
                Provide a travel guide with attractions, food recommendations, and events.
                Tailor recommendations based on user interests: {self.interests}.
                
                Destination: {self.destination_city}
                Arrival Date: {self.date_from}
                Departure Date: {self.date_to}
                """,
                agent=self.get_guide_expert_agent,
                expected_output="A markdown itinerary including attractions, food, and activities.",
                output_file="guide_report.md",
            )
        except Exception as e:
            raise ValueError(f"Error: Error occured with exception {e}")

        return guide_task
    
    def get_planner_task(self):
        try: 
            location_task = self.get_location_task()
            guide_task = self.get_guide_task()
            planner_task = Task(
                description=f"""
                Combine information into a well-structured itinerary. Include:
                - City introduction (4 paragraphs)
                - Daily travel plan with time allocations
                - Expenses and tips
    
                Destination: {self.destination_city}
                Interests: {self.interests}
                Arrival: {self.date_from}
                Departure: {self.date_to}
                """,
                agent=self.get_trip_planner_expert_agent,
                expected_output="A structured markdown travel itinerary.",
                output_file="travel_plan.md",
                context=[location_task, guide_task],
            )
        except Exception as e:
            raise ValueError(f"Error: Error occured with exception {e}")
    
        return planner_task
    
    def get_tasks(self):
        try: 
            location_task = self.get_location_task()
            guide_task = self.get_guide_task()
            planner_task = self.get_planner_task()

            tasks = [location_task, guide_task, planner_task]
        except Exception as e:
            raise ValueError(f"Error: Error occured with exception {e}")
        return tasks