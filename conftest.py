import os
import pytest
from playwright.sync_api import Playwright, Browser, expect, sync_playwright


def pytest_configure(config):
    print(config)


def pytest_sessionstart(session):
    print(session)


@pytest.fixture(scope="session", autouse=True)
def setup(request):
    print("setup test")
    request.addfinalizer(cleanup)


def cleanup():
    print("completed all tests")
