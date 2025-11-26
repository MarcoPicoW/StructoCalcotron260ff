def fatique_steel(delta_sigma_sd_Qfat,durchmesser_s, d_i = 0, delta_sigma_sd_fat = 0, stirrups = False):
    if d_i == 0:
        k_durchmesser = 1
    else:
        k_durchmesser = 0.35 + 0.026 * (d_i / durchmesser_s)
        print(f"k_durchmesser = {round(k_durchmesser,2)}")
    if delta_sigma_sd_fat == 0:
        if stirrups and durchmesser_s <= 16:
            delta_sigma_sd_fat = 135
        elif durchmesser_s <= 20:
            delta_sigma_sd_fat = 145 * k_durchmesser
        else:
            delta_sigma_sd_fat = 120 * k_durchmesser

    print(round(delta_sigma_sd_Qfat, 2), "N/mm²" , "<=", round(delta_sigma_sd_fat * 0.8,2), "N/mm²" )
    print(delta_sigma_sd_Qfat <= delta_sigma_sd_fat* 0.8)


fatique_steel(delta_sigma_sd_Qfat=27.2,durchmesser_s=24)
fatique_steel(delta_sigma_sd_Qfat=23.3,durchmesser_s=24)
fatique_steel(delta_sigma_sd_Qfat=35.8,durchmesser_s=24)
fatique_steel(delta_sigma_sd_Qfat=41.9,durchmesser_s=24)
fatique_steel(delta_sigma_sd_Qfat=42.4,durchmesser_s=24)
fatique_steel(delta_sigma_sd_Qfat=52.8,durchmesser_s=24)
fatique_steel(delta_sigma_sd_Qfat=16,durchmesser_s=24, d_i=192)

#if __name__ == "__main__":
#    fatique_steel()