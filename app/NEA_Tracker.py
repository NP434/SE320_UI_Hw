import streamlit as st
from data import get_data
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Near Earth Asteroid Tracker"
)

objects = get_data()
if objects is None:
    st.write("No data available")

st.title("Near earth Objects")
st.write(f"### Total Near earth objects over past 7 days: {st.session_state['total_count']}")

fig, ax = plt.subplots(figsize =(8,8))
earth = plt.Circle((0,0), 1, color='blue', label='Earth')
ax.add_artist(earth)
scale_factor = 1e-7
for neo in objects:
    distance = neo["Miss Distance (km)"] * scale_factor
    angle = np.random.uniform(0,2* np.pi)
    x = distance * np.cos(angle)
    y = distance * np.sin(angle)
    ax.plot(x, y, 'ro')
    ax.text(x, y, f"{neo['Name']}",
             fontsize=4, ha='right')
    
max_distance = max(neo["Miss Distance (km)"] for neo in objects) * scale_factor * 1.1
ax.set_xlim(-max_distance, max_distance)
ax.set_ylim(-max_distance, max_distance)
ax.set_xlabel("Distance (scaled)")
ax.set_ylabel("Distance (scaled)")
ax.set_title("Near-Earth Objects Distance Plot")
ax.grid(True)
ax.set_aspect('equal', adjustable='box')

st.pyplot(fig)