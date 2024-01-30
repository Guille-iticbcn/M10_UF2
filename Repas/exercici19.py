areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print("Segon element: ", areas_pis[1])

print("Últim element: ", areas_pis[-1])

index_terrassa = areas_pis.index("Terrassa")
print("Àrea de la terrassa: ", areas_pis[index_terrassa + 1])

print("Del primer element al tercer element: ", areas_pis[:3])

print("Del tercer element a l'últim: ", areas_pis[2:])

index_hab1 = areas_pis.index("Habitació1")
index_hab2 = areas_pis.index("Habitació2")
total_habitacions = areas_pis[index_hab1 + 1] + areas_pis[index_hab2 + 1]
print("Total àrea de les dues habitacions: ", total_habitacions)

index_lavabo = areas_pis.index("Lavabo")
areas_pis[index_lavabo + 1] = 8.5
print("Nova llista d'àrees (modificada el lavabo): ", areas_pis)

areas_pis.extend(["Pati interior", 2.78])
print("Nova llista d'àrees (amb pati interior): ", areas_pis)

total_pis = sum([area for area in areas_pis[1:] if isinstance(area, (int, float))])
print("Total àrea del pis: ", total_pis)
