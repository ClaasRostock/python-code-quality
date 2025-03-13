def force_required(m: float, a: float) -> float:
    """Calculate required force.

    Calculates the force required to accelerate a mass
    with consideration of friction.

    Parameters
    ----------
    m : float
        the mass in kg
    a : float
        the targeted accelaration in m/s^2

    Returns
    -------
    float
        the required force in N
    """
    g: float = 9.81  # gravity in m/s^2
    mu: float = 0.1  # friction coefficient
    F: float = m * a + m * g * mu
    return F
