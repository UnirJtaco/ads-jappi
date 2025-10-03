import streamlit as st
import time

# Configuración de la página
st.set_page_config(
    page_title="Jappi - Sistema de Pedidos",
    page_icon="🍽️",
    layout="wide"
)

# Base de datos simulada de usuarios (en un sistema real, esto estaría en una base de datos segura)
USERS = {
    "jtaco": {
        "password": "Pucp1234",
        "nombre": "Juan",
        "apellido": "Taco",
        "telefono": "+51 999888777",
        "email": "jtaco@example.com",
        "metodo_pago": {
            "tipo": "",  # "debito" o "credito"
            "numero": "",
            "vencimiento": "",
            "cvv": ""
        }
    }
}

# Base de datos simulada de restaurantes
RESTAURANTS = {
    "La Pizzería Feliz": {
        "producto_principal": "Pizza Margherita",
        "imagen": "🍕"
    },
    "Sushi Master": {
        "producto_principal": "Roll California",
        "imagen": "🍱"
    },
    "Burger House": {
        "producto_principal": "Hamburguesa Clásica",
        "imagen": "🍔"
    },
    "Tacos México": {
        "producto_principal": "Tacos al Pastor",
        "imagen": "🌮"
    }
}

def login():
    st.title("🍽️ Bienvenido a Jappi")
    
    # Crear formulario de login
    with st.form("login_form"):
        username = st.text_input("Usuario").strip()
        password = st.text_input("Contraseña", type="password").strip()
        submit_button = st.form_submit_button("Iniciar Sesión")

    if submit_button:
        if username and password:  # Verificar que no estén vacíos
            if username in USERS and USERS[username]["password"] == password:
                st.success("Login exitoso!")
                time.sleep(1)  # Simular proceso de login
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos")
        else:
            st.warning("Por favor ingrese usuario y contraseña")
    return False

def profile_page():
    st.title("Mi Perfil")
    user_data = USERS[st.session_state.username]
    
    with st.form("profile_form"):
        nombre = st.text_input("Nombre", value=user_data["nombre"])
        apellido = st.text_input("Apellido", value=user_data["apellido"])
        telefono = st.text_input("Teléfono", value=user_data["telefono"])
        email = st.text_input("Email", value=user_data["email"])
        
        if st.form_submit_button("Guardar Cambios"):
            USERS[st.session_state.username].update({
                "nombre": nombre,
                "apellido": apellido,
                "telefono": telefono,
                "email": email
            })
            st.success("¡Perfil actualizado correctamente!")
            st.rerun()

def settings_page():
    st.title("Configuración")
    
    # Cambiar contraseña
    with st.expander("Cambiar Contraseña", expanded=False):
        with st.form("password_form"):
            current_password = st.text_input("Contraseña Actual", type="password")
            new_password = st.text_input("Nueva Contraseña", type="password")
            confirm_password = st.text_input("Confirmar Nueva Contraseña", type="password")
            
            if st.form_submit_button("Actualizar Contraseña"):
                if USERS[st.session_state.username]["password"] != current_password:
                    st.error("La contraseña actual es incorrecta")
                elif new_password != confirm_password:
                    st.error("Las nuevas contraseñas no coinciden")
                else:
                    USERS[st.session_state.username]["password"] = new_password
                    st.success("¡Contraseña actualizada correctamente!")

    # Método de pago
    with st.expander("Método de Pago", expanded=False):
        with st.form("payment_form"):
            tipo_tarjeta = st.selectbox(
                "Tipo de Tarjeta",
                options=["", "debito", "credito"],
                index=0 if not USERS[st.session_state.username]["metodo_pago"]["tipo"] else 
                      1 if USERS[st.session_state.username]["metodo_pago"]["tipo"] == "debito" else 2
            )
            numero_tarjeta = st.text_input(
                "Número de Tarjeta",
                value=USERS[st.session_state.username]["metodo_pago"]["numero"]
            )
            col1, col2 = st.columns(2)
            with col1:
                vencimiento = st.text_input(
                    "Fecha de Vencimiento (MM/YY)",
                    value=USERS[st.session_state.username]["metodo_pago"]["vencimiento"]
                )
            with col2:
                cvv = st.text_input(
                    "CVV",
                    type="password",
                    value=USERS[st.session_state.username]["metodo_pago"]["cvv"]
                )
            
            if st.form_submit_button("Guardar Método de Pago"):
                USERS[st.session_state.username]["metodo_pago"].update({
                    "tipo": tipo_tarjeta,
                    "numero": numero_tarjeta,
                    "vencimiento": vencimiento,
                    "cvv": cvv
                })
                st.success("¡Método de pago actualizado correctamente!")

    # Eliminar cuenta
    with st.expander("Eliminar Cuenta", expanded=False):
        st.warning("⚠️ Esta acción no se puede deshacer")
        with st.form("delete_account_form"):
            confirm_password = st.text_input("Ingrese su contraseña para confirmar", type="password")
            if st.form_submit_button("Eliminar mi cuenta"):
                if USERS[st.session_state.username]["password"] == confirm_password:
                    del USERS[st.session_state.username]
                    st.session_state.logged_in = False
                    st.success("Cuenta eliminada correctamente")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Contraseña incorrecta")

def show_restaurants():
    st.title("🍽️ Restaurantes Disponibles")
    # Mostrar restaurantes en una disposición de columnas
    cols = st.columns(2)
    for idx, (nombre, info) in enumerate(RESTAURANTS.items()):
        with cols[idx % 2]:
            st.subheader(f"{info['imagen']} {nombre}")
            st.write(f"**Producto destacado:** {info['producto_principal']}")
            st.button("Ver Menú", key=f"restaurant_menu_{nombre}")
            st.write("---")

def main_page():
    # Barra lateral para perfil y configuración
    with st.sidebar:
        st.title("Menú")
        if "current_page" not in st.session_state:
            st.session_state.current_page = "home"
            
        if st.button("Inicio", type="primary" if st.session_state.current_page == "home" else "secondary"):
            st.session_state.current_page = "home"
            st.rerun()
            
        if st.button("Mi Perfil", type="primary" if st.session_state.current_page == "profile" else "secondary"):
            st.session_state.current_page = "profile"
            st.rerun()
            
        if st.button("Configuración", type="primary" if st.session_state.current_page == "settings" else "secondary"):
            st.session_state.current_page = "settings"
            st.rerun()
            
        if st.button("Cerrar Sesión"):
            st.session_state.logged_in = False
            st.rerun()

    # Contenido principal según la página seleccionada
    if st.session_state.current_page == "home":
        show_restaurants()

def main():
    # Inicializar el estado de la sesión si no existe
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Mostrar página según el estado de login
    if not st.session_state.logged_in:
        login()
    else:
        main_page()
        if st.session_state.current_page == "profile":
            profile_page()
        elif st.session_state.current_page == "settings":
            settings_page()

if __name__ == "__main__":
    main()