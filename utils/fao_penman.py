import numpy as np

def fao_penman_debug(entry, albedo=0.23):
    """
    FAO-56 Penman-Monteith with debug prints of all intermediates.
    """
    # 1. Air temperature (°C)
    T = (entry['tempf'] - 32) * 5/9
    print(f"T (°C): {T:.2f}")

    # 2. Wind speed at 2 m (m/s)
    u2 = entry['windspeedmph'] * 0.44704
    print(f"u2 (m/s): {u2:.2f}")

    # 3. Saturation and actual vapor pressures (kPa)
    Tdew = (entry['dewPoint'] - 32) * 5/9
    es = 0.6108 * np.exp((17.27 * T) / (T + 237.3))
    ea = 0.6108 * np.exp((17.27 * Tdew) / (Tdew + 237.3))
    print(f"es (kPa): {es:.4f}")
    print(f"ea (kPa): {ea:.4f}")
    print(f"es - ea (kPa): {es - ea:.4f}")

    # 4. Slope of vapor pressure curve Δ (kPa/°C)
    Delta = (4098 * es) / ((T + 237.3) ** 2)
    print(f"Delta (kPa/°C): {Delta:.4f}")

    # 5. Psychrometric constant γ (kPa/°C) at near sea level
    P_kPa = entry['baromabsin'] * 3.38639
    gamma = 0.000665 * P_kPa
    print(f"barometric pressure (kPa): {P_kPa:.2f}")
    print(f"gamma (kPa/°C): {gamma:.4f}")

    # 6. Net radiation Rn (MJ/m²/day)
    Rs_MJ = entry['solarradday'] / 1e6
    Rns = (1 - albedo) * Rs_MJ
    Rnl = 1 # simplified assumption
    Rn = Rns - Rnl
    print(f"Rs (MJ/m²/day): {Rs_MJ:.4f}")
    print(f"Rns (MJ/m²/day): {Rns:.4f}")
    print(f"Rnl (MJ/m²/day): {Rnl:.4f}")
    print(f"Rn (MJ/m²/day): {Rn:.4f}")

    # 7. Soil heat flux G
    G = 0
    print(f"G (MJ/m²/day): {G:.4f}")

    # 8. Penman-Monteith numerator & denominator
    num = 0.408 * Delta * (Rn - G) + gamma * (900 / (T + 273)) * u2 * (es - ea)
    den = Delta + gamma * (1 + 0.34 * u2)
    print(f"numerator: {num:.4f}")
    print(f"denominator: {den:.4f}")

    ET0 = num / den
    print(f"ET₀ (mm/day): {ET0:.4f}")
    return ET0