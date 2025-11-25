def v_Rd_nosteel(tau_cd,d,d_v,f_sd,f_ck,torque_rate = 1,E_s = 205000,D_max = 32):
    k_g = max(1.2,48/(16+(D_max*min(1,(60/f_ck)**2))))
    varepsilon_v = (f_sd/E_s)*torque_rate
    k_d = 1/(1+(varepsilon_v*d*k_g))
    v_Rd = k_d * tau_cd * d_v
    #print(min(1,(60/f_ck)),k_g, k_d)
    print(f"v_Rd = {round(v_Rd,2)*2} kN/m'")



v_Rd_nosteel(tau_cd=1.2,d=590,d_v=560,f_sd=300,f_ck=35,torque_rate=0.68)
v_Rd_nosteel(tau_cd=1.2,d=590,d_v=560,f_sd=300,f_ck=35,torque_rate=1.5)
v_Rd_nosteel(tau_cd=1.2,d=350,d_v=300,f_sd=300,f_ck=35,torque_rate=1.5)