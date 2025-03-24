
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# Librería para poder utilizar el tipo de datos pickle:
import pickle

# Librería para poder utilizar el tipo de datos pandas:
import pandas as pd

# Librería para poder emplear expresiones matemáticas:
import numpy as np

# Librería para poder conectarse al Hub de Hugging Face:
from huggingface_hub import hf_hub_download

# Librería para el menú de opciones:
from streamlit_option_menu import option_menu  

# # # # # FIN LIBRERÍAS # # # # #


# Configuración de la página
st.set_page_config(page_title="👩🏽 Tasación - Particular 👨🏼", page_icon=":car:", layout="wide");

# Estilos CSS para mejorar la apariencia
def aplicar_estilos():
    st.markdown(
        """
        <style>

        [data-testid="stAppViewContainer"] {
            background-color: #fffafe;
        }
        .stButton>button {
            background-color: #fff0fb; 
            color: #252124;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #ffffff;
            border: 2px solid #ffc0f1;
            color: #252124;
        }
        .stSidebar .stButton>button {
            background-color: #fff0fb;  /* Color pastel para el botón de la barra lateral */
            color: #252124;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
        }
        .stSidebar .stButton>button:hover {
            background-color: #ffffff;
            color: #252124;
        }

        .margen-error {
            padding: 15px;
            background-color: #fff0fb;
            border-radius: 8px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .margen-error h3 {
            color: #252124;
            font-weight: 600;
        }
        .margen-error p {
            font-size: 16px;
            color: #252124;
        }
        </style>
        """,
        unsafe_allow_html=True
    );

# Se aplican todos los estilos definidos a la página:
aplicar_estilos();

# # # Barra de Navegación Superior usando streamlit-options-menu # # #
with st.container():
    menu = option_menu(
        menu_title = None,  # No título para el menú
        options = ["Inicio", "Tasación - Particular", "Tasación - Empresa", "Sobre Nosotros", "Nuestro Método", "Contáctanos"],
        icons = ["house", "person-fill", "building", "info-circle", "clipboard-check", "phone"],
        orientation = "horizontal",  # Menú horizontal
        default_index = 1,  # Establecer "Inicio" como la opción por defecto
        styles={
            "container": {"padding": "0!important", "background-color": "#fffafe"},  # Fondo como el del resto de la página
            "icon": {"color": "#5c0048", "font-size": "20px"},  # Color de los íconos
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "padding": "5px",
                "margin": "0px",
                "color": "#5c0048",
                "font-weight": "bold",
            },
            "nav-link-selected": {"background-color": "#eeb1e1"},  # Color de la opción seleccionada
        }
    )

    # Redirigir según la opción seleccionada:
    if menu == "Inicio":
        switch_page("main_page")
    elif menu == "Tasación - Particular":
        pass
    elif menu == "Tasación - Empresa":
        switch_page("empresa_page")
    elif menu == "Sobre Nosotros":
        switch_page("nosotros_page")
    elif menu == "Nuestro Método":
        st.write("En proceso...")
    elif menu == "Contáctanos":
        st.write("Contacto")


# Función para cargar el modelo (se accede al hub de Hugging Face)::
def cargar_modelo():
    modelo_path = hf_hub_download(repo_id="clara-ab/random_forest_grid_model", filename="random_forest_grid_model.pkl");
    with open(modelo_path, "rb") as file:
        return pickle.load(file);

# Función para cargar los encoders (se accede al hub de Hugging Face):
def cargar_encoders():
    encoders_path = hf_hub_download(repo_id="clara-ab/random_forest_grid_model", filename="encoders.pkl");
    with open(encoders_path, "rb") as file:
        return pickle.load(file);



# # # # #  INICIO FUNCIÓN TASADOR PARTICULAR # # # # #

# Título de la página:
st.markdown("## 🚗 Tasación de tu coche");

# Se añade un espacio:
st.markdown("<br>", unsafe_allow_html=True);

# Texto:
st.write("Revisa los datos ingresados y presiona el botón para obtener una tasación estimada.");

# Se crea un DataFrame con los datos ingresados:
data = {
    "region": [st.session_state.get("region_estado", None)],
    "year": [st.session_state.get("year_fabricacion", None)],
    "manufacturer": [st.session_state.get("fabricante", None)],
    "model": [st.session_state.get("modelo", None)],
    "condition": [st.session_state.get("estado_coche", None)],
    "cylinders": [st.session_state.get("numero_cilindrada", None)],
    "fuel": [st.session_state.get("tipo_combustible", None)],
    "odometer": [st.session_state.get("numero_millas", None)],
    "transmission": [st.session_state.get("tipo_transmision", None)],
    "drive": [st.session_state.get("tipo_traccion", None)],
    "type": [st.session_state.get("tipo_coche", None)],
    "paint_color": [st.session_state.get("color_coche", None)],
    "state": [st.session_state.get("siglas_estado", None)]
}
df_input = pd.DataFrame(data);

# Se cargan los codificadores del hub de Hugging Face:
encoders = cargar_encoders();

# Se aplican los encoders a las columnas categóricas:
categorical_cols = df_input.select_dtypes(include=["object"]).columns.tolist();
for column in categorical_cols:
    df_input[column] = df_input[column].apply(lambda x: encoders[column].transform([x])[0] if x in encoders[column].classes_ else -1);

# Se muestran los datos ingresados en un contenedor extendible:
with st.expander("📋 Datos ingresados para la predicción"):
    st.dataframe(df_input, use_container_width=True);

# Se añade un espacio:
st.markdown("<br>", unsafe_allow_html=True);

# Se agrega el texto explicativo sobre el margen de error en MAPE con clases para el estilo:
st.markdown("""
    <div class="margen-error">
        <h3>Margen de error en la predicción</h3>
        <p>
            La predicción tiene un margen de error de <strong>±2.58%</strong>, lo que significa que el valor estimado podría variar un 
            2.58% más o menos respecto al valor real. Por ejemplo, si la tasación estimada es de <strong>10,000 €</strong>, la diferencia 
            podría ser de <strong>±258 €</strong>.
        </p>
    </div>
""", unsafe_allow_html=True);

# Se añade un espacio:
st.markdown("<br>", unsafe_allow_html=True);

# Se carga el modelo del hub de Hugging Face:
modelo = cargar_modelo();

# Se realiza la predicción cuando el usuario presiona el botón:
if st.button("🔍 Realizar Tasación"):
    prediccion = modelo.predict(df_input);
    prediccion_original = np.exp(prediccion); # Se realiza la transformación exponencial dado que el modelo está entrenado con los datos en logarítmico
    st.success(f"💰 El valor estimado de tu coche es: **{prediccion_original[0]:,.0f} $**");



# Botón para volver al inicio en la barra lateral
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("main_page");


# # # # #  FIN FUNCIÓN TASADOR PARTICULAR # # # # #

