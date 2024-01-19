# Author: Colton Crowther
# GitHub username: ojo4f3
# Date: 07 APR 2023
# Description:

import re
import datetime as dt
from dateutil import parser


class Sorter:
    def __init__(self):
        self._error = "I don't understand. Please say again."
        self._request_types = [
            ["hey chuck"],
            ["search for"],
            ["joke", "tell"],
            ["news"],
            ["weather", "high", "low", "forecast"],
            ["time", "date", "until"],
            ["you", "your"],
            ["random", "story"],
        ]
        self._request_functions = {
            0: self.chat_request,
            1: self.search_request,
            2: self.joke_request,
            3: self.news_request,
            4: self.weather_request,
            5: self.time_request,
            6: self.admin_request,
            7: self.story_request,
        }

    def determine_request_type(self, input_msg):
        request = input_msg.lower()
        for index, category in enumerate(self._request_types):
            for keyword in category:
                if keyword in request:
                    search_func = self._request_functions[index]
                    response = search_func(keyword, request)
                    return response
        return self._error

    def chat_request(self, keyword, request):
        pass

    def search_request(self, keyword, request):
        pass

    def joke_request(self, keyword, request):
        pass

    def news_request(self, keyword, request):
        pass

    def weather_request(self, keyword, request):
        pass

    def time_request(self, keyword, request):
        now = dt.datetime.now()
        if keyword == 'time':
            return f"It is {now.strftime('%I %M %p')}"
        elif keyword == 'date':
            return f"Today is {now.strftime('%A, %dth %B %Y')}"
        elif keyword == 'until':
            pattern = "[adfjmnos]\w*\s\d{1,2}(st|nd|rd|th)?\s\d{4}"
            target_string = re.search(pattern, request)
            target_date = parser.parse(target_string.group(0))
            result = target_date - now
            if result.days > 365:
                years = result.days // 365
                days = result.days % 365
                return f'{target_string.group(0)} is in {years} years and {days} days'
            else:
                return f'{target_string.group(0)} is in {result.days} days'
        else:
            return self._error

    def admin_request(self, keyword, request):
        pass

    def story_request(self, keyword, request):
        pass
