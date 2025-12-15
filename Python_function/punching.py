def calculate_u(d_v,type,diameter=0, width=0, height=0, distance=0):
    """Calculate the perimeter 'u' based on the type of punching shear.
     Args:
        d_v in m (float): Effective depth of the slab.
        type (str): which type of verification section will be used after SIA 262 (Figur 22 or 23). Exemple: type = 22a means after figur 22 a)
            diameter in m (float, optional): Diameter of the column or load area.
            width in m (float, optional): Width of the rectangular column or load area.
            height in m (float, optional): Height of the rectangular column or load area.
            distance in m (float, optional): Distance from the column to the end of the plate. 
    Returns:
        float: The calculated perimeter 'u' in m.
         """
    from math import pi
    if type == "22a":
        u = (d_v + diameter) * pi
    elif type == "22b":
        u = 2 * (width + height) + pi * d_v
    elif type == "22d":
        u = (2 * width) + height +( 0.5 * pi * d_v) + (2 * distance)
    elif type == "23b":
        u = 3 * d_v + width + ( 0.5 * pi * d_v)
    elif type == "23c":
        u = 3 * d_v +  ( 0.25 * pi * d_v)
    else:
        raise ValueError("Invalid type. Please choose from '22a', '22b', '22d', '23b', or '23c'.")
    return u


def calculate_psi(r_s,d,m_sd,m_Rd,f_sd = 435 ,E_s = 205000):
    """Calculate the reduction factor 'psi' for steel reinforcement.
     Args:
        r_s (float): [in m] Distance to the torque null point. For a first estimation, use "r_s = 0.22 * l" where l is the span length between the supports.
        d (float): [in m] d.
        m_sd (float): [in kNm/m'] mean moment acting on the section considering torsion and bending.
        m_Rd (float): [in kNm/m'] Design bending moment capacity.
        f_sd (float): [in MPa] Design strength of the steel reinforcement.
        E_s (float): [in MPa] Modulus of elasticity of the steel reinforcement."""
    
    psi = 1.5 * (r_s / d) * (f_sd / E_s) * (m_sd / m_Rd)**(3/2)
    return psi
def calculate_k_g(f_ck,D_max = 32):
    """Calculate the coefficient k_g based on concrete strength and maximum aggregate size.
    
    Args:
        f_ck (float): Characteristic compressive strength of concrete in MPa.
        D_max (float, optional): Maximum aggregate size in mm. Default is 32 mm.
    
    Returns:
        float: The calculated coefficient k_g.
    """
    k_g = max(1.2, 48 / (16 + (D_max * min(1, (60 / f_ck) ** 2))))
    return k_g
def calculate_k_r(d,psi,k_g):
    """Calculate the coefficient k_r based on effective depth.
    Args:
        d (float): Effective depth in meters.
        psi (float): Reduction factor for steel reinforcement.
        k_g (float): Coefficient based on concrete strength and aggregate size.
    Returns:
        float: The calculated coefficient k_r.
    """
    k_r = min(1 /(0.45 + (0.18 * psi * (d*1000) * k_g )), 2)
    return k_r

def calculate_v_Rd_nosteel_punching(tau_cd,d_v,u,k_r):
    """Calculate the punching shear resistance v_Rd without steel reinforcement.
    Args:
        tau_cd (float): Design shear stress in MPa.
        d_v (float): Effective depth in meters.
        u (float): Perimeter in meters.
        k_r (float): Coefficient based on effective depth."""
    v_Rd = k_r * tau_cd * 1000 * d_v * u
    return v_Rd
def calculate_k_e(e_u,b):
    """Calculate the coefficient k_e based on eccentricity and width.
    for apporximation of punching Type 1 use:
    k_e = 0.9 for inner columns
    k_e = 0.75 for walls and walls edge
    k_e = 0.7 for edge columns
    k_e = 0.65 for corner columns
    Args:
        e_u (float): Eccentricity in meters.
        b (float): is the diameter of a circle with the same area as the area inside the verification section.
    Returns:
        float: The calculated coefficient k_e.
    """
    k_e = min(1 + (3 * e_u / b), 2)
    return k_e

def calculate_b_s(r_sx,r_sy,l_x=0,l_y=0):
    """Calculate the side length b_s for punching shear verification.
    Args:
        r_sx (float): Distance to the torque null point in the x-direction in meters.
        r_sy (float): Distance to the torque null point in the y-direction in meters.
        l_x (float, optional): Length of the support in the x-direction in meters. Default is 0.
        l_y (float, optional): Length of the support in the y-direction in meters. Default is 0."""
    from math import sqrt
    b_s = 1.5 * sqrt(r_sx * r_sy)
    if l_x != 0 and l_y != 0:
        b_s = min(b_s,l_x,l_y)
    if l_x != 0 and l_y == 0:
        b_s = min(b_s,l_x)
    if l_x == 0 and l_y != 0:
        b_s = min(b_s,l_y)
    return b_s