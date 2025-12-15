def calculate_v_Rd_nosteel(tau_cd,d,d_v,f_ck,f_sd = 435,torque_rate = 1,E_s = 205000,D_max = 32, width = 0):
    """Calculate the punching shear resistance v_Rd in kN/m without shear reinforcement.
    Parameters:
    tau_cd : float
        Design shear stress in MPa.
    d : float
        Effective depth of the slab in m.
    d_v : float
        Shear perimeter in m.
    f_ck : float
        Characteristic compressive strength of concrete in MPa.
    f_sd : float, optional
        Design yield strength of reinforcement in MPa, default is 435 MPa.
    torque_rate : float, optional
        Torque rate, default is 1.
    E_s : float, optional
        Modulus of elasticity of steel in MPa, default is 205000 MPa.
    D_max : float, optional
        Maximum aggregate size in mm, default is 32 mm.
    width : float, optional
        Width for which the punching shear resistance is calculated in m, default is 0 (no width).
    """
    k_g = max(1.2,48/(16+(D_max*min(1,(60/f_ck)**2))))
    varepsilon_v = (f_sd/E_s)*torque_rate
    k_d = 1/(1+(varepsilon_v*d*1000*k_g))
    v_Rd = k_d * tau_cd *1000 * d_v
    print("Epsilon=",varepsilon_v,"\nk_d =", k_d)
    print(f"v_Rd = {round(v_Rd,2)} kN/m'")
    if width != 0:
        print(f"V_Rd({width}m) = {round(v_Rd,2)*width} kN")


if __name__ == "__main__":
    calculate_v_Rd_nosteel