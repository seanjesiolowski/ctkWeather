import requests
import datetime
import json

city = 'Lowville'


def select_city(app_city):
    global city
    city = app_city


class Weather:
    def __init__(self, city):
        self.city = city
        self.current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        api_key = 'd2482af69c8e2848b4fa90c99bfd9cab'
        api_url = f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={api_key}'
        response_api = requests.get(api_url)
        print("API response status code:", response_api.status_code)
        raw_data = response_api.text

        self.parse_json = json.loads(raw_data)

    def get_list_f(self):
        # with open("weather.json", "r") as f:
        min_k = self.parse_json["main"]["temp_min"]
        curr_k = self.parse_json["main"]["temp"]
        max_k = self.parse_json["main"]["temp_max"]
        k_list = [min_k, curr_k, max_k]
        f_list = [format(((item - 273.15) * 9/5 + 32), '.2F')
                  for item in k_list]
        return f_list
