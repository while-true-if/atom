import re

atom = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", 
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", 
    "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", 
    "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", 
    "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", 
    "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", 
    "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", 
    "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", 
    "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", 
    "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", 
    "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", 
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", 
    "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

amount = [
    1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 14.007, 
    15.999, 18.998, 20.180, 22.990, 24.305, 26.982, 
    28.085, 30.974, 32.06, 35.45, 39.948, 39.098, 40.078, 
    44.956, 47.867, 50.942, 51.996, 54.938, 55.845, 
    58.933, 58.693, 63.546, 65.38, 69.723, 72.630, 
    74.922, 78.971, 79.904, 83.798, 85.468, 87.62, 
    88.906, 91.224, 92.906, 95.95, 98.907, 101.07, 
    102.91, 106.42, 107.87, 112.41, 114.82, 118.71, 
    121.76, 127.60, 126.90, 131.29, 132.91, 137.33, 
    138.91, 140.12, 140.91, 144.24, 145.00, 150.36, 
    151.96, 157.25, 158.93, 162.50, 164.93, 167.26, 
    168.93, 173.04, 174.97, 178.49, 180.95, 183.84, 
    186.21, 190.23, 192.22, 195.08, 196.97, 200.59, 
    204.38, 207.2, 208.98, 209.00, 210.00, 222.00, 
    223.00, 226.00, 227.00, 232.04, 231.04, 238.03, 
    237.05, 244.00, 243.00, 247.00, 247.00, 251.00, 
    252.00, 257.00, 258.00, 259.00, 262.00, 267.00, 
    270.00, 271.00, 270.00, 277.00, 276.00, 281.00, 
    280.00, 285.00, 284.00, 289.00, 288.00, 293.00, 
    294.00, 294.00]

z = []
count = 0
error = 0

a = input("分子を書いてください。(Please input the molecule for which you want to calculate the molecular weight.)\n>>> ")
a_split1 = re.findall('[A-Z][a-z]*\d*', a)

for i in range(len(a_split1)):
    count = 0
    if re.search('\d', a_split1[i]):
        c = []
        match = re.findall('[A-Za-z]+|\d+', a_split1[i])
        c.extend(match)
        d = c[0]
        e = c[1]
        for j in range(118):
            if d == atom[j]:
                f = j
                break
            else:
                count += 1
        if count == 118:
            print("Input Error")
            error = 1
            break
        g = amount[j]
        h = g * float(e)
        z.append(h)
    else:
        for k in range(118):
            if a_split1[i] == atom[k]:
                l = k
                break
            else:
                count += 1
        if count == 118:
            print("Input Error")
            error = 1
            break
        m = amount[l]
        z.append(m)

if error == 0:
    print(f">>> {sum(z)}")
