import streamlit as st

st.set_page_config(page_title="Crime Statistics Dashboard", layout="wide")

st.title("Crime Statistics Analysis Dashboard")

st.sidebar.header("Filters")
st.sidebar.selectbox("Location", ["All", "Location A", "Location B"])
st.sidebar.slider("Year Range", 2015, 2025, (2018, 2023))
st.sidebar.selectbox("Crime Type", ["All", "Theft", "Assault", "Burglary"])

st.subheader("Crime Trend Analysis")
st.info("Crime trend visualization will be displayed here.")

st.subheader("Crime Hotspot Analysis")
st.info("Crime hotspot clustering map will be displayed here.")

st.subheader("Crime Type Prediction")
st.button("Predict Crime Type")
