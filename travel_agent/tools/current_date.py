from datetime import datetime


def get_current_date() -> str:
    """
    Returns today's date in a human-readable format.
    Use this tool whenever today's date is needed in the travel plan.
    """
    return datetime.now().strftime("%d %B %Y")
