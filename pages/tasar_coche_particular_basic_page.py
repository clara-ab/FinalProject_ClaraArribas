
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# Librería para el menú de opciones:
from streamlit_option_menu import option_menu  

# # # # #  FIN LIBRERÍAS # # # # #


# # # # #  INICIO FUNCIÓN TASAR COCHE PARTICULAR (2) # # # # #

# Se configura la página para poder aprovechar toda la página:
st.set_page_config(page_title = "👩🏽 Tasación - Particular 👨🏼", page_icon = ":car:", layout = "wide");

# Se aplica un color de fondo #f5dae0:
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

# Función para validar si un texto contiene solo letras:
def validar_letras(texto): return texto.isalpha();

# Función para validar un correo electrónico:
def validar_email(email): return '@' in email and '.' in email;

# Lista de opciones para el fabricante
opciones_fabricante = [
    'gmc', 'chevrolet', 'toyota', 'ford', 'jeep', 'nissan', 'mazda',
    'cadillac', 'honda', 'dodge', 'buick', 'chrysler', 'volvo', 'audi',
    'infiniti', 'lincoln', 'acura', 'hyundai', 'mercedes benz', 'bmw',
    'mitsubishi', 'subaru', 'volkswagen', 'porsche', 'kia', 'fiat',
    'land rover', 'mercury', 'renault'
];

# Lista de opciones para el tipo de coche
tipos_coche = [
    'pickup', 'truck', 'other', 'coupe', 'SUV', 'hatchback',
    'mini-van', 'sedan', 'offroad', 'convertible', 'wagon', 'van',
    'bus'
]

# Título - 👩🏽🚘 Tasación - Coche Particular 🚗👨🏼:
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 👩🏽🚘 Tasación - Coche Particular 🚗👨🏼 </h1>", unsafe_allow_html = True);

# Título - Datos Básicos:
st.markdown("## DATOS BÁSICOS");

# Campo - Año de Fabricación:
year_fabricacion = st.number_input("Año de fabricación del coche:", min_value = 1900, max_value = 2025);
st.session_state.year_fabricacion = year_fabricacion; # Se guarda el año de fabricación para poder invocarlo donde sea

# Campo - Fabricante:
fabricante = st.selectbox("Selecciona el fabricante:", opciones_fabricante)
st.session_state.fabricante = fabricante ; # Se guarda el fabricante para poder invocarlo donde sea

# Campo - Modelo:
modelo = st.text_input("Modelo:");
st.session_state.modelo =  modelo.lower().replace('-', ' '); # Se guarda el modelo para poder invocarlo donde sea

# Campo - Tipo de Coche:
tipo_coche = st.selectbox("Tipo de Coche:", tipos_coche);
st.session_state.tipo_coche = tipo_coche; # Se guarda el tipo del coche para poder invocarlo donde sea

# Campo - Estado del Coche:
estado_coche = st.selectbox("Estado del Coche:", ['good', 'excellent', 'like new', 'new', 'fair', 'salvage']);
st.session_state.estado_coche = estado_coche;  # Se guarda el estado del coche para poder invocarlo donde sea

# Campo - Kilometraje: 
numero_millas = st.number_input("Número de Millas:", min_value = 0);
st.session_state.numero_millas = numero_millas;  # Se guarda el kilometraje del coche para poder invocarlo donde sea

# Campo - Color del Coche:
color_coche = st.selectbox("Color del coche:", ['white', 'blue', 'red', 'black', 'silver', 'grey', 'brown', 'yellow', 'orange', 'green', 'custom', 'purple']);
st.session_state.color_coche = color_coche;  # Se guarda el color del coche para poder invocarlo donde sea


# Se añade un espacio:
st.markdown("<br>", unsafe_allow_html=True);

# Botón para pasar a la siguiente página del formulario:
if st.button("Siguiente  ➡️  Detalles Técnicos"): switch_page("tasar_coche_particular_tecnicos_page");

# Botón para volver al inicio en la barra lateral:
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("main_page");


# # # # #  FIN FUNCIÓN TASAR COCHE PARTICULAR (2) # # # # #