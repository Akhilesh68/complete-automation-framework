from selenium import webdriver
import pytest
from test_data.home_page_test_data import HomePageTestData


""" This hook adds the marker name and description to each test's report, where applicable."""


def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Marker Name</th>")
    cells.insert(3, "<th>Marker Description</th>")


def pytest_html_results_table_row(report, cells):
    marker_name = getattr(report, "marker_name", "No marker")
    marker_description = getattr(
        report, "marker_description", "No description"
    )

    cells.insert(2, f"<td>{marker_name}</td>")
    cells.insert(3, f"<td>{marker_description}</td>")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        descriptions = {
            "smoke": "Basic application functionality",
            "sanity": "Specific functionality after a small change",
            "regression": "Existing functionality after code changes",
            "pending": "Test case marked as pending",
            "negative": "Tests with invalid inputs",
        }

        marker_names = [
            marker.name
            for marker in item.iter_markers()
            if marker.name in descriptions
        ]

        report.marker_name = ", ".join(marker_names) or "No marker"
        report.marker_description = ", ".join(
            descriptions[name] for name in marker_names
        ) or "No description"

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

@pytest.fixture(params=HomePageTestData.INVALID_FORM_TEST_DATA)  # This executes entire dicts
# @pytest.fixture(params=[HomePageTestData.INVALID_SEARCH_TEST_DATA[0]])  # This executes 1st dict only
def fetch_invalid_home_data(request):
    return request.param




