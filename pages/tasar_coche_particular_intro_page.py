
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# Librería para el menú de opciones:
from streamlit_option_menu import option_menu  

# # # # #  FIN LIBRERÍAS # # # # #


# # # # #  INICIO FUNCIÓN TASAR COCHE PARTICULAR (1) # # # # #

# Se configura la página para poder aprovechar toda la página:
st.set_page_config(page_title = "👩🏽 Tasación - Particular 👨🏼", page_icon = ":car:", layout = "wide");

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


# Lista de estados de EE.UU. con las siglas:
estados_eeuu = [
    'Alabama (AL)', 'Alaska (AK)', 'Arizona (AZ)', 'Arkansas (AR)', 'California (CA)', 'Colorado (CO)', 'Connecticut (CT)', 
    'Delaware (DE)', 'Florida (FL)', 'Georgia (GA)', 'Hawaii (HI)', 'Idaho (ID)', 'Illinois (IL)', 'Indiana (IN)', 'Iowa (IA)', 
    'Kansas (KS)', 'Kentucky (KY)', 'Louisiana (LA)', 'Maine (ME)', 'Maryland (MD)', 'Massachusetts (MA)', 'Michigan (MI)', 
    'Minnesota (MN)', 'Mississippi (MS)', 'Missouri (MO)', 'Montana (MT)', 'Nebraska (NE)', 'Nevada (NV)', 'New Hampshire (NH)', 
    'New Jersey (NJ)', 'New Mexico (NM)', 'New York (NY)', 'North Carolina (NC)', 'North Dakota (ND)', 'Ohio (OH)', 
    'Oklahoma (OK)', 'Oregon (OR)', 'Pennsylvania (PA)', 'Rhode Island (RI)', 'South Carolina (SC)', 'South Dakota (SD)', 
    'Tennessee (TN)', 'Texas (TX)', 'Utah (UT)', 'Vermont (VT)', 'Virginia (VA)', 'Washington (WA)', 'West Virginia (WV)', 
    'Wisconsin (WI)', 'Wyoming (WY)', 'Washington D.C. (DC)'
]


# Título - 👩🏽🚘 Tasación - Coche Particular 🚗👨🏼
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 👩🏽🚘 Tasación - Coche Particular 🚗👨🏼</h1>", unsafe_allow_html = True);


# Título - Datos de Contacto:
st.markdown("## DATOS DE CONTACTO");

# Campo - Nombre:
nombre = st.text_input("Nombre:");
if nombre and not validar_letras(nombre): st.error("El nombre solo puede contener letras."); # Se comprueba si solo tiene letras

# Campo - Apellido:
apellidos = st.text_input("1er Apellido:");
if apellidos and not validar_letras(apellidos): st.error("Los apellidos solo pueden contener letras."); # Se comprueba si solo tiene letras

# Campo - Email:
email = st.text_input("Correo electrónico:");
if email and not validar_email(email): st.error("Por favor ingresa un correo electrónico válido."); # Se comprueba si es un correo válido (tiene @ y .)

# Campo - Número de Teléfono:
telefono = st.text_input("Número de Teléfono:");
if telefono and not telefono.isdigit(): st.error("El número de teléfono solo puede contener números."); # Se comprueba si solo tiene números.

# Campo - Estado de EEUU:
estado_seleccionado = st.selectbox("Selecciona el estado de EE.UU.:", estados_eeuu);

# Campo - Región de EEUU:
region_estado = st.text_input("Región de EEUU:");
if region_estado and not validar_letras(region_estado): st.error("Las regiones solo pueden contener letras."); # Se comprueba si solo tiene letras
st.session_state.region_estado = region_estado.lower();

# Para el modelo harán falta las siglas por lo que se guardan aisladas:
if estado_seleccionado:
    siglas_estado = estado_seleccionado.split(" (")[1][:-1];
    st.session_state.siglas_estado = siglas_estado.lower(); # Se guardan las siglas para poder invocarlas donde sea



# Se añade un espacio:
st.markdown("<br>", unsafe_allow_html=True);


# Botón para pasar a la siguiente página del formulario:
if st.button("Siguiente  ➡️  Datos Básicos"): switch_page("tasar_coche_particular_basic_page");

# Botón para volver al inicio en la barra lateral:
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("main_page");

# # # # #  FIN FUNCIÓN TASAR COCHE PARTICULAR (1) # # # # #