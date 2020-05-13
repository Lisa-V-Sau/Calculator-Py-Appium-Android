from appium import webdriver


class Driver:

    def __init__(self):

        desired_caps = {
            "deviceName": "emulator-5554",
            "platformName": "Android",
            "appPackage": "com.android.calculator2",
            "appActivity": ".Calculator",
}

        self.instance = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
