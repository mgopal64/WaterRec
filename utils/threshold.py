THRESHOLD = 35

def should_water(ET0):
    """
    Determines whether watering is needed based on the ET0 value and threshold.

    Parameters: 
    ET0 (float): The reference evapotranspiration value.

    Returns:
    bool: True if watering is needed, False otherwise.
    """
    if ET0 >= THRESHOLD:
        return "It's time to water the plants!"
    else:
        return "No need to water the plants yet."
