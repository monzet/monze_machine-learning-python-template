import streamlit as st
import joblib
import numpy as np

# Cargar el modelo
with open('models/modelo_entrenado.pkl', 'rb') as file:
    model = joblib.load('models/modelo_entrenado.pkl')



st.title("Predicción de Diabetes")

# Inputs del usuario
pregnancies = st.number_input('Embarazos', min_value=0)
glucose = st.number_input('Glucosa', min_value=0)
blood_pressure = st.number_input('Presión arterial', min_value=0)
skin_thickness = st.number_input('Espesor de piel', min_value=0)
insulin = st.number_input('Insulina', min_value=0)
bmi = st.number_input('IMC', min_value=0.0, format="%.1f")
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, format="%.3f")
age = st.number_input('Edad', min_value=0)

# Botón para predecir
if st.button('Predecir'):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error('Posible diabetes')
    else:
        st.success('No parece haber diabetes')