def calculate_l_bd(diameter_s, f_ck, c_d,k_cp,sigma_sd):
    """
    Calculate the anchorage length.

    Parameters:
    diameter_s (float): The diameter of the reinforcement [mm].
    f_ck (float): The characteristic compressive strength of concrete [MPa].
    c_d (float): The design compressive strength of concrete [mm].
    k_cp (float): A coefficient related to the concrete properties.
    sigma_sd (float, optional): The design tensile stress [MPa]. Defaults to f_sd.

    Returns:
    float: The anchorage length.
    """
    l_bd =max(50 *k_cp * diameter_s * ((sigma_sd/435)**(3/2)) *((25/f_ck)**(1/2)) *((diameter_s/20)**(1/3)) * (((1.5 * diameter_s)/c_d)**(1/2)),10 * diameter_s)
    return l_bd

def calculate_c_d(c_s,c_x,c_y,diameter_s):
    """
    Calculate the design concrete cover.

    Parameters:
    c_s (float): distance between two reinforcement bars [mm].
    c_x (float): The cover in the x-direction [mm].
    c_y (float): The cover in the y-direction [mm].
    diameter_s (float): The diameter of the reinforcement [mm].

    Returns:
    float: The design concrete cover.
    """
    c_d = min(0.5 * c_s, c_x, c_y, 3.75 * diameter_s)
    return c_d

if __name__ == "__main__":
    # Example usage
    diameter = 16  # Example diameter in mm
    f_ck = 30     # Example characteristic compressive strength in MPa
    c_d = calculate_c_d(10,30,30,16)      # Example design compressive strength in mm
    k_cp = 1.4    # Example coefficient
    f_sd = 300    # Example design tensile stress in MPa

    l_bd = calculate_l_bd(diameter, f_ck, c_d, k_cp, f_sd)
    print(f"Calculated design concrete cover (c_d): {c_d} mm")
    print(f"Calculated anchorage length (l_bd): {l_bd} mm")