# Lista de herramientas con su ranking (por ejemplo, según popularidad o preferencia)
herramientas = [
    {"nombre": "Python", "ranking": 1},
    {"nombre": "JavaScript", "ranking": 2},
    {"nombre": "Java", "ranking": 3},
    {"nombre": "C++", "ranking": 4},
    {"nombre": "SQL", "ranking": 5},
]

# Ordenar por ranking (de menor a mayor)
herramientas_ordenadas = sorted(herramientas, key=lambda h: h["ranking"])

# Imprimir la tabla con formato
print(f"{'Ranking':<10}{'Herramienta':<20}")
print("-" * 30)
for h in herramientas_ordenadas:
    print(f"{h['ranking']:<10}{h['nombre']:<20}")
    
# Lista de empresas con los servicios que ofrecen
empresas = [
    {"nombre": "TechSoft", "servicios": ["Desarrollo web", "Soporte técnico"]},
    {"nombre": "DataCorp", "servicios": ["Análisis de datos", "Consultoría"]},
    {"nombre": "CloudNet", "servicios": ["Hosting", "Almacenamiento en la nube"]},
    {"nombre": "InnovaSys", "servicios": ["Desarrollo de apps", "Diseño UX/UI"]},
]

# Imprimir la tabla con formato
print(f"{'Empresa':<15}{'Servicios':<40}")
print("-" * 55)
for e in empresas:
    servicios_str = ", ".join(e["servicios"])
    print(f"{e['nombre']:<15}{servicios_str:<40}")