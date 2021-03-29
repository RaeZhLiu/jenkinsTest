from BasePage.publicPage import BasePage
import time


class InputKey(BasePage):

    def inputKey(self, content):
        self.getUrl("https://www.baidu.com")
        self.find("id", "kw").send_keys(f'{content}')
        self.find("id", "su").click()
        time.sleep(5)
        assert f'{content}' in self.title()