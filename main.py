# main.py
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import (
    URBAN_ROUTES_URL,
    ADDRESS_FROM,
    ADDRESS_TO,
    PHONE_NUMBER,
    CARD_NUMBER,
    CARD_CODE,
    MESSAGE_FOR_DRIVER
)
from methods import UrbanRoutesMethods
from sms import retrieve_phone_code


class TestUrbanRoutes:
    driver = None
    methods = None

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get(URBAN_ROUTES_URL)
        time.sleep(3)
        cls.methods = UrbanRoutesMethods(cls.driver)

    def test_1_set_address(self):
        self.methods.set_address(ADDRESS_FROM, ADDRESS_TO)
        assert self.methods.get_from() == ADDRESS_FROM
        assert self.methods.get_to() == ADDRESS_TO

    def test_2_select_comfort_tariff(self):
        self.methods.select_comfort_tariff()
        assert self.methods.get_comfort_tariff_active() == 'Comfort'

    def test_3_set_phone_number(self):
        # 1. Ingresamos el número y damos Siguiente (aquí se dispara el SMS)
        self.methods.enter_phone_number(PHONE_NUMBER)
        # 2. Recuperamos el código SMS que ya se envió
        code = retrieve_phone_code(self.driver)
        # 3. Escribimos el código y confirmamos
        self.methods.confirm_phone_code(code)
        assert self.methods.get_phone_number() == PHONE_NUMBER

    def test_4_add_credit_card(self):
        self.methods.set_credit_card(CARD_NUMBER, CARD_CODE)
        assert self.methods.get_card_checked()
        self.methods.close_payment_modal()

    def test_5_write_comment_for_driver(self):
        self.methods.set_message_for_driver(MESSAGE_FOR_DRIVER)
        assert self.methods.get_message_for_driver() == MESSAGE_FOR_DRIVER

    def test_6_select_blanket(self):
        self.methods.select_blanket()
        assert self.methods.get_blanket_value()

    def test_7_add_two_ice_creams(self):
        self.methods.add_two_ice_creams()
        assert self.methods.get_ice_cream_count() == '2'

    def test_8_click_order_button(self):
        self.methods.click_order_button()
        assert self.methods.get_order_modal_title() == 'Buscar automóvil'

    def test_9_driver_info(self):
        self.methods.wait_for_driver_info()
        assert 'El conductor llegará' in self.methods.get_order_modal_title()
        assert self.methods.get_order_car_number()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()