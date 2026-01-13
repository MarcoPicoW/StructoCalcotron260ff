def estimate_A_s_pure_bending(M_ed,d,f_sd=435,f_cd=22,b=1000):
    """
    Estimate the required area of steel reinforcement (A_s) for a given
    design bending moment (M_ed) and effective height (d) of a reinforced
    concrete section, using the simplified formula.

    Parameters:
    M_ed : float
        Design bending moment in kNm.
    d : float
        Distance between the middle of steel reinforcement and the opposite side of the section in mm.
    f_sd : float, optional
        Design yield strength of the steel in MPa. Default is 450 MPa.
    f_cd : float, optional
        Design compressive strength of concrete in MPa. Default is 22 MPa.
    b : float, optional
        Width of the section in mm. Default is 1000 mm.

    Returns:
    A_s : float
        Required area of steel reinforcement in mm².
    """
    # Convert M_ed from kNm to Nmm
    M_ed_Nmm = M_ed * 1e6  # kNm to Nmm

    # Calculate A_s using the formula A_s = M_ed / (f_sd * d)
    A_s = M_ed_Nmm / (f_sd * 0.9 * d)
    x = A_s * f_sd / (0.85 * f_cd * b)
    M_Rd_Nmm = A_s * f_sd * (d - 0.425 * x)
    M_Rd = M_Rd_Nmm / 1e6  # Nmm to kNm
    if b == 1000:
        print(f"estimated A_s = {round(A_s)} mm²/m'")
        print(f"Neutral axis depth x = {round(x)} mm")
        print(f"m_Rd > m_Ed: {M_Rd>M_ed} (m_Rd = {round(M_Rd,1)} kNm/m'> m_Ed = {round(M_ed,1)} kNm/m')")
    else:
        print(f"estimated A_s = {round(A_s)} mm²")
        print(f"Neutral axis depth x = {round(x)} mm")
        print(f"M_Rd > M_Ed: {M_Rd>M_ed} (M_Rd = {round(M_Rd,1)} kNm > M_Ed = {round(M_ed,1)} kNm)")
    print(f"x/d < 0.5 * f_sd/435 : {(x/d) < (0.5 * f_sd/435)} ({round(x/d,2)} < {round(0.5 * f_sd/435,2)})")
    return A_s

