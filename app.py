import streamlit as st
import os
from crew import supply_chain_crew

st.title("💉 COVID-19 Vaccine Distribution Agents 💉")
st.markdown("""
Welcome to the interactive demonstration of our autonomous agents for COVID-19 vaccine distribution.
Provide the necessary information below and click "Run Agent Crew" to see the agents collaborate on a distribution plan.
""")

st.header("Provide Context for the Agents")

population_data = st.text_area(
    "Population Data",
    "City A: 2,000,000 people, City B: 800,000 people."
)
infection_rates = st.text_area(
    "Infection Rates",
    "City A has a 5% weekly increase in infection rates, while City B is stable."
)
vaccine_availability = st.text_area(
    "Vaccine Availability",
    "We have 1,000,000 doses of Pfizer and 500,000 doses of Moderna available this week."
)
cold_chain_logistics = st.text_area(
    "Cold Chain Logistics",
    "All our trucks are equipped with the necessary freezers for both Pfizer and Moderna vaccines."
)
distribution_partnerships = st.text_area(
    "Distribution Partnerships",
    "We have partnerships with all major hospitals and 30% of pharmacies in the region."
)

if st.button("Run Agent Crew"):
    # Check for API Key
    if "OPENAI_API_KEY" not in os.environ and "OPENAI_API_KEY" not in st.secrets:
        st.warning("⚠️ OPENAI_API_KEY is missing. The agents might fail if they try to access the LLM.")
        st.info("For this demo to work fully, you need to set the OPENAI_API_KEY environment variable or secret.")

    with st.spinner("The agents are collaborating on a distribution plan..."):
        inputs = {
            'population_data': population_data,
            'infection_rates': infection_rates,
            'vaccine_availability': vaccine_availability,
            'cold_chain_logistics': cold_chain_logistics,
            'distribution_partnerships': distribution_partnerships
        }

        try:
            results = supply_chain_crew.kickoff(inputs=inputs)
            st.header("Agents' Final Distribution Plan")
            st.markdown(results)
        except Exception as e:
            st.error(f"An error occurred while running the crew: {e}")
            st.warning("Please ensure your OPENAI_API_KEY is valid if you are using the default LLM.")
