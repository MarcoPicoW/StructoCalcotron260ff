def v_Rd_nosteel(tau_cd,d,d_v,f_sd,plastische_Verformung = False,torque_rate = 1,E_s = 205000,D_max = 32):
    k_g = 48/(16+D_max)
    varepsilon_v = (f_sd/E_s)*torque_rate
    if plastische_Verformung:
        varepsilon_v = (f_sd/E_s)*1.5
    k_d = 1/(1+(varepsilon_v*d*k_g))
    v_Rd = k_d * tau_cd * d_v
    print(f"v_Rd = {round(v_Rd,2)} kN/m'")

v_Rd_nosteel(1.2,590,560,300,True)
v_Rd_nosteel(1.2,350,300,300,True)
v_Rd_nosteel(1.2,590,560,300)
v_Rd_nosteel(1.2,350,300,300)
v_Rd_nosteel(1.2,590,560,300,False,0.5)
v_Rd_nosteel(1.2,350,300,300,False,0.5)
v_Rd_nosteel(1.2,590,560,300,False,0.37)
v_Rd_nosteel(1.2,350,300,300,False,0.37)