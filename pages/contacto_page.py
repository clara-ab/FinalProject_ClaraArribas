
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para poder utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# Librería para el menú de opciones:
from streamlit_option_menu import option_menu 

# # # # #  FIN LIBRERÍAS # # # # #


# # # # # INICIO CONTACTO FUNCTION # # # # #

# Se configura la página para aprovechar todo el espacio:
st.set_page_config(page_title=" 🤗 Sobre Nosotros 🧑🏿‍🤝‍🧑🏽", page_icon=":car:", layout="wide");

# Se aplica el color de fondo deseado:
page_bg_color = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #fffafe;
    }
    </style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True);

# # # Barra de Navegación Superior usando streamlit-options-menu # # #
with st.container():
    menu = option_menu(
        menu_title = None,  # No título para el menú
        options = ["Inicio", "Tasación - Particular", "Tasación - Empresa", "Sobre Nosotros", "Nuestro Método", "Contáctanos"],
        icons = ["house", "person-fill", "building", "info-circle", "clipboard-check", "phone"],
        orientation = "horizontal",  # Menú horizontal
        default_index = 5,  # Establecer "Inicio" como la opción por defecto
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
        switch_page("empresa_page")
    elif menu == "Sobre Nosotros":
        switch_page("nosotros_page")
    elif menu == "Nuestro Método":
        switch_page("metodo_page")
    elif menu == "Contáctanos":
        pass

# Espacio
st.markdown("<br>", unsafe_allow_html=True)

# Título centrado
st.markdown("<h1 style='text-align: center;'>📞 Contáctanos </h1>", unsafe_allow_html=True)

# Espacio
st.markdown("<br>", unsafe_allow_html=True)

# Dos columnas para diseño equilibrado
col1, col2 = st.columns([1, 2])

with col1:
    st.image("images/contacto_image.png", use_container_width=True)

with col2:
    st.write("""
        ### ¿Tienes dudas o necesitas más información?
        
        📧 **Email:** contacto@clarascarcorner.com  
             
        📍 **Dirección:** Calle Automóviles, 5, New York, Estados Unidos  
             
        ☎ **Teléfono:** +34 123 456 789  
             
        🕘 **Horario:** Lunes a Viernes - 9:00 a 18:00
        
        ¡Déjanos un mensaje y nos pondremos en contacto contigo lo antes posible!
    """)

    # Formulario de contacto
    with st.form("contact_form"):
        nombre = st.text_input("Nombre")
        email = st.text_input("Correo Electrónico")
        mensaje = st.text_area("Mensaje")
        enviar = st.form_submit_button("Enviar")

        if enviar:
            st.success("✅ ¡Gracias por contactarnos! Te responderemos pronto.")

# Espacio
st.markdown("<br>", unsafe_allow_html=True)

# # # # # FIN CONTACTO FUNCTION # # # # #