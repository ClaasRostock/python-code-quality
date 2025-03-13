def force_required(
    m: float,  # mass in kg
    a: float,  # accelaration in m/s^2
) -> float:
    g: float = 9.81  # gravity in m/s^2
    mu: float = 0.1  # friction coefficient
    F: float = m * a + m * g * mu
    return F
