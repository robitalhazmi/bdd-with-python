from selenium.webdriver.common.by import By
from browser import Browser

class SearchPageLocator(object):
    # Search Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")
    SEARCH_FIELD = (By.ID, "search-home-input")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[class*=submit]")


class SearchPage(Browser):
    # Search Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term):
        self.fill(search_term, *SearchPageLocator.SEARCH_FIELD)
        self.click_element(*SearchPageLocator.SUBMIT_BUTTON)
