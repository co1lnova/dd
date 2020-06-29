

class AssertHelper:

    def __init__(self, res):
        self.res = res

    def get_first_document_name(self):
        driver = self.res.driver
        first_doc_name = driver.find_element_by_xpath('//*[@class="card_header sc-htpNat eBgbTM"]').text
        doc_name = first_doc_name[0:11]
        return doc_name

    def get_dzo1(self):
        driver = self.res.driver
        dzo1 = driver.find_element_by_xpath('//a[contains(text(),"sb_docs_DZO1")]').text
        return dzo1

    def get_implementation_status(self):
        driver = self.res.driver
        implementation_status = driver.find_element_by_xpath('//*[@class="badge undefined sc-bxivhb fJJMlw"]').text
        return implementation_status

    def get_marketplace_button_text(self):
        driver = self.res.driver
        marketplace = driver.find_element_by_xpath('//span[contains(text(),"Маркетплейс")]')
        return marketplace



