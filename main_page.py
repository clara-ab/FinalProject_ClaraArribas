
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para poder utilizar Streamlit:
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# Librería para utilizar el menú de opciones (barra de navegación):
from streamlit_option_menu import option_menu  

# # # # # FIN LIBRERÍAS # # # # #



# # # # # INICIO MAIN FUNCTION # # # # #

def main():
    # Configuración de la página:
    st.set_page_config(page_title = "🚗 CLARA'S CAR CORNER 🚗", page_icon = ":car:", layout = "wide")

    # Se aplica un color de fondo deseado #fffafe:
    page_bg_color = """
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: #fffafe;
        }
        </style>
        """
    st.markdown(page_bg_color, unsafe_allow_html = True);

    # Espacio:
    st.markdown("<br>", unsafe_allow_html = True);


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

            # Se establece visualmente que se está en la pantalla de 'Inicio' [index = 0]
            default_index = 0,

            # Se define el estilo de la barra de navegación:
            styles = {
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
        pass  # main_page es el Inicio por lo que no se hace nada si hacen click
    elif menu == "Tasación - Particular":
        switch_page("particular_page");
    elif menu == "Tasación - Empresa":
        switch_page("empresa_page");
    elif menu == "Sobre Nosotros":
        switch_page("nosotros_page");
    elif menu == "Nuestro Método":
        switch_page("metodo_page");
    elif menu == "Contáctanos":
        switch_page("contacto_page");


    # Espacio 🚗 CLARA'S CAR CORNER 🚗:
    st.markdown("<br>", unsafe_allow_html = True);

    # Título:
    st.markdown("<h1 style='text-align: center; font-family: \'Droid Sans Mono\', monospace;'> 🚗 CLARA'S CAR CORNER 🚗 </h1>", unsafe_allow_html = True);

    # Espacio:
    st.markdown("<br>", unsafe_allow_html = True);

    # Imagen:
    st.image("images/portada_coches.png", use_container_width = True);
    
    # Texto introductorio para la página de la empresa:
    st.markdown("""
        # ¡Bienvenido a **Clara's Car Corner**! 🚗✨

        **¿Estás buscando vender tu coche usado?**  
        ¡Estás en el lugar adecuado! En **Clara's Car Corner**, nos especializamos en ofrecer un proceso de venta de coches de segunda mano **transparente**, **rápido** y **sin complicaciones**. 💨

        ## ¿Por qué elegirnos? 🤔
        ### 1. **Tasación justa 💸**
        Utilizamos un algoritmo avanzado para ofrecerte una **estimación precisa** del valor de tu coche.

        ### 2. **Proceso sencillo 📝**
        Olvídate de trámites complicados.

        ### 3. **Asesoramiento personalizado 💬**
        Si tienes alguna duda, **nuestro equipo de expertos está disponible** para ayudarte.

        ---
        ¡Descubre todo lo que **Clara's Car Corner** tiene para ofrecerte! 🌟
    """);

if __name__ == "__main__":
    main()
