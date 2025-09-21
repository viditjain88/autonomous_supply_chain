"""
This file contains interactive test cases for the Autonomous Supply Chain system.
A user can input data to see the agents in action.
"""
from agents import logistics_agent, demand_agent, inventory_agent
from tasks import optimize_route_task, forecast_demand_task, manage_inventory_task
from crew import supply_chain_crew

def run_interactive_session():
    """
    Runs an interactive session to showcase the supply chain agent crew.
    """
    print("Welcome to the Autonomous Supply Chain Interactive Showcase!")
    print("="*60)

    # In a real-world scenario, the agents would use tools to fetch this data.
    # For this interactive showcase, we'll simulate user-provided context.

    print("First, the Demand Forecaster Agent will predict future product demand.")
    historical_data = input("Enter a brief description of historical sales data (e.g., 'steady sales for the last 6 months'): ")
    market_trends = input("Enter any relevant market trends (e.g., 'upcoming holiday season'): ")

    # We will prepend this context to the task description to guide the agent.
    forecast_demand_task.description = (
        f"Forecast product demand using the following information:\n"
        f"- Historical Sales: {historical_data}\n"
        f"- Market Trends: {market_trends}"
    )

    print("\nNext, the Inventory Manager Agent will adjust inventory levels.")
    supply_constraints = input("Enter any supply constraints (e.g., 'supplier shipment delayed by 2 weeks'): ")

    manage_inventory_task.description = (
        f"Adjust inventory levels based on demand forecasts and the following supply constraints:\n"
        f"- Supply Constraints: {supply_constraints}"
    )

    print("\nFinally, the Logistics Optimizer Agent will propose efficient shipping routes.")
    shipping_manifests = input("Enter a brief description of current shipping manifests (e.g., '3 trucks heading to the west coast'): ")
    vendor_relationships = input("Enter any details about vendor relationships (e.g., 'new partnership with a local carrier'): ")

    optimize_route_task.description = (
        f"Analyze current shipping manifests and vendor relationships to propose new, efficient routes.\n"
        f"- Shipping Manifests: {shipping_manifests}\n"
        f"- Vendor Relationships: {vendor_relationships}"
    )

    print("\nRunning the supply chain crew with your inputs...")
    print("="*60)

    # Run the crew with the updated tasks
    results = supply_chain_crew.run()

    print("\nSupply Chain Optimization Results:")
    print("="*60)
    print(results)
    print("="*60)
    print("Thank you for using the Interactive Showcase!")

if __name__ == "__main__":
    run_interactive_session()
