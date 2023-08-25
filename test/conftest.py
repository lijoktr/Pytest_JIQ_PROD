import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager


driver = None
chromedriver_path = "C:/Users/lijom/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")

options = webdriver.EdgeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "edge":
        driver = webdriver.Edge(options=options)
    driver.get("https://careerswales.gov.wales/job-ideas-quiz")

    driver.maximize_window()
    request.cls.driver = driver  # instead of return driver
    yield
    driver.close()  # executing last


"""

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):

        #Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        #:param item:

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

"""