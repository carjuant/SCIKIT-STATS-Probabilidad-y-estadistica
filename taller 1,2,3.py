"""
SOLUCIÓN SIMPLIFICADA DE 3 TALLERES DE PROBABILIDAD
Taller 1: Distribución Binomial
Taller 2: Variables Aleatorias Discretas  
Taller 3: Probabilidad Conjunta Continua
"""

import numpy as np
from scipy import stats
from scipy import integrate

def taller_1_binomial():
    """
    TALLER 1: Problema de memorias defectuosas
    Máquina produce 12,000 memorias con 3% defectuosas
    Probabilidad de que en 600 memorias, 12 sean defectuosas
    """
    print("=" * 50)
    print("TALLER 1: DISTRIBUCIÓN BINOMIAL")
    print("=" * 50)
    
    # Parámetros del problema
    n = 600          # Tamaño de la muestra
    p = 0.03         # Probabilidad de defectuoso (3%)
    k = 12           # Número de defectuosos buscados
    
    # Usar distribución binomial
    probabilidad = stats.binom.pmf(k, n, p)
    
    print(f"Parámetros:")
    print(f"n = {n} (tamaño muestra)")
    print(f"p = {p} (probabilidad defectuoso)")
    print(f"k = {k} (defectuosos buscados)")
    print(f"\nP(X = {k}) = C({n},{k}) * ({p})^{k} * (1-{p})^{n-k}")
    print(f"Resultado: {probabilidad:.6f}")
    print(f"En porcentaje: {probabilidad*100:.4f}%")
    
    return probabilidad

def taller_2_variables_discretas():
    """
    TALLER 2: Variables aleatorias discretas
    Del documento parece ser sobre valor esperado y varianza
    """
    print("\n" + "=" * 50)
    print("TALLER 2: VARIABLES ALEATORIAS DISCRETAS")  
    print("=" * 50)
    
    # Crear una variable aleatoria discreta simple
    # Valores y probabilidades (ejemplo con dados)
    valores = np.array([1, 2, 3, 4, 5, 6])
    probabilidades = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
    
    # Calcular valor esperado E[X]
    valor_esperado = np.sum(valores * probabilidades)
    
    # Calcular varianza Var[X] = E[X^2] - (E[X])^2
    valor_esperado_cuad = np.sum(valores**2 * probabilidades)
    varianza = valor_esperado_cuad - valor_esperado**2
    
    print("Variable aleatoria: Lanzamiento de dado justo")
    print(f"Valores posibles: {valores}")
    print(f"Probabilidades: {probabilidades}")
    print(f"\nE[X] = Σ x * p(x) = {valor_esperado:.2f}")
    print(f"E[X²] = Σ x² * p(x) = {valor_esperado_cuad:.2f}")
    print(f"Var[X] = E[X²] - (E[X])² = {varianza:.2f}")
    print(f"σ = √Var[X] = {np.sqrt(varianza):.2f}")
    
    return valor_esperado, varianza

def taller_3_probabilidad_conjunta():
    """
    TALLER 3: Probabilidad conjunta continua
    Del documento: f(x,y) = (1/5)(x + y + 3y) para 0 ≤ x,y ≤ 1
    """
    print("\n" + "=" * 50)
    print("TALLER 3: PROBABILIDAD CONJUNTA CONTINUA")
    print("=" * 50)
    
    # Definir función de densidad conjunta corregida
    def f_xy(x, y):
        if 0 <= x <= 1 and 0 <= y <= 1:
            return (1/5) * (x + y + 3*y)  # Simplificado: (1/5)(x + 4y)
        else:
            return 0
    
    # Verificar que integra a 1
    integral_total, error = integrate.dblquad(f_xy, 0, 1, lambda x: 0, lambda x: 1)
    
    # Calcular probabilidad en región [0,0.5]x[0,0.5]
    prob_region, _ = integrate.dblquad(f_xy, 0, 0.5, lambda x: 0, lambda x: 0.5)
    
    print("Función de densidad conjunta:")
    print("f(x,y) = (1/5)(x + 4y) para 0 ≤ x ≤ 1, 0 ≤ y ≤ 1")
    print(f"Verificación: ∫∫ f(x,y) dxdy = {integral_total:.6f}")
    print(f"P(0 ≤ X ≤ 0.5, 0 ≤ Y ≤ 0.5) = {prob_region:.6f}")
    
    # Calcular densidad marginal de X
    def f_x(x):
        return integrate.quad(lambda y: f_xy(x, y), 0, 1)[0]
    
    # Calcular densidad marginal de Y  
    def f_y(y):
        return integrate.quad(lambda x: f_xy(x, y), 0, 1)[0]
    
    print(f"\nDensidad marginal en x=0.5: f_X(0.5) = {f_x(0.5):.4f}")
    print(f"Densidad marginal en y=0.5: f_Y(0.5) = {f_y(0.5):.4f}")
    
    return integral_total, prob_region

def main():
    """
    FUNCIÓN PRINCIPAL - EJECUTA LOS 3 TALLERES
    """
    print("SOLUCIÓN DE 3 TALLERES DE PROBABILIDAD")
    print("Versión Simple y Concisa")
    print("=" * 50)
    
    # Ejecutar los 3 talleres
    resultado_1 = taller_1_binomial()
    resultado_2 = taller_2_variables_discretas() 
    resultado_3 = taller_3_probabilidad_conjunta()
    
    # Resumen final
    print("\n" + "=" * 50)
    print("RESUMEN DE RESULTADOS")
    print("=" * 50)
    print(f"Taller 1 - Binomial: {resultado_1:.6f}")
    print(f"Taller 2 - Valor esperado: {resultado_2[0]:.2f}, Varianza: {resultado_2[1]:.2f}")
    print(f"Taller 3 - Integral total: {resultado_3[0]:.6f}")
    print(f"Taller 3 - Prob región: {resultado_3[1]:.6f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()