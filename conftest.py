import pytest
from calculator import Calculator

# pytest 编码格式
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')


@pytest.fixture()
def calculate():
    cal = Calculator()
    print("开始计算")
    yield cal
    print("结束计算")