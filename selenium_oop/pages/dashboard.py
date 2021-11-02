from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from .basepage import BasePage


class Dashboard(BasePage):
    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def select_top_menu_element(self, name: str) -> None:
        self._click((By.XPATH, f'//ul/li/a[text()="{name}"]'))

    def select_sub_menu_element(self, name: str) -> None:
        self._click((By.XPATH, f'//ul/li/a[text()="{name}"]'))

    def find_in_city_list(self, name: str, keys: str) -> None:
        self._send_keys((By.XPATH, f'//div/input[ @ placeholder="{name}"]'),
                        keys)

    def select_from_city_list(self, name: str) -> None:
        self._click(
            (By.XPATH, f'//div/ul/li/span[text()="{name}"]')
        )

    def select_warehouse_list(self, name: str) -> None:
        self._click(
            (By.XPATH, f'//div/input[@placeholder="{name}"]')
        )

    def find_warehouse_by_number(self, number: str) -> None:
        self._move_to_element(
            (By.XPATH, f'//div/ul/li[@data-warehouse-number="{number}"]')
        )

    def select_warehouse(self, number: str) -> None:
        self._click(
            (By.XPATH, f'//div/ul/li[@data-warehouse-number="{number}"]')
        )

    def select_office_link(self) -> None:
        return self._click(
            (By.XPATH, '//div/table/tbody/tr/td[1]/a/span')
        )

    def is_office_exist(self):
        return self.check_exists_by_xpath(
            (By.XPATH, "//div/h2/span")
        )
