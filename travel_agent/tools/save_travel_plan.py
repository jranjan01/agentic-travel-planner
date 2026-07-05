from pathlib import Path


def save_travel_plan(city: str, content: str) -> str:
    formatted_city = city.strip().lower().replace(" ", "_")

    output_dir = Path("saved_trips")
    output_dir.mkdir(exist_ok=True)

    file_path = output_dir / f"{formatted_city}_travel_plan.md"

    file_path.write_text(content, encoding="utf-8")

    return f"Travel plan saved to {file_path.resolve()}"
