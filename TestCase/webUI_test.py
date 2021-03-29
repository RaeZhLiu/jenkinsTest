"""
测试百度网首页搜索关键词之后，跳转页面标题的正确性
1. 搜索"今日头条"，验证正确性
2. 搜索"王者荣耀"，验证正确性
"""
from BasePage.inputkey import InputKey
import pytest


class TestSearch(InputKey):
    def test_u1(self):
        """
        测试用例1，验证'今日头条'关键词在百度上的搜索结果
        """
        self.inputKey("今日头条")

    def test_u2(self):
        """
        测试用例2， 验证'王者荣耀'关键词在百度上的搜索结果
        """
        self.inputKey("王者荣耀")
