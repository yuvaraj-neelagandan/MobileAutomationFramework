import pytest
from appium import webdriver
from utilities.settings import *

driver = None


@pytest.fixture()
def setup(request):
    global driver
    capabilities = {
        'platformName': (CONFIG[platform]['platformName']),
        'platformVersion': (CONFIG[platform]['platformVersion']),
        'deviceName': (CONFIG[platform]['deviceName']),
        'automationName': (CONFIG[platform]['automationName']),
        'appPackage': (CONFIG[platform]['appPackage']),
        'appActivity': (CONFIG[platform]['appActivity']),
        'noReset': (CONFIG[platform]['noReset']),
        'app': (CONFIG[platform]['folder']),
    }
    url = 'http://localhost:4723/wd/hub'
    request.instance.driver = webdriver.Remote(url, capabilities)
    driver = request.instance.driver

    def teardown():
        request.instance.driver.quit()

    request.addfinalizer(teardown)


@pytest.fixture(scope="session")
def app(request):
    return request.config.getoption("--app")


@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshots in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            tc_name = report.nodeid.split("::")[-1]
            file_name = BaseUtility.ROOT_PATH + "/reports/screenshots/" + tc_name + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="screenshots/%s.png" alt="screenshots" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % tc_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    if driver is not None:
        driver.save_screenshot(name)


def pytest_configure(config):
    config._metadata['Project Name'] = 'AIT_Test_Project'
    config._metadata['Module Name'] = 'Test'
    config._metadata['Tester'] = 'Yuvaraj Neelagandan'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
