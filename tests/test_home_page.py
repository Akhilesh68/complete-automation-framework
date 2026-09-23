from time import sleep

from pages.home_page import HomePage
import pytest
from pytest_check import check


# @pytest.mark.sanity
def test_form_submission(setup, fetch_valid_home_data):
    homepage = HomePage(setup)
    homepage.enter_name(fetch_valid_home_data['name'])
    homepage.enter_email(fetch_valid_home_data['email'])
    homepage.enter_password(fetch_valid_home_data['password'])
    homepage.click_submit_btn()
    msg = homepage.alert_msg()
    print(msg)
    # assert 'Success12' in msg # Hard assertion
    check.is_true('Success12',msg) # Soft assertion


# @pytest.mark.regression
def test_invalid_form_submission(setup, fetch_invalid_home_data):
    homepage = HomePage(setup)
    homepage.enter_name(fetch_invalid_home_data['name'])
    homepage.enter_email(fetch_invalid_home_data['email'])
    homepage.enter_password(fetch_invalid_home_data['password'])
    homepage.click_submit_btn()
    msg = homepage.alert_msg()
    print(msg)
    assert 'Success' in msg
