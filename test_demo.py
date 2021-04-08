import pytest
import yaml
import allure

def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    return datas

@allure.feature("测试计算器")
class TestCal:

    @pytest.mark.parametrize('a,b,expect', get_datas()['add_int']['datas'], ids=get_datas()['add_int']['ids'])
    @allure.story("测试相加功能_int")
    def test_add_int(self, calculate, a, b, expect):
        assert expect == calculate.add(a, b)

    @pytest.mark.parametrize('a,b,expect', get_datas()['add_float']['datas'], ids=get_datas()['add_float']['ids'])
    @allure.story("测试相加功能_float")
    def test_add_float(self, calculate, a, b, expect):
        assert expect == round(calculate.add(a, b), 2)

    @pytest.mark.parametrize('a,b,expect', get_datas()['div_int']['datas'], ids=get_datas()['div_int']['ids'])
    @allure.story("测试相除功能_int")
    def test_div_int(self, calculate, a, b, expect):
        try:
            calculate.div(a, b)
        except Exception as f:
            print(f)

    @pytest.mark.parametrize('a, b, expect',get_datas()['div_float']['datas'], ids=get_datas()['div_float']['ids'])
    @allure.story("测试相除功能_float")
    def test_div_float(self, calculate, a, b, expect):
        assert expect == round(calculate.div(a, b), 2)
