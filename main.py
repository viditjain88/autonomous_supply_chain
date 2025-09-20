"""
Main entry point for the Autonomous Supply Chain system.
"""
from agents import logistics_agent, demand_agent, inventory_agent
from tasks import optimize_route_task, forecast_demand_task, manage_inventory_task
from crew import supply_chain_crew

if __name__ == "__main__":
    # Example: Run the crew to optimize supply chain
    results = supply_chain_crew.run()
    print("Supply Chain Optimization Results:", results)
