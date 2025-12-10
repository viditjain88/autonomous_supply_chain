"""
Main entry point for the Autonomous Supply Chain system.
"""

from crew import supply_chain_crew

if __name__ == "__main__":
    # Run the Gemini-based supply chain crew
    results = supply_chain_crew.run()
    print("Supply Chain Optimization Results:")
    for key, value in results.items():
        print(f"\n=== {key.replace('_', ' ').title()} ===\n{value}")
