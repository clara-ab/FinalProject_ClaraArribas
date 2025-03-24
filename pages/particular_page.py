
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para poder utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# Librería para el menú de opciones:
from streamlit_option_menu import option_menu 

# # # # #  FIN LIBRERÍAS # # # # #

# # # # # INICIO FUNCIÓN PARTICULAR # # # # #

# Se configura la página para poder aprovechar toda la página:
st.set_page_config(page_title = "👩🏽 Particular 👨🏼", page_icon = ":car:", layout = "wide");

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


# Título - 👩🏽 Particular 👨🏼:
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 👩🏽 Particular 👨🏼 </h1>", unsafe_allow_html = True);

# Se añade un espacio:
st.markdown("<br>", unsafe_allow_html=True);

# Se crean dos columnas para poner la imagen y el texto al lado:
col1, col2 = st.columns([1, 2])  # Se coloca una proporción de 1/2 para que el texto ocupe más que la imagen

# Columna 1 - Imagen:
with col1:
    st.image("images/particular_door_image.png", use_container_width = True);

# Columna 2 - Texto:
with col2:
    st.write(""" 
        ### 🚘 ¿Eres un particular y quieres vender tu coche?  

        ¡Estás en el lugar adecuado! En **Vende Tu Coche**, hemos diseñado un proceso simple y sin complicaciones para ayudarte a vender tu vehículo de manera rápida y eficiente.  
        Nuestro objetivo es que obtengas una valoración justa y transparente sin perder tiempo.  

        ### 🛠 ¿Cómo funciona?  
        1. **Introduce los datos de tu coche**: modelo, año, kilometraje, estado y otros detalles.  
        2. **Nuestro sistema calculará un precio justo** basado en múltiples factores del mercado actual.  
        3. **Recibe tu tasación al instante** y decide si deseas continuar con la venta.  

        ### 🔹 ¿Por qué elegirnos?  
        ✅ **Proceso rápido y transparente**: sin papeleo complicado ni largas esperas.  
        ✅ **Sin comisiones ocultas**: la tasación es completamente gratuita y sin compromisos.  
        ✅ **Asesoramiento personalizado**: nuestro equipo está aquí para responder cualquier duda y ayudarte en el proceso.  

        No importa el modelo ni el estado de tu coche, en nuestra plataforma encontrarás un proceso **seguro, confiable y sin complicaciones**.  

        🚀 **¡Empieza ahora y obtén tu tasación en minutos!**  
    """);

# Se añade un espacio:
st.markdown("<br>", unsafe_allow_html=True);

# Botón - Inicio Proceso de Tasación:
if st.button("Iniciar proceso de tasación"): switch_page("tasar_coche_particular_intro_page");  # Si se pulsa pasa a la siguiente página


# Botón para volver al inicio en la barra lateral:
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("main_page");

# # # # # FIN FUNCIÓN PARTICULAR # # # # #
