import streamlit as st

# Page configuration
st.set_page_config(
    page_title="World Cities",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🌍 World Cities Explorer")
st.markdown("---")

# Hero section
col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.header("Welcome!")
    st.markdown("""
    Explore cities from around the world with our interactive application.
    
    **Features:**
    - 🗺️ Browse cities by country and region
    - 📊 View detailed city statistics
    - 📈 Analyze population and geographic data
    - 🔍 Search and filter cities
    """)

with col2:
    st.info("""
    ### 📋 Quick Stats
    - Total Cities: 43,000+
    - Countries Covered: 250+
    - Data Updated: 2024
    """)

st.markdown("---")

# Features section
st.header("🚀 Getting Started")

tab1, tab2, tab3 = st.tabs(["Browse Cities", "Search", "Analytics"])

with tab1:
    st.subheader("Browse by Location")
    st.markdown("""
    Select countries and regions to explore cities:
    - Filter by continent
    - View city details
    - Compare cities
    """)
    if st.button("📍 Start Browsing"):
        st.write("Navigate to Cities page in the sidebar →")

with tab2:
    st.subheader("Search Cities")
    st.markdown("""
    Find specific cities quickly:
    - Search by name
    - Filter by population
    - Advanced filters
    """)
    if st.button("🔍 Start Searching"):
        st.write("Navigate to Search page in the sidebar →")

with tab3:
    st.subheader("View Analytics")
    st.markdown("""
    Analyze city data:
    - Population distributions
    - Regional statistics
    - Data visualizations
    """)
    if st.button("📈 View Analytics"):
        st.write("Navigate to Analytics page in the sidebar →")

st.markdown("---")

# Footer
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Dataset:** World Cities Database")
with col2:
    st.markdown("**Built with:** Streamlit")
with col3:
    st.markdown("**Version:** 1.0.0")
