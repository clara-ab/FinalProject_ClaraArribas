
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para poder utilizar Streamlit:
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# Librería para utilizar el menú de opciones (barra de navegación):
from streamlit_option_menu import option_menu  

# # # # # FIN LIBRERÍAS # # # # #



# # # # # INICIO NUESTRO MÉTODO FUNCTION # # # # #

# Configuración de la página:
st.set_page_config(page_title=" ⚙️ Nuestro Método 🖥️", page_icon=":car:", layout="wide");

# Se aplica el color de fondo deseado:
page_bg_color = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #fffafe;
    }
    </style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True);

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

        # Se establece visualmente que se está en la pantalla de 'Nuestro Método' [index = 4]
        default_index = 4,

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
        switch_page("empresa_page"); 
    elif menu == "Sobre Nosotros":
        switch_page("nosotros_page"); 
    elif menu == "Nuestro Método":
        pass  # metodo_page es Nuestro Método por lo que no se hace nada si hacen click
    elif menu == "Contáctanos":
        switch_page("contacto_page");

# Espacio:
st.markdown("<br>", unsafe_allow_html = True);

# Título ⚙️ Nuestro Método 🖥️:
st.markdown("<h1 style='text-align: center; font-family: \"Droid Sans Mono\", monospace;'>⚙️ Nuestro Método 🖥️  </h1>", unsafe_allow_html=True);

# Espacio:
st.markdown("<br>", unsafe_allow_html=True)

# Texto explicativo del método:
st.write("""
    ## 🔍 ¿Cómo desarrollamos el modelo de predicción?
    
    El principal objetivo de este proyecto es predecir el **precio de venta** de un coche usado a partir de sus características.
    Para ello, analizamos nuestra base de datos con más de **400,000 anuncios**.
    
    ### 🏁 Pasos del proceso:

    **1️⃣ Lectura y Guardado de Datos:**
    - Importamos y exploramos el dataset inicial.
    
    **2️⃣ Análisis Exploratorio de Datos:**
    - Eliminación de constantes y duplicados.
    - Estudio detallado de valores nulos y su tratamiento.
    - Análisis de la distribución de las variables numéricas y categóricas.
    
    **3️⃣ Tratamiento de Nulos:**
    - **Fabricante:** Modelo de lenguaje RoBERTa (`roberta-base-squad2`).
    - **Cilindrada & Tracción:** Combinación de otras variables y ajuste manual.
    - **Combustible & Transmisión:** Búsqueda de palabras clave en el modelo y descripción.
    - **Pintura Exterior:** Inferencia desde la descripción (rellenando ~50,000 nulos).
    - **Kilometraje:** Expresiones regulares para detección y ajuste automático.
    
    **4️⃣ Codificación de Variables Categóricas:**
    - Uso de `LabelEncoder` optimizado para múltiples columnas.
    
    **5️⃣ Selección de Características Relevantes:**
    - Aplicación del análisis del Factor de Inflación de la Varianza (VIF).
    
    **6️⃣ Entrenamiento del Modelo:**
    - Algoritmo seleccionado: **Random Forest Regressor**.
    - Optimización de hiperparámetros con `GridSearchCV`.
    - Evaluación del rendimiento del modelo.

    Finalmente, el modelo entrenado ha sido almacenado en **Hugging Face Hub**, permitiendo su integración sin sobrecargar GitHub.
""");

# Espacio:
st.markdown("<br>", unsafe_allow_html = True);

# Botón para descargar el notebook del proyecto:
with open("src/FinalProject_ClaraArribas.ipynb", "rb") as file:
    st.download_button(
        label = "📥 Descargar Notebook Completo",
        data = file,
        file_name = "FinalProject_ClaraArribas.ipynb",
        mime = "application/octet-stream"
    );

# Espacio:
st.markdown("<br>", unsafe_allow_html=True)


# # # # # FIN NUESTRO MÉTODO FUNCTION # # # # #
