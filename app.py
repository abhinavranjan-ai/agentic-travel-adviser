from src.agentic_trip_adviser.ui.streamlit.load_ui import LoadStreamlitUI

if __name__=="__main__":
    from_city = "India"
    destination_city = "Rome"
    date_from = "1st September 2025"
    date_to = "7th September 2025"
    interests = "sight seeing and good food"
    
    LoadStreamlitUI().load_ui()