import pytest

from E2ETesting.helpers.commonmethods import invokebrowser
from E2ETesting.pages.AccountPage import AccountPage
from E2ETesting.pages.LoginPage import LoginPage


@pytest.fixture(scope="module")
def driver():
    driver = invokebrowser()
    loginpage = LoginPage(driver)
    loginpage.login()
    yield driver


def test_login(driver):
    #LoginPage(driver)
    title = driver.title
    # print(title)
    assert "Account" in title


def test_logout(driver):
    #LoginPage(driver)
    acountpage = AccountPage(driver)
    acountpage.logout()
    title = driver.title
    assert "Your Store" in title


def test_seachproduct(driver):
    acountpage = AccountPage(driver)
    acountpage.seachDesktopItems()
    title = driver.current_url
    assert "product" in title


# testlogin()
# testlogut()
