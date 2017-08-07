import unittest
from appium import webdriver
import logging
from base.basetestcase import BaseTestCase
from views.agreement_handler import AgreementHandler
from views.sidebar import SideBar
from helpers.data_collection_calculator import DataCalc

class NineDayWeatherTests(BaseTestCase):
    def test_9day_forecast(self):
        agreement_handler = AgreementHandler(self.driver)
        agreement_handler.handle_agreement()
        agreement_handler.handle_update_version()

        sidebar = SideBar(self.driver)
        sidebar.open_sidebar()
        sidebar.swipe_sidebar_dowm_to_up()

        expected_forcast_dates = DataCalc.get_next_n_day_date(9)
        actual_forcast_dates = sidebar.click_nine_day_forcast().get_forecast_dates()
        self.assertListEqual(expected_forcast_dates,actual_forcast_dates)




