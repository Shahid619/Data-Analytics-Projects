# utils/scoring.py
def calculate_score(criteria_dict):
    """Calculate total score, missing conditions, and quality label."""
    # Count TRUE values
    score = sum(criteria_dict.values()) * 20
    missing = [key for key, value in criteria_dict.items() if not value]

    # Assign label based on score
    if score == 100:
        quality = "Perfect Trade"
    elif score >= 80:
        quality = "High Quality"
    elif score >= 60:
        quality = "Average Setup"
    else:
        quality = "Weak / Rushed Trade"

    compromised = ", ".join(missing) if missing else "None"
    return score, compromised, quality
