import configparser
import os

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


class BasePage(object):
    _driver: WebDriver

    # 读取配置文件
    @staticmethod
    def getConfig():
        config = configparser.ConfigParser()
        config.read(os.path.join(os.getcwd(), '../', 'iselenium.ini'))
        return config

    def setup(self):
        config = self.getConfig()
        print("获取配置文件section:", config.sections())

        # 控制是否采用无界面形式运行自动化测试
        try:
            # using_headless = os.environ['using_headless']
            using_headless = config.get('env', 'using_headless')
            print("是否使用无界面：", using_headless)
        except KeyError:
            using_headless = None
            print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')

        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('使用无界面方式运行')
            chrome_options.add_argument("--headless")

        self._driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'), options=chrome_options)
        self._driver.maximize_window()
        self._driver.implicitly_wait(5)

    def teardown(self):
        self._driver.quit()

    def getUrl(self, url=None):
        self._driver.get(url)

    def find(self, by, value):
        return self._driver.find_element(by, value)

    def title(self):
        return self._driver.title