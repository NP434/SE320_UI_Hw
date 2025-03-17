import streamlit as st
from data import get_data
import altair as alt
st.set_page_config(
    page_title="Near Earth Asteroid Tracker"
)

objects = get_data()

st.title("Near earth Objects over the past week")
st.write(objects)
st.dataframe(objects,column_order=("col2","col1"))

