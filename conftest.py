import os
import pytest
from playwright.sync_api import Playwright, Browser, expect, sync_playwright


def pytest_configure(config):
    # print(dir(config))
    print("configure")


def pytest_sessionstart(session):
    # print(dir(session))
    print("sessionstart")


def pytest_sessionfinish(session):
    # print(dir(session))
    print("sessionfinish")


@pytest.fixture(scope="session", autouse=True)
def setup(request):
    print("fixture")
    request.addfinalizer(cleanup)


def cleanup():
    print("cleanup")
