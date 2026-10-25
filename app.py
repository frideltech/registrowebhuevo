import pandas as pd
import streamlit as st
# constantes que siempre deben estar en mayúsculas
NOMBRE_WEB_APP = "PAGINA WEB REGISTRO DEL HUEVO"
PUNTOS_XP_MISION=40
RANGO_MAXIMO=100
def CrearMision(mision,lugar,lider,nombreHuevo)->tuple[bool,dict]:
    try:
        mision = mision.strip()
        lugar = lugar.strip()
        lider = lider.strip()
        nombreHuevo = nombreHuevo.strip()
        if not mision or not lugar or not lider:
            return False, {}
        else:
            registroHuevo ={
                "mision": mision,
                "lugar": lugar,
                "lider": lider,
                "nombreHuevo": nombreHuevo,
                "puntosXP": PUNTOS_XP_MISION,
            }
            return True, registroHuevo
    except AttributeError:
        return False, {}
# CONFIGURACION DE LA PAGINA WEB
st.set_page_config(
    page_title=NOMBRE_WEB_APP,
    page_icon=":egg:",
    layout="wide")
# NICIACION DE LA MEMORIA Y DEL ESTADO DE LA PAGINA WEB
if "registroHuevoEstado" not in st.session_state:
    st.session_state.registroHuevoEstado = [{"mision": "Bautizo del Huevo", "lugar": "Aula C-16", "lider": "Leonardo", "nombreHuevo": "AJJ", "puntosXP": 50}]

# MENU LATERAL SIDEBAR
st.sidebar.title("Menú de Registro de Misiones del Huevo SIS-121 UCB")
st.sidebar.subheader("Navegacion del Sistema")
opcionMenu = st.sidebar.radio("Seleccione el Modulo:", ["Estado del Huevo", "Registro Mision","Ver Detalle Mision"])
# CABECERA PRINCIPAL
st.title(NOMBRE_WEB_APP)
st.caption("Sistema de Registro de Misiones del Huevo SIS-121 UCB")
st.divider()
# CUERPO DE LA WEB
# MODULO 1 ESTADO DEL HUEVO
if opcionMenu == "Estado del Huevo":
    st.header("Modulo 1: Estado del Huevo")
    columna1,columna2, column3 = st.columns(3)
    with columna1:
        st.metric(label="ESTADISTICA GENERAL DEL SISTEMAO DEL SERVIDOR",value=f"{RANGO_MAXIMO} % HP")
    with columna2:
        totalXP =sum(item["puntosXP"] for item in st.session_state.registroHuevoEstado)
        st.metric(label="PUNTOS DE EXPERIENCIA (XP) ACUMULADAS",value=f"{totalXP} XP", delta=f"{PUNTOS_XP_MISION} XP por Mision")
    with column3:
        st.metric(label="MISIONES REGISTRADAS",value=len(st.session_state.registroHuevoEstado))
# MODULO 2 REGISTRO DE MISION
elif opcionMenu == "Registro Mision":
    st.header("Modulo 2: Registro de Mision del Huevo")
    with st.form("formMision",clear_on_submit=True):
        misionInput = st.text_input("Ingrese el nombre de la Mision:")
        lugarInput = st.text_input("Ingrese el lugar de la Mision:")
        liderInput = st.text_input("Ingrese el nombre del lider de la Mision:")
        nombreHuevoInput = st.text_input("Ingrese el nombre del Huevo:")
        botonRegistrarMision = st.form_submit_button("Registrar Mision")
        if botonRegistrarMision:
            exito, registroHuevo = CrearMision(misionInput,lugarInput,liderInput,nombreHuevoInput)
            if exito:
                st.session_state.registroHuevoEstado.append(registroHuevo)
                st.success(f"Mision '{misionInput}' registrada exitosamente.")
            else:
                st.error("Error al registrar la mision. Por favor complete todos los campos.")
elif opcionMenu == "Ver Detalle Mision":
    st.header("Modulo 3: Ver Detalle de Misiones del Huevo")
    if len(st.session_state.registroHuevoEstado) > 0:
        dfMisiones= pd.DataFrame(st.session_state.registroHuevoEstado)
        st.dataframe(dfMisiones,user_container_width=True)
        st.download_button(label="Descargar Detalle de Misiones",
                           data=dfMisiones.to_csv(index=False).encode('utf-8'),
                           file_name="detalle_misiones.csv",mime="text/csv")
    else:
        st.warning("No hay misiones registradas para mostrar.")
    