libro = {"titulo": "El Principito", "disponible": True}
usuario = {"nombre": "Agustina", "prestamos": []}

# Prestar libro
if libro["disponible"]:
    libro["disponible"] = False
    usuario["prestamos"].append(libro["titulo"])
    print("Libro prestado.")

# Devolver libro
libro["disponible"] = True
usuario["prestamos"].remove(libro["titulo"])
print("Libro devuelto.")
