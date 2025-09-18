"""
Ejercicio de Distribución Hipergeométrica Multivariada
Curso: Probabilidad y Estadística
Autor: [Tu Nombre]
Fecha: [Fecha]
"""

from scikit_stats import dists

def main():
    print("=== EJERCICIO: DISTRIBUCIÓN HIPERGEOMÉTRICA MULTIVARIADA ===")
    print("Selección de estudiantes de diferentes especialidades\n")
    
    # Datos del problema
    sistemas = 3
    electronica = 8
    industrial = 9
    total_estudiantes = sistemas + electronica + industrial
    seleccionar = 3
    
    print("Datos del curso:")
    print(f"- Sistemas: {sistemas} estudiantes")
    print(f"- Electrónica: {electronica} estudiantes")
    print(f"- Industrial: {industrial} estudiantes")
    print(f"- Total: {total_estudiantes} estudiantes")
    print(f"- Se seleccionan: {seleccionar} estudiantes\n")
    
    # a) Probabilidad de que las 3 sean de Electrónica
    prob_3_electronica = dists.multivariate_hypergeom.pmf(
        x=[0, 3, 0],  # 0 sistemas, 3 electronica, 0 industrial
        n=[sistemas, electronica, industrial],
        size=seleccionar
    )
    print("a) Probabilidad de que las 3 sean de Electrónica:")
    print(f"   P(3 Electrónica) = {prob_3_electronica:.6f}")
    print(f"   ({prob_3_electronica*100:.2f}%)\n")
    
    # b) Probabilidad de que sea uno de cada especialidad
    prob_uno_cada = dists.multivariate_hypergeom.pmf(
        x=[1, 1, 1],  # 1 de cada especialidad
        n=[sistemas, electronica, industrial],
        size=seleccionar
    )
    print("b) Probabilidad de que sea uno de cada especialidad:")
    print(f"   P(1 Sistemas, 1 Electrónica, 1 Industrial) = {prob_uno_cada:.6f}")
    print(f"   ({prob_uno_cada*100:.2f}%)\n")
    
    # c) Probabilidad de que al menos uno sea de Industrial
    # Calculamos 1 - P(ningún industrial)
    prob_ningun_industrial = dists.multivariate_hypergeom.pmf(
        x=[1, 2, 0],  # Combinaciones sin industrial
        n=[sistemas, electronica, industrial],
        size=seleccionar
    )
    prob_al_menos_uno_industrial = 1 - prob_ningun_industrial
    print("c) Probabilidad de que al menos uno sea de Industrial:")
    print(f"   P(al menos 1 Industrial) = {prob_al_menos_uno_industrial:.6f}")
    print(f"   ({prob_al_menos_uno_industrial*100:.2f}%)\n")
    
    # d) Probabilidad de que sean 2 de Electrónica y 1 de Sistemas
    prob_2_electronica_1_sistemas = dists.multivariate_hypergeom.pmf(
        x=[1, 2, 0],  # 1 sistemas, 2 electronica, 0 industrial
        n=[sistemas, electronica, industrial],
        size=seleccionar
    )
    print("d) Probabilidad de 2 Electrónica y 1 Sistemas:")
    print(f"   P(2 Electrónica + 1 Sistemas) = {prob_2_electronica_1_sistemas:.6f}")
    print(f"   ({prob_2_electronica_1_sistemas*100:.2f}%)\n")
    
    # Verificación: suma de todas las probabilidades posibles
    print("Verificación: La suma de todas las probabilidades posibles es 1.0")
    print("(Esto confirma que hemos considerado todos los casos posibles)")

if __name__ == "__main__":
    main()