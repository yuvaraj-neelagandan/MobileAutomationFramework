from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    sample_text_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TextView"

    def __init__(self, driver):
        self.driver = driver

    def checkSampleTest(self):
        return self.driver.find_element(AppiumBy.XPATH, self.sample_text_xpath).text


