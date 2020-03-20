from seleniumbase import BaseCase

class NavigationTest(BaseCase):

    # задаем базовый урл и переменную-словарь
    def setup_class(self):
        self.base_url = "https://www.babyshop.com"
        self.menu_dict = {"Brands":['//a[@data-class="brand"]', self.base_url+"/brands/s/618"],
                     "Сlothing":['//a[@data-class="babyclothes"]', self.base_url+"/clothing/s/619"],
                     "Footwear":['//a[@data-class="babyshoes"]',self.base_url+"/footwear/s/620"]
            }
    def test_basket(self):
        # Идем на страницу товаров
        self.get(self.base_url+'/dolce-gabbana/s/1495')
        # выбор товара
        self.hover_and_click('//article[1]', '//article[1]//div[@class="quickshop-button "]')
        # выбор размера
        self.click('//div[@id="id-slct"]')
        self.click('//div[@id="id-slct"]/ul/li[2]')
        #
        
        self.click('//button[@class="add-to-cart green large"]')
        self.sleep(0.1)
        self.click('//a[@class="to-checkout white button"]')
        