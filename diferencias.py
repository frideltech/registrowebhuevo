import streamlit as st
print ("Hola mundo")   -    st.write("Hola mundo")
input ("Ingrese su nombre: ")  - st.text_input("Ingrese su nombre: ")
int(input("Ingrese su edad: "))  - st.number_input("Ingrese su edad: ", min_value=0, max_value=120)
print(f"Su nombre es {nombre} y su edad es {edad}")  - st.write(f"Su nombre es {nombre} y su edad es {edad}") - st.metric("Nombre y Edad", {nombre})
variableList={"nombre": nombre, "edad": edad} - st.json(variableList)
while True:
    st.write("Este es un bucle infinito. Presiona 'Stop' para detenerlo.")
-
st.sidebar.write("Este es un bucle infinito. Presiona 'Stop' para detenerlo.")
st.sidebar.selectbox("Seleccione una opción:", ["Opción 1", "Opción 2", "Opción 3"])