def effective_plate_width(l_0,b_1,b_2=0,b_w=0):
    b_eff_1 = min((0.2*b_1) + (0.1*l_0), 0.2*l_0)
    print(f"Effective plate width b_eff,1 = {round(b_eff_1,3)} m")
    if b_2 != 0:
        b_eff_2 = min((0.2*b_2) + (0.1*l_0), 0.2*l_0)
        print(f"Effective plate width b_eff,2 = {round(b_eff_2,3)} m")
        if b_w != 0:
            b_eff = b_eff_1 + b_eff_2 + b_w
            print(f"Total effective plate width b_eff = {round(b_eff,3)} m")
            return b_eff
    if b_w != 0 and b_2 == 0:
        b_eff = b_eff_1 + b_w
        print(f"Total effective plate width b_eff = {round(b_eff,3)} m")
        return b_eff
effective_plate_width(l_0 = 7.7,b_1 = 5.375, b_2 = 0, b_w = 0.3)