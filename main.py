import unittest
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from time import sleep


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):  # установка параметров
        self.driver = wd.Chrome()
        self.product_url = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"
        self.favorite_url = "https://www.avito.ru/favorites"

    @staticmethod
    def click_button(button):
        button.click()
        sleep(0.1)

    def test_favourite_avito(self):
        driver = self.driver
        driver.get(self.product_url)
        nonactivited_button = driver.find_element(by=By.CSS_SELECTOR,
                                                  value="button[title='Добавить в избранное'][class='desktop-usq1f1']")
        self.click_button(button=nonactivited_button)  # добавляем в избранное
        activited_button = driver.find_element(by=By.CSS_SELECTOR,
                                               value="button[title='В избранном'][class='desktop-usq1f1']")
        assert activited_button.get_attribute('data-is-favorite') == 'true'  # кнопка изменилась?
        driver.get(self.favorite_url)  # переход в раздел избранных объявлений
        product_link = driver.find_element(by=By.CSS_SELECTOR, value='a[class="css-1e7cqb"]').get_attribute('href')
        assert product_link == self.product_url  # объявление добавлено в избранное


if __name__ == "__main__":
    unittest.main()
