from selenium import webdriver
import pytest
from test_data.home_page_test_data import HomePageTestData


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    yield driver
    driver.quit()


@pytest.fixture(params=HomePageTestData.VALID_FORM_TEST_DATA)  # This executes entire dicts
# @pytest.fixture(params=[HomePageTestData.VALID_SEARCH_TEST_DATA[0]])  # This executes 1st dict only
def fetch_valid_home_data(request):
    return request.param


# request.param will receive each dictionary one by one:

@pytest.fixture(params=HomePageTestData.INVALID_FORM_TEST_DATA) # This executes entire dicts
# @pytest.fixture(params=[HomePageTestData.INVALID_SEARCH_TEST_DATA[0]])  # This executes 1st dict only
def fetch_invalid_home_data(request):
    return request.param
