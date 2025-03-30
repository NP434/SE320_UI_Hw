"""
Author: Noah Perea
Date completed: 3/18/2025
Credits: Chatgpt helped to refine the data sorting and improve optimization and synergy with streamlits perfered data structures
"""
from json import dump, load
from datetime import date
from requests import get
import streamlit as st
import os

try:
    API_KEY = os.getenv("API_KEY") #load API key
except KeyError:
    try:
        API_KEY = st.secrets["API_KEY"]
    except Exception as e:
        print(e)


@st.cache_data(ttl = 3600)
def get_data() -> list:
    """This function is responsible for obtaining and formating the NEO data from the Nasa API"""
    current_date = date.today()
    start_date = (current_date.replace(day = current_date.day - 7)) # get range for last seven days
    try:
        response = get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={current_date}&api_key={API_KEY}")
        raw_data = response.json() 
        if raw_data is None: # Case is used if API fetch fails
            neo_list = None
            total_count = 0

        else:
            with open("asteroids.json", "w") as file:
                dump(raw_data, file, indent = 4, sort_keys= True)
            neos_data = raw_data.get('near_earth_objects', {}) 
           
            neo_list = []  # Flat list for display
            total_count = 0  # Track total count

            for date_key, neos_on_date in neos_data.items(): # iterate over the near earth objects by date
                total_count += len(neos_on_date)  # Update total count

            # Process NEO details and append to neo_list
                neo_list.extend([
                {
                    "Date": date_key,
                    "Name": neo['name'],
                    "Diameter (km)": round(neo['estimated_diameter']['kilometers']['estimated_diameter_max'], 2),
                    "Diameter (ft)": round(neo['estimated_diameter']['feet']['estimated_diameter_max'], 2),
                    "Hazardous": neo['is_potentially_hazardous_asteroid'],
                    "Velocity (km/h)": round(float(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']), 2),
                    "Velocity (miles/h)": round(float(neo['close_approach_data'][0]['relative_velocity']['miles_per_hour']), 2),
                    "Miss Distance (Lunar)": round(float(neo['close_approach_data'][0]['miss_distance']['lunar']), 2)
                    #"Miss Distance (km)": round(float(neo['close_approach_data'][0]['miss_distance']['kilometers']), 2),
                    #"Miss Distance (miles)": round(float(neo['close_approach_data'][0]['miss_distance']['miles']), 2)
                } for neo in neos_on_date
            ])

        
        return neo_list,total_count
    except Exception as e:
        print(e)

def reset_cache() -> None:
    """Clears the data cache"""
    get_data.clear()