import streamlit as st
from agents import logistics_agent, demand_agent, inventory_agent
from tasks import optimize_route_task, forecast_demand_task, manage_inventory_task
from crew import supply_chain_crew

def run_crew_and_get_results(historical_data, market_trends, supply_constraints, shipping_manifests, vendor_relationships):
    """
    This function would normally run the crew, but for this UI example,
    we will mock the kickoff() method to return a pre-defined string.
    """
    # Update task descriptions with the user's input
    forecast_demand_task.description = (
        f"Forecast product demand using the following information:\\n"
        f"- Historical Sales: {historical_data}\\n"
        f"- Market Trends: {market_trends}"
    )
    manage_inventory_task.description = (
        f"Adjust inventory levels based on demand forecasts and the following supply constraints:\\n"
        f"- Supply Constraints: {supply_constraints}"
    )
    optimize_route_task.description = (
        f"Analyze current shipping manifests and vendor relationships to propose new, efficient routes.\\n"
        f"- Shipping Manifests: {shipping_manifests}\\n"
        f"- Vendor Relationships: {vendor_relationships}"
    )

    # Mocked results
    mocked_results = """
    ### Demand Forecast Report
    - Based on the provided data, we project a **25% increase in demand** for the next quarter.
    - The new marketing campaign is expected to further boost sales by **10%**.
    - **Recommendation:** Increase production by **35%** to meet the anticipated demand.

    ### Inventory Adjustment Report
    - The supplier delay will impact our production schedule by an estimated **3 weeks**.
    - **Recommendation:** Immediately source **50% of the required materials** from our alternative supplier in North America.
    - **Recommendation:** Increase our safety stock by **15%** for the affected components.

    ### Logistics Optimization Report
    - The current shipping routes are operating at **95% efficiency**.
    - We have identified a new shipping partner that can **reduce transit times by 2 days** for our European shipments.
    - **Recommendation:** Initiate a trial run with the new shipping partner for one month to validate their performance.
    """
    return mocked_results

st.title("🚢 Autonomous Supply Chain Agents 🚢")
st.markdown("""
Welcome to the interactive demonstration of our autonomous supply chain agents.
Provide the necessary information below and click "Run Crew" to see the agents in action.
""")

st.header("Provide Context for the Agents")

historical_data = st.text_area(
    "Historical Sales Data",
    "Sales have been growing steadily at 10% per month for the last year."
)
market_trends = st.text_area(
    "Market Trends",
    "A new marketing campaign is set to launch next month."
)
supply_constraints = st.text_area(
    "Supply Constraints",
    "Our main supplier has a 2-week production delay."
)
shipping_manifests = st.text_area(
    "Current Shipping Manifests",
    "10 cargo containers are currently en route to our warehouses."
)
vendor_relationships = st.text_area(
    "Vendor Relationships",
    "We have a strong, long-term relationship with our primary shipping partner."
)

if st.button("Run Crew"):
    with st.spinner("The agents are collaborating..."):
        results = run_crew_and_get_results(
            historical_data,
            market_trends,
            supply_constraints,
            shipping_manifests,
            vendor_relationships
        )
        st.header("Agents' Final Report")
        st.markdown(results)
