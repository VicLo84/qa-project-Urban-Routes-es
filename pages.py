from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    #  Configurar dirección
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    #  Seleccionar tarifa "Comfort"
    call_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_fee = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')
    comfort_title = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
    #  Rellenar número de teléfono
    phone_number_button = (By.CLASS_NAME, 'np-text')
    phone_number_field = (By.ID, 'phone')
    phone_next_button = (By.XPATH, '//*/div[1]/form/div[2]/button')
    code_number_field = (By.XPATH, '//div[2]/form/div[1]/div[1]/input')
    confirmation_button = (By.XPATH, '//div[2]/form/div[2]/button[1]')
    #  Agregar tarjeta de crédito
    payment_method_title = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]')
    payment_method_button = (By.CLASS_NAME, 'pp-text')
    add_card_plus_button = (By.CLASS_NAME, 'pp-plus')
    card_number_field = (By.ID, 'number')
    cvv_field = (By.XPATH, '//div[2]/div[2]/input')
    no_interactable_space = (By.CLASS_NAME, 'card-wrapper')
    add_card_button = (By.XPATH, '//form/div[3]/button[1]')
    close_add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    #  Escribir mensaje para conductor
    drivers_message_field = (By.ID, 'comment')
    #  Pedir manta y pañuelos
    blanket_and_tissues_slider = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div')
    #  Pedir helado
    chocolate_plus_counter = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]')
    choco_ice_cream_counter = (By.XPATH, '//div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]')
    #  Cambio modal de botón
    find_taxi_button = (By.CSS_SELECTOR, '.smart-button-main')


    def __init__(self, driver):
        self.driver = driver

    """Funciones Prueba 01"""
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
    """Funciones Prueba 02"""
    def click_call_taxi_button(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def select_comfort_fee(self):
        self.driver.find_element(*self.comfort_fee).click()

    def get_comfort_title(self):
        return self.driver.find_element(*self.comfort_title).text
    """Funciones Prueba 03"""
    def click_phone_number_button(self):
        self.driver.find_element(*self.phone_number_button).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def click_next_phone_button(self):
        self.driver.find_element(*self.phone_next_button).click()

    def set_phone_code(self, code):
        self.driver.find_element(*self.code_number_field).send_keys(code)

    def click_confirmation_button(self):
        self.driver.find_element(*self.confirmation_button).click()
    """Funciones Prueba 04"""
    def return_payment_method_text(self):
        return self.driver.find_element(*self.payment_method_title).text

    def click_payment_method_button(self):
        self.driver.find_element(*self.payment_method_button).click()

    def click_add_plus_button(self):
        self.driver.find_element(*self.add_card_plus_button).click()

    def set_card_number(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def set_card_code(self, code):
        self.driver.find_element(*self.cvv_field).send_keys(code)

    def click_no_interactable_space(self):
        self.driver.find_element(*self.no_interactable_space).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    def click_close_add_card_button(self):
        self.driver.find_element(*self.close_add_card_button).click()
    """Funciones Prueba 05"""
    def set_drivers_message(self, message_for_driver):
        self.driver.find_element(*self.drivers_message_field).send_keys(message_for_driver)
    """Funciones Prueba 06"""
    def click_blanket_and_tissues_slider(self):
        self.driver.find_element(*self.blanket_and_tissues_slider).click()
    """Funciones Prueba 07"""
    def double_click_ice_cream(self):
        self.driver.find_element(*self.chocolate_plus_counter).click()
        self.driver.find_element(*self.chocolate_plus_counter).click()
    def get_ice_cream_count(self):
        return self.driver.find_element(*self.choco_ice_cream_counter).text
    """Funciones Prueba 08"""
    def get_button_text_change(self):
        return self.driver.find_element(*self.find_taxi_button).text