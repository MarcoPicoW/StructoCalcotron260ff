def effective_plate_width(l_0,b_1,b_w,b_2=0):
    b_eff_1 = min((0.2*b_1) + (0.1*l_0), 0.2*l_0)
    print("\n-------------------")
    print(f"Effective plate width b_eff,1 = {round(b_eff_1,3)} m")
    if b_2 != 0:
        b_eff_2 = min((0.2*b_2) + (0.1*l_0), 0.2*l_0)
        print(f"Effective plate width b_eff,2 = {round(b_eff_2,3)} m")
        b_eff = b_eff_1 + b_eff_2 + b_w
        print(f"Total effective plate width b_eff = {round(b_eff,3)} m")
        return b_eff
    else:
        b_eff = b_eff_1 + b_w
        print(f"Total effective plate width b_eff = {round(b_eff,3)} m")
        return b_eff
        

if __name__ == "__main__":
    effective_plate_width()