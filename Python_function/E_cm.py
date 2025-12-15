def calculate_E_cm(f_cm, k_E=10000):
    """Calculate the modulus of elasticity of concrete E_cm in MPa.

    Parameters:
    f_cm : float
        Mean compressive strength of concrete in MPa.
    k_E : float, optional
        The coefficient kE is between 10,000 and 12,000 for aggregates made from alluvial gravel, between 8,000 and 10,000 for those made from crushed limestone, and between 6,000 and 8,000 for limestone-containing rock. 
        Depending on the concrete composition, significant deviations from these values may occur (especially for self-compacting concrete); if necessary, cm must be determined by testing. SIA 2030 applies to concrete with recycled aggregates.
        Coefficient for the calculation, default is 10000. 

    Returns:
    float
        Modulus of elasticity of concrete E_cm in MPa.
    """
    E_cm = k_E * (f_cm) ** (1/3)
    print("E_cm =", E_cm, "MPa")
    return E_cm