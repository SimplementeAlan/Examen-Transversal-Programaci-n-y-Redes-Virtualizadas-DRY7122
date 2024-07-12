vlan_id = int(input("Ingrese el número de VLAN: "))

if 1 <= vlan_id <= 1005:
    print("VLAN en el rango normal.")
elif 1006 <= vlan_id <= 4094:
    print("VLAN en el rango extendido.")
else:
    print("Número de VLAN inválido.")

