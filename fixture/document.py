import time
from selenium.webdriver.common.keys import Keys


class DocumentHelper:

    def __init__(self, res):
        self.res = res

    def create(self, document):
        driver = self.res.driver
        defdocs_implement_document = driver.find_element_by_xpath('//*[@class="Button Button_basic"]')
        defdocs_implement_document.click()
        deffocs_doc_name = driver.find_element_by_xpath('//*[@data-test-id="name"]')
        deffocs_doc_name.send_keys(document.name)
        deffocs_doc_number = driver.find_element_by_xpath('//*[@data-test-id="number"]')
        deffocs_doc_number.send_keys(document.number)
        deffocs_doc_date = driver.find_element_by_xpath('//*[@data-test-id="date"]')
        deffocs_doc_date.send_keys(document.date)
        time.sleep(3)
        defdocs_file_input = driver.find_element_by_xpath('//*[@type="file"]')
        defdocs_file_input.send_keys(document.file)
        time.sleep(2)
        defdocs_save_button = driver.find_element_by_xpath('//*[@type="submit"]')
        defdocs_save_button.click()
        time.sleep(2)

    def add_subsidiary(self):
        driver = self.res.driver
        defdocs_enter_add_subsidiary = driver.find_element_by_xpath('//span[contains(text(),"Добавить организацию")]')
        defdocs_enter_add_subsidiary.click()
        def_docs_add_subsidiary = driver.find_element_by_xpath('//*[@class="Icon bz-icon bz-icon-arrow-right bz-icon-24"]')
        def_docs_add_subsidiary.click()
        time.sleep(2)
        defdocs__add_subsidiary_close = driver.find_element_by_xpath('//span[contains(text(),"Закрыть")]')
        defdocs__add_subsidiary_close.click()
        time.sleep(2)

    def modify_first_implementation_name(self, name):
        driver = self.res.driver
        time.sleep(1)
        def_docs_edit_info = driver.find_element_by_xpath('//*[@class="Block-HeaderControls"]')
        def_docs_edit_info.click()
        deffocs_doc_name = driver.find_element_by_xpath('//*[@data-test-id="name"]')
        deffocs_doc_name.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        deffocs_doc_name.send_keys(name)
        defdocs_save_button = driver.find_element_by_xpath('//*[@type="submit"]')
        defdocs_save_button.click()
        time.sleep(2)





