# locators.py
from selenium.webdriver.common.by import By


class UrbanRoutesLocators:
    # 1. Configurar la dirección (Desde y Hasta)
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')

    # 2. Seleccionar la tarifa Comfort
    CALL_A_TAXI_BUTTON = (By.XPATH, '//button[text()="Pedir un taxi"]')
    COMFORT_TARIFF = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    COMFORT_TARIFF_ACTIVE = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')

    # 3. Rellenar el teléfono
    PHONE_BUTTON = (By.CLASS_NAME, 'np-text')
    PHONE_INPUT = (By.ID, 'phone')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Siguiente"]')
    CODE_INPUT = (By.ID, 'code')
    CONFIRM_CODE_BUTTON = (By.XPATH, '//button[text()="Confirmar"]')
    PHONE_VERIFY = (By.XPATH, '//div[@class="np-button filled"]/div[@class="np-text"]')

    # 4. Agregar tarjeta de crédito
    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, 'pp-button')
    ADD_CARD_BUTTON = (By.XPATH, '//div[text()="Agregar tarjeta"]')
    CARD_NUMBER_INPUT = (By.NAME, 'number')
    CARD_CODE_INPUT = (By.XPATH, '//div[@class="card-second-row"]//input[@name="code"]')
    ADD_CARD_SUBMIT_BUTTON = (By.XPATH, '//button[text()="Agregar"]')
    CARD_CHECKBOX = (By.ID, 'card-1')
    CLOSE_PAYMENT_MODAL_BUTTON = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')

    # 5. Escribir mensaje para el conductor
    COMMENT_INPUT = (By.ID, 'comment')

    # 6. Pedir una manta y pañuelos
    ORDER_REQUIREMENTS_HEADER = (By.CLASS_NAME, 'reqs-arrow')
    BLANKET_SWITCH = (By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"]/..//span[@class="slider round"]')
    BLANKET_CHECKBOX = (By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"]/..//input[@type="checkbox"]')

    # 7. Pedir 2 helados
    ICE_CREAM_PLUS_BUTTON = (By.XPATH, '//div[@class="r-counter-label" and text()="Helado"]/..//div[@class="counter-plus"]')
    ICE_CREAM_COUNTER_VALUE = (By.XPATH, '//div[@class="r-counter-label" and text()="Helado"]/..//div[@class="counter-value"]')

    # 8. Modal para buscar un taxi
    ORDER_BUTTON = (By.CLASS_NAME, 'smart-button')
    ORDER_MODAL_TITLE = (By.CLASS_NAME, 'order-header-title')

    # 9. (Opcional) Información del conductor
    ORDER_CAR_NUMBER = (By.XPATH, '//div[@class="order-number"]/div[@class="number"]')