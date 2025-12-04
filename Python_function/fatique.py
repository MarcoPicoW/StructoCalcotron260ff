def fatique_steel(sigma_sd_max,sigma_sd_min,durchmesser_s, d_i = 0, delta_sigma_sd_fat = 0, stirrups = False):
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

    print("\n",round(delta_sigma_sd_Qfat, 2), "N/mm²" , "<=", round(delta_sigma_sd_fat * 0.8,2), "N/mm²" )
    print( delta_sigma_sd_Qfat <= delta_sigma_sd_fat* 0.8, f"n = {round((delta_sigma_sd_fat* 0.8)/ delta_sigma_sd_Qfat,2)}" )

def fatique_concrete(sigma_cd_max, sigma_cd_min, f_cd, k_c = 1, ):
    decisive_sigma_cd = 0.5 * k_c * f_cd + 0.45 * sigma_cd_min
    print("\n",f"{sigma_cd_max} N/mm² <= {round(decisive_sigma_cd,2)} N/mm² <= {0.9 * k_c * f_cd} N/mm²")
    print(sigma_cd_max <= decisive_sigma_cd <= 0.9 * k_c * f_cd)




fatique_steel(147.2,109.8,24)
fatique_concrete(8.5, 6.3, 22)
print("\n-------------------")
fatique_steel(208.7,173.3,24)
fatique_steel(244.2,202.8,24)
fatique_concrete(10.2, 8.5, 22)
print("\n-------------------")
fatique_steel(66,43.1,24)
fatique_concrete(6.7, 4.4, 22)
print("\n-------------------")
fatique_steel(167.2,126.1,24)
fatique_steel(207.8,156.7,24)
fatique_concrete(10, 7.5, 22)
print("\n-------------------")
fatique_steel(213.1,167.9,24, d_i=192)
fatique_concrete(12.4, 9.7, 22)
print("\n-------------------")
#if __name__ == "__main__":
#    fatique_steel()