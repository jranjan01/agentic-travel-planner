from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "saved_trips"


def save_travel_plan(city: str, content: str) -> str:
    """
    Saves the final Markdown travel guide to the 'travel_agent/saved_trips' directory.
    Use this tool only after the complete travel guide has been generated.
    The filename is automatically created using the destination city
    (e.g., 'tokyo_travel_plan.md').

    Args:
        city: The primary destination city.
        content: The complete Markdown travel guide to save.

    Returns:
        Confirmation that the file was successfully saved.
    """
    formatted_city = city.strip().lower().replace(" ", "_")

    OUTPUT_DIR.mkdir(exist_ok=True)

    file_path = OUTPUT_DIR / f"{formatted_city}_travel_plan.md"

    file_path.write_text(content, encoding="utf-8")

    return f"Travel plan saved to {file_path.resolve()}"
