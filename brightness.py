def adjust_brightness(color: tuple, brightness_percentage: int) -> tuple:
    return tuple(int(c * brightness_percentage / 100) for c in color)
