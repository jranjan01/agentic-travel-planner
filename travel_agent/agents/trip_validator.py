from google.adk.agents import LlmAgent

from travel_agent.config import GEMINI_LITE_MODEL


trip_validator = LlmAgent(
    name="trip_validator",
    model=GEMINI_LITE_MODEL,
    description="Validates that the generated travel plan is complete and usable.",
    instruction="""
Review the following travel plan.

{travel_plan}

Your ONLY responsibility is to validate the travel plan.

Do NOT rewrite it.
Do NOT improve it.
Do NOT generate a new travel plan.

The travel plan must include:

- Destination
- Source
- Travel dates or duration
- Budget
- Places to visit
- Activities

If the travel plan satisfies all requirements, respond exactly:

ok

Otherwise respond exactly:

retry

Then briefly list the missing or incorrect items.
""",
    output_key="validation_result",
)
