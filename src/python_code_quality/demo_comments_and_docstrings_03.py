def f(
    m,  # mass in kg
    a,  # accelaration in m/s^2
):
    g = 9.81  # gravity in m/s^2
    mu = 0.1  # friction coefficient
    F = m * a + m * g * mu
    return F
