import pytest

#类名一定要Test_开头，并且T要大写，不然执行不了
class Test_abd():
    # #类级别的使用：setup和teardown只执行一次
    def setup_class(self):
        print('\n=====setup======')
    def teardown_class(self):
        print('=====teardown===')
    def test_a(self):
        print('\ntesta 11111111111')
        assert 1

    def test_b(self):
        print('\ntestb ttttttttt')
        assert 1

