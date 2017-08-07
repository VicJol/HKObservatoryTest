from helpers.data_collection_calculator import DataCalc
import logging

class NineDayForecast():
    forecast_date_elements_xpath = \
        "//android.widget.TextView[@resource-id ='hko.MyObservatory_v1_0:id/sevenday_forecast_date']"
    forecast_dates = []

    def __init__(self, driver):
        self.driver = driver

    def get_forecast_dates(self):
        """
        Swipe the HK 9-day forcast page till the end
        :return: a list with 9 day date as "day month"
        """
        forecast_date_elements = self.driver.find_elements_by_xpath(self.forecast_date_elements_xpath)
        logging.debug('Found dates.')

        for elem in forecast_date_elements:
            date = elem.get_attribute('text')
            self.forecast_dates.append(date)

        bottom_day_text = forecast_date_elements[-1].get_attribute('text')
        logging.debug('bottom_day_text :%s'%bottom_day_text)

        to_the_end = False
        i = 0
        while(to_the_end is False):
            top_day_element_location = forecast_date_elements[0].location
            top_day_x = top_day_element_location['x']
            top_day_y = top_day_element_location['y']

            bottom_day_element_location = forecast_date_elements[-1].location
            bottom_day_x = bottom_day_element_location['x']
            bottom_day_y = bottom_day_element_location['y']


            self.driver.swipe(top_day_x, bottom_day_y, top_day_x, top_day_y)

            logging.debug("The %s time swipe"%(i+1))

            last_day_text_list = []
            forecast_date_elements = self.driver.find_elements_by_android_uiautomator\
                ('new UiSelector().resourceId("hko.MyObservatory_v1_0:id/sevenday_forecast_date")')
            for elem in forecast_date_elements:
                date = elem.get_attribute('text')
                logging.debug(date)
                self.forecast_dates.append(date)

            logging.debug("forecast_date_elements[-1].get_attribute('text') : "+
                          forecast_date_elements[-1].get_attribute('text'))

            try:
                last_day_text_list.append(forecast_date_elements[-1].get_attribute('text'))
                logging.debug("last day text list index %s"%i + " and the text is %s"%last_day_text_list[i])

                i += 1
            except IndexError as e:
                logging.debug(e)
                logging.debug("Swipe ends here")
                to_the_end = True
                logging.debug("to_the_end : %s"%to_the_end)

        removed_duplicated_list = DataCalc.remove_duplicated_items_in_list(self.forecast_dates)
        logging.debug('Actual forecast dates: ')
        logging.debug(removed_duplicated_list)
        return removed_duplicated_list