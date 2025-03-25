
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para poder utilizar Streamlit:
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# Librería para utilizar el menú de opciones (barra de navegación):
from streamlit_option_menu import option_menu 

# Librería para poder utilizar el tipo de datos pandas:
import pandas as pd

# Librería para poder utilizar lel tipo de datos pickle:
import pickle

# Librería para poder emplear expresiones matemáticas:
import numpy as np

# Librería para poder conectarse al Hub de Hugging Face:
from huggingface_hub import hf_hub_download

# # # # #  FIN LIBRERÍAS # # # # #



# # # # #  INICIO FUNCIÓN TASAR COCHE EMPRESA (1) # # # # #

# Configuración de la página:
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

# Función para limpiar los datos antes de hacer predicciones:
def limpiar_datos(df):

    # Se convierten las columnas de texto a minúsculas y reemplaza guiones por espacios cuando sea necesario:
    df['region'] = df['region'].str.lower();
    df['state'] = df['state'].str.lower();
    df['manufacturer'] = df['manufacturer'].str.lower();
    df['model'] = df['model'].str.replace("-", " ").str.lower();
    df['type'] = df['type'].str.lower();
    df['condition'] = df['condition'].str.lower();
    df['paint_color'] = df['paint_color'].str.lower();
    df['fuel'] = df['fuel'].str.lower();
    df['drive'] = df['drive'].str.lower();
    df['transmission'] = df['transmission'].str.lower();
    
    # Se asegura de que 'odometer' y 'cylinders' son numéricos:
    df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce');
    df['cylinders'] = pd.to_numeric(df['cylinders'], errors='coerce');
    
    return df

# Función para cargar el modelo desde Hugging Face:
def cargar_modelo():

    # Se descarga el modelo desde Hugging Face:
    modelo_path = hf_hub_download(repo_id = "clara-ab/random_forest_grid_model", filename = "random_forest_grid_model.pkl");
    
    # Se carga el modelo descargado:
    with open(modelo_path, "rb") as file:
        modelo = pickle.load(file);
    
    return modelo

# Función para cargar el diccionario de encoders desde Hugging Face:
def cargar_encoders():

    # Se descarga el diccionario de encoders desde Hugging Face:
    encoders_path = hf_hub_download(repo_id = "clara-ab/random_forest_grid_model", filename = "encoders.pkl");
    
    # Se cargan los encoders desde la ruta descargada
    with open(encoders_path, "rb") as file:
        encoders = pickle.load(file);
    
    return encoders


# # # Barra de Navegación Superior # # #
with st.container():
    # Se define la barra de navegación:
    menu = option_menu(

        # No se coloca título al menú:
        menu_title = None,

        # Se colocan las opciones de la barra de navegación:
        options = ["Inicio", "Tasación - Particular", "Tasación - Empresa", "Sobre Nosotros", "Nuestro Método", "Contáctanos"],

        # Se colocan iconos acompañando a los textos:
        icons = ["house", "person-fill", "building", "info-circle", "clipboard-check", "phone"],

        # Orientación horizontal de la barra:
        orientation = "horizontal",

        # Se establece visualmente que se está en la pantalla de 'Tasación - Empresas' [index = 2]
        default_index = 2,

        # Se define el estilo de la barra de navegación:
        styles={
            "container": {"padding": "0!important", "background-color": "#fffafe"},  # Se establece el color del container como el color de fondo
            "icon": {"color": "#5c0048", "font-size": "20px"},  # Color de los íconos
            # Estilo de las letras:
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
    );

    # Se redirije a la página correspondiente según la opción seleccionada:
    if menu == "Inicio":
        switch_page("main_page")
    elif menu == "Tasación - Particular":
        switch_page("particular_page");
    elif menu == "Tasación - Empresa":
        pass; # empresa_page es Tasación - Empresa por lo que no se hace nada si hacen click
    elif menu == "Sobre Nosotros":
        switch_page("nosotros_page");
    elif menu == "Nuestro Método":
        switch_page("metodo_page");
    elif menu == "Contáctanos":
        switch_page("contacto_page");


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

# Espacio:
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

# Espacio:
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
    # Se lee el archivo Excel con pandas
    df_input = pd.read_excel(archivo_coche);
    
    # Se muestran las primeras filas del archivo cargado para verificar que se ha subido correctamente:
    st.write("Datos cargados del archivo:");
    st.write(df_input.head());

    # Se verifica que las columnas necesarias están presentes:
    columnas_requeridas = [
        'region', 'year', 'manufacturer', 'model', 'condition', 'cylinders', 'fuel',
        'odometer', 'transmission', 'drive', 'type', 'paint_color', 'state'
    ];
    
    # Si no son las columnas correctas, se notifica:
    if not all(col in df_input.columns for col in columnas_requeridas):
        st.error("El archivo Excel no contiene todas las columnas necesarias.")

    # Si sí son las columnas correctas, se carga el modelo descargado del hub Hugging Face y se aplica la predicción:
    else:
        # Se carga el modelo con la función:
        modelo = cargar_modelo();

        # Se invoca a la función para limpiar los datos del DataFrame:
        df_input = limpiar_datos(df_input);

        # Se cargan el diccionario de codificadores con la función:
        encoders = cargar_encoders();

        # Se identifican las columnas categóricas en df_input para aplicar la codificación:
        categorical_cols = df_input.select_dtypes(include=["object"]).columns.tolist();

        # Antes de aplicar la codificación y "dejar de entender" las variables categóricas, se hace una copia para mantenerlas:
        df_original = df_input.copy();

        # Se aplica el LabelEncoder a las columnas categóricas en df_input:
        for column in categorical_cols:
            # Se usa el diccionario de encoders y se aplica a las columnas categóricas (si no se encuentra una equivalencia en los diccionarios se coloca un -1):
            df_input[column] = df_input[column].apply(lambda x: encoders[column].transform([x])[0] if x in encoders[column].classes_ else -1);

        # Se realizan las predicciones con las variables del archivo:
        predicciones = modelo.predict(df_input[columnas_requeridas]);

        # Se realiza la transformación inversa a la que se utiliza para entrenar el modelo:
        predicciones_originales = np.exp(predicciones);

        # Se añaden las predicciones al DataFrame original (con las variables categóricas sin codificar) como una nueva columna:
        df_original['predicted_price'] = predicciones_originales.round(0);

        # Se muestra el DataFrame con las predicciones
        st.write("Archivo con las predicciones:");
        st.write(df_original);

        # Se guarda el archivo con las predicciones en un nuevo archivo Excel:
        archivo_con_predicciones = "archivo_con_predicciones.xlsx";
        df_original.to_excel(archivo_con_predicciones, index = False);

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