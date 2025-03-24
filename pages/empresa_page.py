
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# Librería para el menú de opciones:
from streamlit_option_menu import option_menu 

# # # # #  FIN LIBRERÍAS # # # # #


# # # # #  INICIO FUNCIÓN EMPRESA # # # # #

# Configuración de la página
st.set_page_config(page_title = "🏢 Empresa 🏣", page_icon=":car:", layout="wide")


# Se aplica un color de fondo #fffafe:
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


# Título:
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 🏢 Empresa 🏣 </h1>", unsafe_allow_html = True);

# Añadir espacio con <br> (salto de línea) para un margen más grande
st.markdown("<br>", unsafe_allow_html=True);

# Crear columnas para poner la imagen y el texto al lado
col1, col2 = st.columns([1, 3])  # Proporción de espacio, la imagen en la columna más pequeña (col1) y el texto en la más grande (col2)

# Columna 1: Imagen (al margen izquierdo)
with col1:
    st.image("images/empresa_image.png", use_container_width = True)

# Columna 2: Texto
with col2:
    st.write("""
        ### 🚛 Empresas: Vende tu Flota de Vehículos de Manera Eficiente  

        Si representas a una empresa y buscas vender varios vehículos a la vez, hemos diseñado una solución ágil y efectiva para ti. 
        Sabemos que el proceso de tasación puede ser tedioso cuando se trata de gestionar una flota, por lo que hemos simplificado 
        cada paso para que puedas obtener una valoración rápida y precisa.  

        En **Vende Tu Coche**, ofrecemos una herramienta que te permite subir un archivo **.CSV** con los datos de todos los vehículos 
        que deseas vender. Nuestro sistema analizará la información y tasará cada coche de manera individual utilizando nuestro algoritmo avanzado, 
        considerando factores como el modelo, el año de fabricación, el kilometraje y el estado general del vehículo.  

        ### 🚀 ¿Cómo funciona?  
        1. **Prepara tu archivo CSV** con los datos básicos de los vehículos que deseas vender.  
        2. **Súbelo a nuestra plataforma** con un solo clic.  
        3. **Recibe la tasación**: nuestro sistema analizará cada coche y te devolverá el mismo archivo CSV con la valoración correspondiente.  

        ### 🔹 ¿Por qué elegirnos?  
        ✅ **Ahorro de tiempo**: olvídate de introducir los datos manualmente coche por coche. Con un solo archivo, puedes tasar toda tu flota.  
        ✅ **Tasaciones precisas y transparentes**: nuestra tecnología analiza cada vehículo de manera objetiva, asegurando precios justos y actualizados.  
        ✅ **Proceso automatizado y seguro**: manejamos tus datos con total confidencialidad y sin complicaciones.  

        Si tu empresa busca vender coches de manera rápida y eficiente, **nuestra plataforma es la mejor opción**. 
        Con un proceso 100% digital, sencillo y sin papeleo innecesario, te ayudamos a gestionar la venta de tu flota sin complicaciones.  

        💼 **Optimiza el proceso de venta de tus vehículos con nuestra herramienta de tasación automatizada. ¡Súbelo ahora y obtén la mejor oferta!**  
    """)

# Añadir espacio con <br> (salto de línea) para un margen más grande
st.markdown("<br>", unsafe_allow_html=True);

# Añadir un botón para iniciar el proceso de tasación
if st.button("Iniciar proceso de tasación"):
    # Este botón redirige a la página donde se iniciará el proceso de tasación
    switch_page("tasar_coche_empresa_intro_page")

# Botón para volver al inicio en la barra lateral
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("main_page");

# # # # #  FIN FUNCIÓN EMPRESA # # # # #