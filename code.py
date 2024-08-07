
def test_03_fill_phone_number(self):
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.click_button_phone_number()
    phone_number = data.phone_number
    routes_page.set_phone(phone_number)
    routes_page.click_button_next()
    code = retrieve_phone_code(driver=self.driver)
    assert code
    routes_page.set_code(code)
    routes_page.click_confirm_button()
    # Agregamos un tiempo de espera para asegurarte de que el número de teléfono se confirme
    WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(routes_page.confirmed_phone_field, phone_number))
    confirmed_phone_number = routes_page.get_confirmed_phone_number()
    assert phone_number in confirmed_phone_number, f"Número de teléfono incorrecto: {confirmed_phone_number}"
    # confirmamos si el numero de telefono que se ingreso, se encuentra ingresado en el campo confirmed_phone_number o localizador np-button arriba de np-text