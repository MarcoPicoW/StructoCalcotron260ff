def I_rectangle(b,h):
    I_y = (b*h**3)/12
    I_z = (h*b**3)/12
    print("I_y =", I_y,"m^4")
    print("I_z =", I_z,"m^4")
    return I_y, I_z
