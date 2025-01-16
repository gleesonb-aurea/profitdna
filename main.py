"""
Main entry point for the Streamlit application.
"""
from typing import Dict, Any
import streamlit as st
from ai_analyzer import ProfitPathwayAnalyzer

def init_session_state() -> None:
    """Initialize session state variables."""
    defaults: Dict[str, Any] = {
        "api_key": None,
        "analyzer": None,
        "results": None
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def main() -> None:
    """Main function to run the Streamlit application."""
    # Set page config
    st.set_page_config(
        page_title="ProfitDNA Analyzer",
        page_icon="💰",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    init_session_state()
    
    # Main app title
    st.title("ProfitDNA Analyzer")
    st.subheader("Strategic Revenue Path Analysis")
    
    # Sidebar for API key
    with st.sidebar:
        st.header("Settings")
        api_key = st.text_input("OpenAI API Key", type="password", key="openai_key")
        if api_key:
            st.session_state.api_key = api_key
            st.session_state.analyzer = ProfitPathwayAnalyzer(api_key)
    
    # Main content area
    if not st.session_state.api_key:
        st.warning("Please enter your OpenAI API key in the sidebar to begin.")
        return
    
    # Product description input
    product_description = st.text_area(
        "Enter your product or product idea",
        height=150,
        placeholder="Example: Developed project management tool for freelancers. Basic MVP ready, 100 waitlist signups. Background in product management. Current focus: Adding features users requested."
    )
    
    # Analysis button
    if st.button("Analyze Product", type="primary"):
        if not product_description:
            st.error("Please enter a product description.")
            return
            
        with st.spinner("Analyzing your product..."):
            try:
                results = st.session_state.analyzer.analyze_product(product_description)
                st.session_state.results = results
            except Exception as e:
                st.error(f"Error during analysis: {str(e)}")
                return
    
    # Display results
    if st.session_state.results:
        results = st.session_state.results
        
        # Revenue Analysis
        st.header("Revenue Strategy Analysis")
        st.markdown(results["revenue_analysis"])
        
        # Implementation Plan
        st.header("Implementation Strategy")
        st.markdown(results["implementation_plan"])
        
        # Profit Summary
        st.header("Financial Summary")
        st.markdown(results["profit_summary"])
        
if __name__ == "__main__":
    main()
