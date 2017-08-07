import datetime
import logging


class DataCalc():

    @staticmethod
    def remove_duplicated_items_in_list(list):
        output = []
        for i in list:
            if i not in output:
                output.append(i)
        return output


    @staticmethod
    def get_next_n_day_date(n):
        """       
        :param n: number of days
        :return: a list contains n dates as "day month"  
        """
        forcast_dates = []
        current_day = datetime.datetime.now()
        print(current_day)
        for i in range(0, n):
            current_day += datetime.timedelta(1)
            day = current_day.strftime('%d %b')
            leading_zero_moved_date = day.lstrip("0")
            forcast_dates.append(leading_zero_moved_date)

        logging.debug('Expected forcast dates: ')
        logging.debug(forcast_dates)
        return forcast_dates








