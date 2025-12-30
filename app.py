import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Crime Statistics Dashboard", layout="wide")

# --- Page Title ---
st.title("Crime Statistics Analysis Dashboard")

# --- Sidebar Filters (Improved) ---
st.sidebar.markdown("<h2 style='text-align: center; color: white ;'> Filters</h2>", unsafe_allow_html=True)

# Store user selections
location = st.sidebar.selectbox("Select Location", ["All", "Location A", "Location B"])
years = st.sidebar.multiselect(
    "Select Year(s)", 
    [2020, 2021], 
    default=[2020, 2021]  # Both selected by default
)
crime_type = st.sidebar.selectbox("Select Crime Type", ["All", "Theft", "Assault", "Burglary"])

# Display selected filters (optional)
st.sidebar.markdown(f"**Location:** {location}")
st.sidebar.markdown(f"**Year(s):** {', '.join(str(y) for y in years)}")
st.sidebar.markdown(f"**Crime Type:** {crime_type}")

# --- Main Dashboard Sections with Columns ---
st.subheader("Crime Trend & Hotspot Analysis")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Crime Trend Analysis")
    st.info("Crime trend visualization will be displayed here.")

with col2:
    st.markdown("### Crime Hotspot Analysis")
    st.info("Crime hotspot clustering map will be displayed here.")

# --- Crime Type Prediction Section ---
st.subheader("Crime Type Prediction")
if st.button("Predict Crime Type"):
    st.success("Prediction will appear here when the model is integrated.")
