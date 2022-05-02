
import pytest
import os

path = os.path.dirname(os.path.realpath(__file__))



@pytest.fixture(scope="session")
def get_baseurl():
    pass

@pytest.fixture(scope="session")
def login_wms():
   pass

