import pytest
from selenium import webdriver
import geckodriver_autoinstaller

@pytest.fixture
def dash_duo(dash_duo):
    geckodriver_autoinstaller.install()
    driver = webdriver.Firefox()
    dash_duo.driver = driver
    return dash_duo
