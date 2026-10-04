# methods.py
import time
from locators import UrbanRoutesLocators


class UrbanRoutesMethods:
    def __init__(self, driver):
        self.driver = driver
        self.locators = UrbanRoutesLocators

    # 1. Configurar las direcciones (Desde y Hasta)
    def set_address(self, address_from, address_to):
        time.sleep(3)
        from_field = self.driver.find_element(*self.locators.FROM_FIELD)
        from_field.clear()
        from_field.send_keys(address_from)
        time.sleep(2)

        to_field = self.driver.find_element(*self.locators.TO_FIELD)
        to_field.clear()
        to_field.send_keys(address_to)
        time.sleep(3)

    def get_from(self):
        return self.driver.find_element(*self.locators.FROM_FIELD).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.TO_FIELD).get_property('value')

    # 2. Seleccionar la tarifa Comfort
    def select_comfort_tariff(self):
        time.sleep(3)
        self.driver.find_element(*self.locators.CALL_A_TAXI_BUTTON).click()
        time.sleep(3)
        self.driver.find_element(*self.locators.COMFORT_TARIFF).click()
        time.sleep(3)

    def get_comfort_tariff_active(self):
        return self.driver.find_element(*self.locators.COMFORT_TARIFF_ACTIVE).text

    # 3. Parte A: Ingresar número de teléfono y dar clic en Siguiente
    def enter_phone_number(self, phone_number):
        time.sleep(3)
        self.driver.find_element(*self.locators.PHONE_BUTTON).click()
        time.sleep(3)

        phone_input = self.driver.find_element(*self.locators.PHONE_INPUT)
        phone_input.send_keys(phone_number)
        time.sleep(2)

        self.driver.find_element(*self.locators.NEXT_BUTTON).click()
        time.sleep(3)

    # 3. Parte B: Ingresar el código SMS y confirmar
    def confirm_phone_code(self, code):
        time.sleep(3)
        code_input = self.driver.find_element(*self.locators.CODE_INPUT)
        code_input.send_keys(code)
        time.sleep(2)
        self.driver.find_element(*self.locators.CONFIRM_CODE_BUTTON).click()
        time.sleep(3)

    def get_phone_number(self):
        return self.driver.find_element(*self.locators.PHONE_VERIFY).text

    # 4. Agregar tarjeta de crédito
    def set_credit_card(self, card_number, card_code):
        time.sleep(3)
        self.driver.find_element(*self.locators.PAYMENT_METHOD_BUTTON).click()
        time.sleep(3)
        self.driver.find_element(*self.locators.ADD_CARD_BUTTON).click()
        time.sleep(3)

        self.driver.find_element(*self.locators.CARD_NUMBER_INPUT).send_keys(card_number)
        time.sleep(2)

        card_code_input = self.driver.find_element(*self.locators.CARD_CODE_INPUT)
        card_code_input.send_keys(card_code)
        time.sleep(2)
        card_code_input.send_keys(u'\ue004')  # Tecla TAB para perder el foco del CVV
        time.sleep(2)

        self.driver.find_element(*self.locators.ADD_CARD_SUBMIT_BUTTON).click()
        time.sleep(3)

    def get_card_checked(self):
        return self.driver.find_element(*self.locators.CARD_CHECKBOX).is_selected()

    def close_payment_modal(self):
        self.driver.find_element(*self.locators.CLOSE_PAYMENT_MODAL_BUTTON).click()
        time.sleep(3)

    # 5. Escribir mensaje para el conductor
    def set_message_for_driver(self, message):
        time.sleep(3)
        self.driver.find_element(*self.locators.COMMENT_INPUT).send_keys(message)
        time.sleep(3)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.locators.COMMENT_INPUT).get_property('value')

    # 6. Pedir una manta y pañuelos
    def open_order_requirements(self):
        time.sleep(3)
        self.driver.find_element(*self.locators.ORDER_REQUIREMENTS_HEADER).click()
        time.sleep(2)

    def select_blanket(self):
        time.sleep(3)
        blanket = self.driver.find_element(*self.locators.BLANKET_SWITCH)
        self.driver.execute_script("arguments[0].scrollIntoView();", blanket)
        time.sleep(2)
        blanket.click()
        time.sleep(2)

    def get_blanket_value(self):
        return self.driver.find_element(*self.locators.BLANKET_CHECKBOX).is_selected()

    # 7. Pedir 2 helados
    def add_two_ice_creams(self):
        time.sleep(3)
        ice_cream_plus = self.driver.find_element(*self.locators.ICE_CREAM_PLUS_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", ice_cream_plus)
        time.sleep(2)
        ice_cream_plus.click()
        time.sleep(1)
        ice_cream_plus.click()
        time.sleep(3)

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.locators.ICE_CREAM_COUNTER_VALUE).text

    # 8. Modal para buscar un taxi
    def click_order_button(self):
        time.sleep(3)
        self.driver.find_element(*self.locators.ORDER_BUTTON).click()
        time.sleep(5)

    def get_order_modal_title(self):
        return self.driver.find_element(*self.locators.ORDER_MODAL_TITLE).text

    # 9. (Opcional) Información del conductor
    def wait_for_driver_info(self):
        time.sleep(45)

    def get_order_car_number(self):
        return self.driver.find_element(*self.locators.ORDER_CAR_NUMBER).text