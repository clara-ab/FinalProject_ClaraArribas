# # # # # INICIO LIBRERÍAS # # # # #
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu  # Librería para el menú de opciones

# # # # # FIN LIBRERÍAS # # # # #

# # # # # INICIO MAIN FUNCTION # # # # #
def main():
    # Se configura la página para poder aprovechar toda la página:
    st.set_page_config(page_title="🚗 CLARA'S CAR CORNER 🚗", page_icon=":car:", layout="wide")

    # Se aplica un color de fondo deseado #fffafe:
    page_bg_color = """
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: #fffafe;
        }
        </style>
        """
    st.markdown(page_bg_color, unsafe_allow_html=True)

    # # # Barra de Navegación Superior usando streamlit-options-menu # # #
    with st.container():
        menu = option_menu(
            menu_title = None,  # No título para el menú
            options = ["Inicio", "Tasación - Particular", "Tasación - Empresa", "Sobre Nosotros", "Nuestro Método", "Contáctanos"],
            icons = ["house", "person-fill", "building", "info-circle", "clipboard-check", "phone"],
            orientation = "horizontal",  # Menú horizontal
            default_index = 0,  # Establecer "Inicio" como la opción por defecto
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
        # Si seleccionas "Inicio", se redirige a la página principal
        pass  # No hacemos nada aquí ya que ya estamos en la página principal
    elif menu == "Tasación - Particular":
        switch_page("particular_page")
    elif menu == "Tasación - Empresa":
        switch_page("empresa_page")
    elif menu == "Sobre Nosotros":
        switch_page("nosotros_page")
    elif menu == "Nuestro Método":
        st.write("En proceso...")
    elif menu == "Contáctanos":
        st.write("Contacto")

    # # # Resto de la página principal # # #
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-family: \'Droid Sans Mono\', monospace;'> 🚗 CLARA'S CAR CORNER 🚗 </h1>", unsafe_allow_html=True)
    st.image("images/portada_coches.png", use_container_width=True)
    
    # Texto introductorio para la página de la empresa
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
    """)

    st.markdown("<h3 style='text-align: center; font-family: \'Droid Sans Mono\', monospace;'>¿Eres un particular o una empresa?</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Particular"): 
                switch_page("particular_page")
        with col_b:
            if st.button("Empresa"): 
                switch_page("empresa_page")

if __name__ == "__main__":
    main()
