from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def add_to_basket(self):
		assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button is not presented"
		button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
		button.click()

	def should_be_book_name(self):
		book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
		book_name_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET).text
		assert book_name == book_name_basket, "Name is not the same"

	def should_be_basket_price(self):
		book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
		basket_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_BASKET).text
		assert book_price == basket_price, "Price is not the same"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

	def should_disappeared(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented, but should be"

