def fatique_steel(sigma_sd_max,sigma_sd_min,durchmesser_s, d_i = 0, delta_sigma_sd_fat = 0, stirrups = False):
    """calculates the fatigue verification for steel
    Parameters:
    sigma_sd_max : float
        maximum stress in steel in MPa
    sigma_sd_min : float
        minimum stress in steel in MPa
    durchmesser_s : float
        diameter of the reinforcement in mm
    d_i : float, optional
        diameter of steelrounding if the steel is not straight, default is 0
    delta_sigma_sd_fat : float, optional
        fatigue strength of the steel in MPa, default is 0. If 0, the value is calculated based on the stirrups and diameter of the reinforcement
    stirrups : bool, optional
        indicates if the reinforcement is stirrups, default is False"""
    delta_sigma_sd_Qfat =sigma_sd_max - sigma_sd_min
    if d_i == 0:
        k_durchmesser = 1
    else:
        k_durchmesser = 0.35 + (0.026 * (d_i / durchmesser_s))
        print(f"k_durchmesser = {round(k_durchmesser,2)}")
    if delta_sigma_sd_fat == 0:
        if stirrups and durchmesser_s <= 16:
            delta_sigma_sd_fat = 135
        elif durchmesser_s <= 20:
            delta_sigma_sd_fat = 145 * k_durchmesser
        else:
            delta_sigma_sd_fat = 120 * k_durchmesser

    print(round(delta_sigma_sd_Qfat, 2), "N/mm²" , "<=", round(delta_sigma_sd_fat * 0.8,2), "N/mm²" )
    print(delta_sigma_sd_Qfat <= delta_sigma_sd_fat* 0.8, f"n = {round((delta_sigma_sd_fat* 0.8)/ delta_sigma_sd_Qfat,2)}" )
def fatique_concrete(sigma_cd_max, sigma_cd_min, f_cd, k_c = 1, ):
    """calculates the fatigue verification for concrete
    Parameters:
    sigma_cd_max : float
        maximum stress in concrete in MPa
    sigma_cd_min : float
        minimum stress in concrete in MPa
    f_cd : float
        design compressive strength of concrete in MPa
    k_c : float, optional
        coefficient depending on SIA 261 4.2.1.7, default is 1
    """
    decisive_sigma_cd = 0.5 * k_c * f_cd + 0.45 * sigma_cd_min

    print(f"{sigma_cd_max} N/mm² <= {round(decisive_sigma_cd,2)} N/mm² <= {0.9 * k_c * f_cd} N/mm²")
    print(sigma_cd_max <= decisive_sigma_cd <= 0.9 * k_c * f_cd)

if __name__ == "__main__":
    fatique_steel()