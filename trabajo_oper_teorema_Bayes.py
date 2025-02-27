import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calcular_probabilidad(P_A, P_B_A, alpha):
    P_not_A = 1 - P_A
    P_B_not_A = 1 - alpha
    P_B = (P_B_A * P_A) + (P_B_not_A * P_not_A)
    P_A_B = (P_B_A * P_A) / P_B
    return P_A_B

def main():
    # Título de la aplicación
    st.title("Calculadora de Probabilidad de COVID-19 con el Teorema de Bayes")

    # Entrada de datos con sliders
    P_A = st.slider("Prevalencia (P(A), Probabilidad inicial de tener COVID-19)", 0.01, 1.0, 0.04)
    alpha = st.slider("Especificidad de la prueba (P(¬B | ¬A) = α)", 0.01, 1.0, 0.95)

    # Crear un rango de valores para la sensibilidad
    sensibilidad_values = np.linspace(0.01, 1.0, 100)
    probabilidades = [calcular_probabilidad(P_A, s, alpha) for s in sensibilidad_values]

    # Mostrar la probabilidad con valores actuales
    P_B_A = st.slider("Sensibilidad de la prueba (P(B | A))", 0.01, 1.0, 0.73)
    probabilidad_final = calcular_probabilidad(P_A, P_B_A, alpha)
    st.write(f"La probabilidad de tener COVID-19 dado un resultado positivo es: **{probabilidad_final:.2%}**")

    # Crear la gráfica
    fig, ax = plt.subplots()
    ax.plot(sensibilidad_values, probabilidades, label="P(A|B) vs Sensibilidad", color="blue")
    ax.axvline(P_B_A, color="red", linestyle="--", label=f"Valor Actual: {P_B_A:.2f}")
    ax.set_xlabel("Sensibilidad (P(B | A))")
    ax.set_ylabel("Probabilidad de tener COVID-19 (P(A | B))")
    ax.set_title("Efecto de la Sensibilidad en P(A|B)")
    ax.legend()

    # Mostrar la gráfica en Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()
