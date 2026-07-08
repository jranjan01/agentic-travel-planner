from google.adk.agents import LlmAgent

from travel_agent.config import GEMINI_MODEL_1
from travel_agent.tools.save_travel_plan import save_travel_plan
from travel_agent.agents.mcp_client import travel_mcp


travel_plan_generator = LlmAgent(
    name="travel_plan_generator",
    model=GEMINI_MODEL_1,
    description="Generates the final travel plan from the validated travel plan.",
    instruction="""
You are an expert travel advisor.

Use the validated travel plan stored in {travel_plan} to generate a complete travel guide.

Use the available tools whenever appropriate to:
- Include today's date.
- Include the expected weather for the destination.
- Save the final travel plan after it has been generated.

Generate a practical and well-organized travel guide.

The travel guide should include:

- Trip Summary
- Destination Overview
- Current Weather
- Day-by-Day Itinerary
- Estimated Budget
- Packing Checklist
- Travel Tips
- Important Notes

Formatting Requirements:

- Return the response as a professional Markdown document.
- Start with a descriptive title that includes the destination country's flag emoji when available.
  Example:
  # 🇯🇵 Tokyo, Japan - 5-Day Travel Guide
- Display the generated date immediately below the title.
- Use Markdown headings (#, ##, ###) for clear section separation.
- Use tables for:
  - Trip Summary
  - Current Weather
  - Estimated Budget
- Use bullet points for:
  - Daily activities
  - Packing checklist
  - Travel tips
  - Important notes
- Separate major sections using horizontal rules (---).
- Use emojis where appropriate to improve readability.
- Keep the document clean, organized, and easy to read.


Guidelines:

- Use the validated travel plan as the primary source of information.
- Enhance the travel guide using tool outputs when available.
- Do not expose internal reasoning or intermediate planning results.
- Return only the final Markdown travel guide.

""",
    tools=[travel_mcp, save_travel_plan],
    output_key="travel_guide",
)
