#Datos
def calcular_bonificaciones (salario_base, cargo, desempeño):
    bonificacion = 0

    if cargo.lower() == "directivo":
        if desempeño.lower()=="alto":
            bonificacion = salario_base * 0.20
        elif desempeño.lower() == "medio":
            bonificacion = salario_base * 0.10
        elif cargo.lower() == "operativo":
            if desempeño.lower() == "alto":
               bonificacion = salario_base * 0.15
        elif desempeño.lower() == "medio":
            bonificacion = salario_base * 0.5

    total_a_recibir = salario_base + bonificacion
    return {
        "cargo": cargo,
        "Nivel de desempeño": desempeño,
        "Salario base": salario_base,
        "Bonificacion": bonificacion,
        "Total a recibir": total_a_recibir
    }
#DATOS EMPLEADOS
empleados = [
    (3000000, "directivo", "alto"),
    (2500000, "DIRECTIVO", "medio"),
    (1300000, "Auxiliar", "bajo"),
    (1700000, "Operativo", "MEDIO")
]
#RESULTADOS
for salario , cargo, desempeño in empleados:
    resultado = calcular_bonificaciones(salario, cargo, desempeño)
    print("\n-----Resumen del Pago-----")
    for key, value in resultado.items():
        print(f"{key}: ${value:,.of}")
    print("----------------------------")
    









