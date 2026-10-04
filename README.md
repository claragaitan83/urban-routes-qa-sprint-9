# Proyecto 9: Pruebas automatizadas de Urban Routes

**Autora:** Clara Milena Gaitán Cárdenas
**Programa:** QA en TripleTen, grupo #62 (Sprint 9)

## Descripción del proyecto

Este proyecto automatiza con Python y Selenium el flujo completo de pedir un taxi en la aplicación web Urban Routes. Las pruebas cubren el escenario de una persona usuaria que:

1. Configura la dirección de origen y destino.
2. Selecciona la tarifa Comfort.
3. Agrega su número de teléfono y lo confirma con el código recibido por SMS.
4. Agrega una tarjeta de crédito.
5. Escribe un mensaje para el conductor.
6. Pide una manta y pañuelos.
7. Pide 2 helados.
8. Pide el taxi y ve el modal de búsqueda de automóvil.
9. Espera a que aparezca la información del conductor.

## Tecnologías y técnicas utilizadas

- **Python** como lenguaje de programación.
- **Selenium WebDriver** para controlar el navegador Chrome y simular las acciones de la persona usuaria.
- **Pytest** como framework para ejecutar las pruebas.
- **PyCharm** como entorno de desarrollo.
- **Git y GitHub** para el control de versiones.
- **Localizadores** de cuatro tipos: ID, XPATH, CLASS_NAME y NAME.
- **Esperas** con `time.sleep` para dar tiempo a que la página cargue.
- **Asserts** en cada prueba para verificar el resultado esperado.
- **Organización por archivos**, cada uno con una sola responsabilidad.
- **Lectura del código SMS** desde los registros de red del navegador.

## Estructura del proyecto

- `data.py`: datos de prueba (URL, direcciones, teléfono, tarjeta y mensaje).
- `locators.py`: localizadores de los elementos de la página.
- `methods.py`: métodos con las acciones y verificaciones.
- `sms.py`: función `retrieve_phone_code` que obtiene el código de confirmación.
- `main.py`: las pruebas automatizadas (de la 1 a la 9).

## Cómo ejecutar las pruebas

1. Instala las dependencias:

```
pip install selenium pytest
```

2. Abre `data.py` y actualiza `URBAN_ROUTES_URL` con el enlace vigente del servidor, porque cambia cada vez que se reinicia. Conserva `?lng=es` al final.
3. Ejecuta las pruebas desde la terminal, dentro de la carpeta del proyecto:

```
pytest main.py
```

También puedes hacer click derecho sobre `main.py` en PyCharm y elegir **Run 'pytest in main.py'**.