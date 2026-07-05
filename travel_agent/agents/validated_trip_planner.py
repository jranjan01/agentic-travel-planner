from google.adk.agents import LoopAgent

from travel_agent.agents.trip_planner import trip_planner
from travel_agent.agents.trip_validator import trip_validator


validated_trip_planner = LoopAgent(
    name="validated_trip_planner",
    description="Generates and validates a travel plan until it meets all validation criteria.",
    sub_agents=[
        trip_planner,
        trip_validator,
    ],
    max_iterations=3,
)
