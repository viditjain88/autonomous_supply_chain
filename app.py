import streamlit as st
import re

# Since we are not using the real agents, we can comment out these imports
# from agents import logistics_agent, demand_agent, inventory_agent
# from tasks import optimize_route_task, forecast_demand_task, manage_inventory_task
# from crew import supply_chain_crew

def generate_dynamic_report(population_data, infection_rates, vaccine_availability, cold_chain_logistics, distribution_partnerships):
    """
    This function generates a dynamic, mocked report based on the user's input
    to simulate the output of the agent crew.
    """

    # --- Demand Forecast Section ---
    demand_forecast_report = "### 💉 Vaccine Demand Forecast\n"
    # Simple keyword analysis on infection rates
    if "increase" in infection_rates.lower() or "surge" in infection_rates.lower() or "high" in infection_rates.lower():
        demand_forecast_report += "- **High Alert:** A significant surge in demand is anticipated based on the rising infection rates.\n"
    else:
        demand_forecast_report += "- **Stable Demand:** Current demand is projected to remain stable, but we must remain vigilant.\n"

    # Try to find numbers in the population data
    population_numbers = re.findall(r'\d[\d,\.]*', population_data)
    if population_numbers:
        total_population = sum([int(n.replace(',', '')) for n in population_numbers])
        projected_doses = int(total_population * 0.8) # Assuming 80% of the population needs to be vaccinated
        demand_forecast_report += f"- **Projected Need:** We project a need for approximately **{projected_doses:,} vaccine doses** for the specified population.\n"
    else:
        demand_forecast_report += "- **Projected Need:** A significant number of vaccine doses will be required.\n"

    demand_forecast_report += "- **Recommendation:** Prioritize distribution to areas with high population density and rising infection rates.\n"


    # --- Inventory Plan Section ---
    inventory_plan_report = "\n### 📦 Vaccine Inventory Plan\n"
    if "pfizer" in vaccine_availability.lower() and "moderna" in vaccine_availability.lower():
        inventory_plan_report += "- **Diverse Stock:** Our inventory includes both Pfizer and Moderna vaccines, allowing for flexible distribution.\n"
    elif "pfizer" in vaccine_availability.lower():
        inventory_plan_report += "- **Inventory Note:** We are currently holding Pfizer vaccines.\n"
    elif "moderna" in vaccine_availability.lower():
        inventory_plan_report += "- **Inventory Note:** We are currently holding Moderna vaccines.\n"
    else:
        inventory_plan_report += "- **Inventory Note:** Vaccine availability needs to be confirmed.\n"

    inventory_plan_report += "- **Recommendation:** Allocate vaccine doses based on the demand forecast and ensure a buffer stock of 15% is maintained.\n"


    # --- Distribution Logistics Section ---
    distribution_logistics_report = "\n### 🚚 Distribution Logistics Report\n"
    if "major hospitals" in distribution_partnerships.lower() and "pharmacies" in distribution_partnerships.lower():
        distribution_logistics_report += "- **Strong Partnerships:** Leveraging our partnerships with major hospitals and pharmacies will be key to successful distribution.\n"
    elif "hospitals" in distribution_partnerships.lower():
        distribution_logistics_report += "- **Hospital Network:** Our primary distribution will be through our network of partner hospitals.\n"
    else:
        distribution_logistics_report += "- **Distribution Network:** Our distribution network needs to be solidified.\n"

    if "cold chain" in cold_chain_logistics.lower() or "freezers" in cold_chain_logistics.lower():
        distribution_logistics_report += "- **Cold Chain Ready:** Our cold chain logistics are fully equipped and ready for vaccine transport.\n"
    else:
        distribution_logistics_report += "- **Cold Chain Warning:** Immediate attention is needed to ensure our cold chain logistics can support the vaccine requirements.\n"

    distribution_logistics_report += "- **Recommendation:** Optimize delivery routes to minimize transit time and ensure vaccine efficacy. Prioritize routes to regions with the highest need.\n"

    return demand_forecast_report + inventory_plan_report + distribution_logistics_report


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
    with st.spinner("The agents are collaborating on a distribution plan..."):
        results = generate_dynamic_report(
            population_data,
            infection_rates,
            vaccine_availability,
            cold_chain_logistics,
            distribution_partnerships
        )
        st.header("Agents' Final Distribution Plan")
        st.markdown(results)
