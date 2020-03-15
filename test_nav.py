from seleniumbase import BaseCase
from selenium.webdriver.common.by import By

class NavigationTest(BaseCase):

    # задаем базовый урл и переменную-словарь
    def setup_class(self):
        self.base_url = "https://www.babyshop.com"
        self.menu_dict = {"Brands":['//a[@data-class="brand"]', self.base_url+"/brands/s/618"],
                     "Сlothing":['//a[@data-class="babyclothes"]', self.base_url+"/clothing/s/619"],
                     "Footwear":['//a[@data-class="babyshoes"]',self.base_url+"/footwear/s/620"]
            }
    # проверяем пункты меню
    def test_menu(self):
        self.get(self.base_url)
        for item in self.menu_dict:
            print(f"Меню {item}")
            self.click(self.menu_dict[item][0])
            # получаем текущий урл в переменную curr_url
            curr_url = self.get_current_url()
            # проверка соответствия полученного и ожидаемого урл
            self.assert_equal(curr_url, self.menu_dict[item][1])

    def test_sub_menu(self):
        self.get(self.base_url)
        self.hover_and_click('a[data-class="babyshoes"]', '//div[@class="babyshoes mid-navigation-container"]/div[@class="content c-16"]/div[@class="c-8"]/ul[2]/li[1]/a')