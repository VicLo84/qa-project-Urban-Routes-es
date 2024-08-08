
import data
import helpers
import pages
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_01_set_route(self):
        self.driver.get(data.urban_routes_url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 5)
        #  Espera a que aparezcan ambos campos
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dst-picker')))
        routes_page = pages.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.button.round')))
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_02_select_comfort_fee(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_call_taxi_button()
        wait = WebDriverWait(self.driver, 5)
        #  Espera a que aparezca el botón de reservación
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'smart-button')))
        routes_page.select_comfort_fee()
        assert routes_page.get_comfort_title() == "Comfort"

    def test_03_fill_phone_number(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_phone_number_button()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(routes_page.phone_number_button))
        phone_number = data.phone_number
        routes_page.set_phone_number(phone_number)
        routes_page.click_next_phone_button()
        code = helpers.retrieve_phone_code(driver=self.driver)
        routes_page.set_phone_code(code)
        routes_page.click_confirmation_button()

    def test_04_add_credit_card(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_payment_method_button()
        assert routes_page.return_payment_method_text() == 'Método de pago'
        routes_page.click_add_plus_button()
        card_number = data.card_number
        code = data.card_code
        routes_page.set_card_number(card_number)
        routes_page.set_card_code(code)
        routes_page.click_no_interactable_space()
        routes_page.click_add_card_button()
        routes_page.click_close_add_card_button()

    def test_05_write_driver_a_message(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        routes_page.set_drivers_message(message_for_driver)

    def test_06_request_blanket_and_tissues(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_blanket_and_tissues_slider()

    def test_07_order_two_ice_creams(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.double_click_ice_cream()
        two_ice_creams_count = routes_page.get_ice_cream_count()
        assert '2' in two_ice_creams_count

    def test_08_call_taxi_modal_change(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        button_text_change = routes_page.get_button_text_change()
        assert 'Pedir un taxi' in button_text_change

    @classmethod
    def teardown_class(cls):
        time.sleep(3)
        cls.driver.quit()
