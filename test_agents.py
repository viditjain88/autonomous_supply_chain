"""
Unit tests for agent creation in agents.py
"""
import pytest
from agents import logistics_agent, demand_agent, inventory_agent

def test_logistics_agent_role():
    assert logistics_agent.role == 'Logistics Optimizer'

def test_demand_agent_role():
    assert demand_agent.role == 'Demand Forecaster'

def test_inventory_agent_role():
    assert inventory_agent.role == 'Inventory Manager'
