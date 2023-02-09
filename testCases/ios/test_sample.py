from pageObjects.ios.BasePage import BasePage
from utilities.baseUtility import BaseUtility


class TestSample(BaseUtility):

    def test_sample_ios(self):
        self.basepage = BasePage(self.driver)
        self.logData = self.getLogger()
        self.logData.info("*************** Test_001 *****************")
        self.logData.info("****Started  Sample test ****")
        self.logData.info("****Opening App****")
        assert (self.basepage.checkSampleTest() == "AIT_Mobile_Framework_Test")
