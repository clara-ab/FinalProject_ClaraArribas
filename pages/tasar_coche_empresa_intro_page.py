
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

import pandas as pd

import pickle

import numpy as np

from huggingface_hub import hf_hub_download

# Librería para el menú de opciones:
from streamlit_option_menu import option_menu 

# # # # #  FIN LIBRERÍAS # # # # #

# Función para limpiar los datos antes de hacer predicciones
def limpiar_datos(df):
    # Convierte las columnas de texto a minúsculas y reemplaza guiones por espacios cuando sea necesario
    df['region'] = df['region'].str.lower()
    df['state'] = df['state'].str.lower()
    df['manufacturer'] = df['manufacturer'].str.lower()
    df['model'] = df['model'].str.replace("-", " ").str.lower()
    df['type'] = df['type'].str.lower()
    df['condition'] = df['condition'].str.lower()
    df['paint_color'] = df['paint_color'].str.lower()
    df['fuel'] = df['fuel'].str.lower()
    df['drive'] = df['drive'].str.lower()
    df['transmission'] = df['transmission'].str.lower()
    
    # Asegurarse de que 'odometer' y 'cylinders' son numéricos
    df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce')
    df['cylinders'] = pd.to_numeric(df['cylinders'], errors='coerce')
    
    return df

# Función para cargar el modelo desde Hugging Face
def cargar_modelo():
    # Descargar el modelo desde Hugging Face
    modelo_path = hf_hub_download(repo_id="clara-ab/random_forest_grid_model", filename="random_forest_grid_model.pkl");
    
    # Cargar el modelo descargado
    with open(modelo_path, "rb") as file:
        modelo = pickle.load(file);
    
    return modelo

# Función para cargar los encoders desde Hugging Face
def cargar_encoders():
    # Descargar el archivo de encoders desde Hugging Face
    encoders_path = hf_hub_download(repo_id="clara-ab/random_forest_grid_model", filename="encoders.pkl")
    
    # Cargar los encoders desde la ruta descargada
    with open(encoders_path, "rb") as file:
        encoders = pickle.load(file)
    
    return encoders


# # # # #  INICIO FUNCIÓN TASAR COCHE EMPRESA (1) # # # # #

# Se configura la página para poder aprovechar toda la página:
st.set_page_config(page_title = "🏢 Tasación - Flota Empresa 🏣", page_icon = ":car:", layout = "wide");

# Se aplica un color de fondo deseado #fffafe:
page_bg_color = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #fffafe;
    }
    </style>
    """
st.markdown(page_bg_color, unsafe_allow_html = True);

# # # Barra de Navegación Superior usando streamlit-options-menu # # #
with st.container():
    menu = option_menu(
        menu_title = None,  # No título para el menú
        options = ["Inicio", "Tasación - Particular", "Tasación - Empresa", "Sobre Nosotros", "Nuestro Método", "Contáctanos"],
        icons = ["house", "person-fill", "building", "info-circle", "clipboard-check", "phone"],
        orientation = "horizontal",  # Menú horizontal
        default_index = 2,  # Establecer "Inicio" como la opción por defecto
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
        switch_page("particular_page")
    elif menu == "Tasación - Empresa":
        pass
    elif menu == "Sobre Nosotros":
        switch_page("nosotros_page")
    elif menu == "Nuestro Método":
        st.write("En proceso...")
    elif menu == "Contáctanos":
        st.write("Contacto")

# Título - 🏢🚘 Tasación - Flota Empresa 🚗🏣:
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 🏢🚘 Tasación - Flota Empresa 🚗🏣 </h1>", unsafe_allow_html = True);

# Título para el Formulariode Datos de la Empresa:
st.markdown("## Datos de la Empresa");

# Campo - Nombre de la Empresa:
nombre_empresa = st.text_input("Nombre de la Empresa:", max_chars = 100);

# Campo - CIF:
cif_empresa = st.text_input("CIF de la Empresa:", max_chars = 9);

# Campo - Domicilio Fiscal:
domicilio_fiscal = st.text_input("Domicilio Fiscal:", max_chars = 200);

# Campo - Teléfono de contacto:
telefono_contacto = st.text_input("Teléfono de Contacto:", max_chars = 15);

# Campo - Correo electrónico:
email_contacto = st.text_input("Correo Electrónico de Contacto:", max_chars = 100);

# Campo - Persona de contacto
persona_contacto = st.text_input("Persona de Contacto en la Empresa:", max_chars = 100);


# Se añade un espacio:
st.markdown("<br>", unsafe_allow_html = True);

# Instrucciones adicionales antes de la descarga:
st.write("""
    ## Instrucciones para completar el archivo CSV
    
    A continuación, puedes descargar el archivo **CSV modelo** que te ayudará a completar la información de los coches que deseas vender. Este archivo contiene todas las columnas necesarias para una correcta tasación.

    **Importante:** Asegúrate de que el archivo CSV esté correctamente formateado con los datos requeridos para que podamos realizar una tasación precisa.

    ---
