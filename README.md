# Jappi - Sistema de Pedidos de Comida

Esta es una aplicación de prototipo para un sistema de pedidos de comida desarrollada con Streamlit.

## Requisitos Previos

1. **Miniconda**
   - Descarga Miniconda desde [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
   - Selecciona la versión correspondiente a tu sistema operativo
   - Ejecuta el instalador y sigue las instrucciones

## Configuración del Ambiente

1. **Crear el ambiente virtual con Miniconda**
   ```powershell
   # Crear un nuevo ambiente con Python 3.9
   conda create -n jappi_env python=3.9

   # Activar el ambiente
   conda activate jappi_env
   ```

2. **Instalar las dependencias**
   ```powershell
   # Instalar Streamlit
   pip install streamlit
   ```

## Ejecutar la Aplicación

1. **Activar el ambiente virtual** (si no está activado)
   ```powershell
   conda activate jappi_env
   ```

2. **Ejecutar la aplicación**
   ```powershell
   streamlit run app.py
   ```

3. **Acceder a la aplicación**
   - La aplicación se abrirá automáticamente en tu navegador predeterminado
   - Si no se abre automáticamente, puedes acceder a través de: http://localhost:8501

## Credenciales de Prueba

Para probar la aplicación, puedes usar las siguientes credenciales:
- **Usuario:** jtaco
- **Contraseña:** Pucp1234

## Funcionalidades

- **Login/Logout:** Sistema de autenticación de usuarios
- **Perfil de Usuario:** Ver y editar información personal
- **Configuración:**
  - Cambiar contraseña
  - Gestionar métodos de pago
  - Eliminar cuenta
- **Restaurantes:** Ver lista de restaurantes disponibles y sus productos destacados

## Estructura del Proyecto

```
jappi_app/
│
├── app.py          # Aplicación principal
└── README.md       # Documentación
```

## Notas Importantes

- Esta es una versión de prototipo con datos simulados
- Los cambios en los datos se mantienen solo durante la sesión actual
- Para un ambiente de producción, se recomienda implementar una base de datos persistente

## Solución de Problemas

1. **Error al activar el ambiente conda**
   ```powershell
   # Si recibes el error "conda is not recognized as a command"
   # Cierra y vuelve a abrir tu terminal después de instalar Miniconda
   ```

2. **Error al ejecutar streamlit**
   ```powershell
   # Verifica que el ambiente está activado
   conda env list
   
   # Reinstala streamlit si es necesario
   pip install --upgrade streamlit
   ```
