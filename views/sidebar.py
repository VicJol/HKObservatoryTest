from views.ninedayforecast import NineDayForecast
import logging

class SideBar():
    tree_expand_button_xpath = "//android.widget.ImageButton[@content-desc='Navigate up']"
    upper_coordinates_ui_selector = 'new UiSelector().text' \
                                    '("Press and hold the following items for adding to the bookmark")'
    down_coordinates_ui_selector = 'new UiSelector().text("Storm Track")'
    nine_day_forcast_ui_selector = 'new UiSelector().text("HK 9-Day Forecast")'

    def __init__(self ,driver):
        self.driver = driver

    def open_sidebar(self):
        sidebar_expand_button = self.driver.find_element_by_xpath(self.tree_expand_button_xpath)
        sidebar_expand_button.click()

    def swipe_sidebar_dowm_to_up(self):
        press_hold_text_element = self.driver.find_element_by_android_uiautomator(self.upper_coordinates_ui_selector)
        upper_x = self._get_coordinates(press_hold_text_element)[0]
        upper_y = self._get_coordinates((press_hold_text_element))[1]

        storm_track_element = self.driver.find_element_by_android_uiautomator(self.down_coordinates_ui_selector)
        down_x = self._get_coordinates(storm_track_element)[0]
        down_y = self._get_coordinates(storm_track_element)[1]

        self.driver.swipe(upper_x, down_y, upper_x, upper_y)

    def _get_coordinates(self,element):
        x_y_coordinates = []
        element_location = element.location
        x_y_coordinates.append(element_location['x'])
        x_y_coordinates.append(element_location['y'])
        return x_y_coordinates

    def click_nine_day_forcast(self):
        nine_day_forcast_element = self.driver.find_element_by_android_uiautomator(self.nine_day_forcast_ui_selector)
        text = nine_day_forcast_element.text
        logging.debug("now click this element: %s"%text)
        nine_day_forcast_element.click()
        return NineDayForecast(self.driver)