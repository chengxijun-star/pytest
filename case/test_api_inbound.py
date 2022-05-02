import allure
import pytest
import os

@allure.feature("WESAPI测试")
class TestInboundAPi():
    @allure.title("测试WMS下发")
    @allure.story("下发主数据")
    @allure.link("",name="")
    @pytest.mark.usefixtures("get_baseurl")
    def test_reveivedata(self,get_baseurl):
        with allure.step("调用接口下发主数据"):
            pass
        with allure.step("查询数据库"):
            pass

if __name__ == '__main__':
    pytest.main(['--alluredir', './allure'])
    os.system('allure generate ./allure -o ./report --clean')




