from urllib import request
import allure
import pytest


class Test_adb():
    def test_3(self):
        print('\n333333333')

    @allure.step("第一步：测试test4")
    @pytest.mark.parametrize(argnames="data_test",argvalues=[(1,2,3),(4,5)],indirect=False,ids=None,scope=None)
    def test_4(self,data_test):
        print(data_test)
        print('\n4444444444')


    @allure.step("第一步：测试test5")
    def test_5(self):
        print('\n5555555555')

if __name__=='__main__':
    pytest.main("test_12.py")