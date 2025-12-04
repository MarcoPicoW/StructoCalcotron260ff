def v_Rd_nosteel(tau_cd,d,d_v,f_sd,f_ck,torque_rate = 1,E_s = 205000,D_max = 32):
    k_g = max(1.2,48/(16+(D_max*min(1,(60/f_ck)**2))))
    varepsilon_v = (f_sd/E_s)*torque_rate
    k_d = 1/(1+(varepsilon_v*d*k_g))
    v_Rd = k_d * tau_cd * d_v
    print("\nEpsilon=",varepsilon_v,"\nk_d =", k_d)
    print(f"v_Rd = {round(v_Rd,2)} kN/m'")
    print(f"V_Rd(2m) = {round(v_Rd,2)*2} kN\n")



v_Rd_nosteel(tau_cd=1.2,d=450,d_v=430,f_sd=300,f_ck=35,torque_rate=0.99)
v_Rd_nosteel(tau_cd=1.2,d=650,d_v=630,f_sd=300,f_ck=35,torque_rate=0.83)
v_Rd_nosteel(tau_cd=1.2,d=850,d_v=820,f_sd=300,f_ck=35,torque_rate=0.63)


#if __name__ == "__main__":
#    v_Rd_nosteel()