""");

# Ruta del archivo de Excel que se ofrece para descarga:
archivo_modelo = "data/raw/test_excel.xlsx"

# Botón - Descarga del archivo:
with open(archivo_modelo, "rb") as f:
    st.download_button(
        label = "📥 Descargar Excel Modelo",
        data = f,
        file_name = "modelo_coche.xlsx",
        mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    );


# Se añade un espacio:
st.markdown("<br>", unsafe_allow_html = True);

# Instrucciones para la carga del archivo:
st.write("""
    ---
    
    ## Subir tu archivo completado
    
    Una vez que hayas completado el archivo CSV con todos los detalles de los coches que deseas vender, puedes **subirlo** en el espacio que se encuentra a continuación.

    **Recuerda:** Verifica que el archivo esté correctamente formateado y contenga toda la información necesaria para cada vehículo. Nosotros procesaremos el archivo y te devolveremos las tasaciones correspondientes para cada coche.

    ¡**Sube tu archivo** para continuar con la tasación!
""");

# Subida de archivo CSV:
archivo_coche = st.file_uploader("Sube el archivo CSV con los coches a vender", type = "xlsx");

# Si el archivo es subido, procesarlo:
if archivo_coche is not None:
    # Leer el archivo Excel con pandas
    df_input = pd.read_excel(archivo_coche)
    
    # Mostrar las primeras filas del archivo cargado para verificar
    st.write("Datos cargados del archivo:")
    st.write(df_input.head())

    # Verificar que las columnas necesarias están presentes
    columnas_requeridas = [
        'region', 'year', 'manufacturer', 'model', 'condition', 'cylinders', 'fuel',
        'odometer', 'transmission', 'drive', 'type', 'paint_color', 'state'
    ]
    
    if not all(col in df_input.columns for col in columnas_requeridas):
        st.error("El archivo Excel no contiene todas las columnas necesarias.")
    else:
        # Cargar el modelo previamente guardado
        modelo = cargar_modelo();

        # Preprocesamiento de las variables si es necesario (por ejemplo, convertir categorías)

        # Aplicar la limpieza de datos al dataframe cargado
        df_input = limpiar_datos(df_input)

        # Cargar los encoders previamente guardados
        encoders = cargar_encoders();

        # Identificar las columnas categóricas en df_input
        categorical_cols = df_input.select_dtypes(include=["object"]).columns.tolist()

        df_original = df_input.copy();

        # Aplicar el LabelEncoder a las columnas categóricas en df_input
        for column in categorical_cols:
            # Usamos el diccionario de encoders y el método .get para aplicar el encoder correspondiente
            df_input[column] = df_input[column].apply(lambda x: encoders[column].transform([x])[0] if x in encoders[column].classes_ else -1)

        # Realizar predicciones con las variables del archivo
        predicciones = modelo.predict(df_input[columnas_requeridas])
        predicciones_originales = np.exp(predicciones);

        # Añadir las predicciones al DataFrame como una nueva columna
        df_original['predicted_price'] = predicciones_originales.round(0);

        # Mostrar el DataFrame con las predicciones
        st.write("Archivo con las predicciones:");
        st.write(df_original);

        # Guardar el archivo con las predicciones en un nuevo archivo Excel
        archivo_con_predicciones = "archivo_con_predicciones.xlsx"
        df_original.to_excel(archivo_con_predicciones, index=False)

        # Botón para que el usuario descargue el archivo con las predicciones
        with open(archivo_con_predicciones, "rb") as f:
            st.download_button(
                label = "📥 Descargar archivo con las predicciones",
                data = f,
                file_name = "archivo_con_predicciones.xlsx",
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            );


# Botón para volver al inicio en la barra lateral:
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("main_page");

# # # # #  FIN FUNCIÓN TASAR COCHE EMPRESA (1) # # # # #