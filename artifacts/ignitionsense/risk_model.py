"""Transparent teaching weights, not empirically fitted combustion coefficients."""

GRAVITY_POINTS = {
    "Microgravity 0g": 25,
    "Lunar 0.16g": 14,
    "Martian 0.38g": 5,
}
FUEL_POINTS = {
    "Solid Polymer": 10,
    "Liquid Propellant": 20,
    "Electrical Insulation": 15,
}


def assess(oxygen: int, gravity: str, fuel: str) -> dict:
    if not 15 <= oxygen <= 40:
        raise ValueError("Oxygen must be between 15% and 40%.")
    if gravity not in GRAVITY_POINTS or fuel not in FUEL_POINTS:
        raise ValueError("Select a supported gravity environment and material.")
    oxygen_points = 45 * (oxygen - 15) / 25
    score = round(min(100, max(0, 10 + oxygen_points + GRAVITY_POINTS[gravity] + FUEL_POINTS[fuel])))
    level, color = ("High", "red") if score >= 70 else (("Moderate", "orange") if score >= 40 else ("Low", "green"))
    return {
        "score": score,
        "level": level,
        "color": color,
        "oxygen_points": oxygen_points,
        "gravity_points": GRAVITY_POINTS[gravity],
        "fuel_points": FUEL_POINTS[fuel],
    }
