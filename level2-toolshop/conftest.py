import os
import pytest
def pytest_addoption(parser):
    parser.addoption(
        "--shop-base-url",
        action="store",
        default=os.getenv(
            "BASE_URL",
            "https://practicesoftwaretesting.com"
        ),
        help="Base URL of the Toolshop website"
    )
@pytest.fixture(scope="session")
def shop_base_url(request):
    return request.config.getoption("--shop-base-url")
