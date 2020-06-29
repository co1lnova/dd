from data.document_data import document_name_be


class NavigationHelper:

    def __init__(self, res):
        self.res = res

    def open_defdocs_service(self):
        driver = self.res.driver
        defdocs_enter_service = driver.find_element_by_xpath('//*[@class="Button Button_basic _109hten"]')
        defdocs_enter_service.click()
        driver.switch_to.frame(driver.find_element_by_id("defdocs"))

    def open_created_document(self):
        driver = self.res.driver
        def_docs_open_doc = driver.find_element_by_xpath(f'//div[contains(text(), "{document_name_be}")]')
        def_docs_open_doc.click()

    def open_parameters(self):
        driver = self.res.driver
        defdocs_open_parameters = driver.find_element_by_xpath('//div[contains(text(), "Параметры")]')
        defdocs_open_parameters.click()

    # def switch_to_default_frame(self):
    #     driver = self.res.driver
    #     driver.switchTo().defaultContent()

    def reopen_defdocs_service(self):
        driver = self.res.driver
        driver.switch_to.default_content()
        marketplace = driver.find_element_by_xpath('//span[contains(text(),"Маркетплейс")]')
        marketplace.click()
        defdocs_enter_service = driver.find_element_by_xpath('//*[@class="Button Button_basic _109hten"]')
        defdocs_enter_service.click()
        driver.switch_to.frame(driver.find_element_by_id("defdocs"))

    def open_first_document(self):
        driver = self.res.driver
        first_doc = driver.find_element_by_xpath('//*[@class="card_header sc-htpNat eBgbTM"]')
        first_doc.click()

    def implement_document(self):
        driver = self.res.driver
        implement_button = driver.find_element_by_xpath('//span[contains(text(),"Отправить на внедрение")]')
        implement_button.click()
