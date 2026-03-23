import pytest
from dash.testing.application_runners import import_app
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Load app
@pytest.fixture
def app():
    return import_app("app")   # ✅ correct filename

# Override dash_duo fixture
@pytest.fixture
def dash_duo(dash_duo):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    dash_duo.driver = driver
    return dash_duo

# Test 1: Header exists
def test_header(dash_duo, app):
    dash_duo.start_server(app)
    header = dash_duo.find_element("#header")
    assert header is not None

# Test 2: Graph exists
def test_graph(dash_duo, app):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None

# Test 3: Radio button exists
def test_radio_button(dash_duo, app):
    dash_duo.start_server(app)
    radio_button = dash_duo.find_element("#region-filter")
    assert radio_button is not None






