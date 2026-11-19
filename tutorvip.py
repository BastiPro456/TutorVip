import streamlit as st
import time

alumnos = []
profesores = []
notas = []

st.title("Registro de Notas de Alumnos")

import streamlit as st
import time


if "Ingresado" not in st.session_state:
    st.session_state["Ingresado"] = False


if not st.session_state["Ingresado"]:

    nombre = st.text_input("Nombre del Profesor/a")

    if st.button("Ingresado"):
        if nombre:
            st.session_state["Ingresado"] = True
            st.session_state["nombre"] = nombre
            st.rerun()
        else:
            st.warning("Ingrese el nombre del profesor.")

if "registros" not in st.session_state:
    st.session_state.registros = {}

if st.session_state["Ingresado"]:

    st.header("Ingrese los nombres de los alumnos")

    entrada_alumnos = st.text_input(
        "Ingrese los nombres separados por comas:"
    )

    if entrada_alumnos:

        lista_alumnos = entrada_alumnos.split(",")

        st.header("Ingrese las notas")

        for alumno in lista_alumnos:

            alumno = alumno.strip()

            if alumno:

                st.subheader(f"Alumno: {alumno}")

                nota = st.number_input(
                    f"Nota de {alumno}",
                    min_value=1,
                    max_value=10,
                    value=1,
                    key=f"nota_{alumno}"
                )

                if st.button(
                    f"Guardar nota de {alumno}",
                    key=f"guardar_{alumno}"
                ):
                    st.session_state.registros[alumno] = nota

                    st.success(
                        f"Nota de {alumno} guardada correctamente"
                    )

    if st.session_state.registros:

        st.header("Registro de notas")

        tabla = [
            {"Alumno": nombre, "Nota": nota}
            for nombre, nota in st.session_state.registros.items()
        ]

        st.table(tabla)

        st.title("Estadisticas de los alumnos")
        notas = list(st.session_state.registros.values())
        if len(notas) > 0:

            st.header("estadisticas")
            promedio = sum(notas) / len(notas)
            nota_max = max(notas)
            nota_min = min(notas)

            aprobados = 0
            desaprobados = 0

            for n in notas:
                if n >= 7:
                    aprobados += 1
                else:
                    desaprobados += 1   
 
            st.write("Promedio:", round(promedio, 2))
            st.write("Aprobados:", aprobados)
            st.write("Desaprobados:", desaprobados)
            st.write("Nota máxima:", nota_max)
            st.write("Nota mínima:", nota_min)
