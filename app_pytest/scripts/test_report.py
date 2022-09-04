import os
import pytest
import allure

class Test_report:
    @pytest.mark.run(order=3)
    def test_12(self):
        print('121212')

    @pytest.mark.run(order=1)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_34(self):
            print('343434')
            allure.attach("错误信息：","test34断言失败")
            assert 1>2

    @pytest.mark.run(order=2)
    def test_45(self):
        print('454545')

if __name__=='__main__':
    pytest.main('pytest_report.py')
    rep_path=os.getcwd()
    print(rep_path)
    with open(rep_path+'/click.bat','w') as f:
        f.write("allure server report")
