import time
from selenium.webdriver.common.action_chains import ActionChains

class SessionHelper:

    def __init__(self, res):
        self.res = res

    def login(self, username, password):
        driver = self.res.driver
        action = ActionChains(driver)
        self.res.open_auth_page()
        auth_login = driver.find_element_by_xpath('//*[@data-test-id="authpage-login"]')
        auth_login.send_keys(username)
        auth_password = driver.find_element_by_xpath('//*[@data-test-id="authpage-password"]')
        auth_password.send_keys(password)
        # time.sleep(1)
        auth_submit_button = driver.find_element_by_xpath('//*[@data-test-id="authpage-submit"]')
        action.move_to_element(auth_submit_button).click().perform()
        # auth_submit_button.click()

    def logout(self):
        driver = self.res.driver
        driver.switch_to.default_content()
        profile_menu = driver.find_element_by_xpath('//*[@class="Icon bz-icon bz-icon-profile bz-icon-24"]')
        profile_menu.click()
        time.sleep(1)
        logout_button = driver.find_element_by_xpath('//span[contains(text(),"Выйти")]')
        logout_button.click()
