# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestAddtocartupdatecart():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_addtocartupdatecart(self):
        print("Membuka: https://magento.softwaretestingboard.com/ ...")
        self.driver.get("https://magento.softwaretestingboard.com/")
        self.driver.set_window_size(1296, 688)

        try:
            self.driver.find_element(
                By.CSS_SELECTOR, ".product-item:nth-child(6) .product-image-photo").click()
        except:
            print()

        try:
            self.driver.find_element(By.ID, "product-addtocart-button").click()
            print("Melakukan penambahan produk ke keranjang")
        except:
            print("Gagal menambahkan produk ke keranjang")

        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(15)
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/main/div[1]/div[2]/div/div/div/a").click()

        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[3]/div/div/label/input")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[3]/div/div/label/input")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[3]/div/div/label/input")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[3]/div/div/label/input").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[3]/div/div/label/input").send_keys("0")
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/main/div[3]/div/div[2]/form/div[2]/button[2]").click()

        time.sleep(5)
        getElement = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/main/div[3]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[4]/span/span/span")

        print("Mengupdate keranjang berhasil")

        if "$450.00" in getElement.text:
            print("✅ Subtotal produk sudah sesuai dengan kuantitas")
        else:
            print("❌ Subtotal produk tidak sesuai dengan kuantitas "+getElement.text)
