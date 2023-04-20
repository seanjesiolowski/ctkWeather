import requests
import datetime
import json


class Weather:
    def __init__(self):
        #! update url
        api_url = r'https://api.openweathermap.org/data/2.5/weather?lat=43.895913&lon=-75.392647&appid=d2482af69c8e2848b4fa90c99bfd9cab'

        response_api = requests.get(api_url)
        print("API response status code:", response_api.status_code)

        self.current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        raw_data = response_api.text
        parse_json = json.loads(raw_data)
        filepath = 'weather.json'

        with open(filepath, 'w') as f:
            json.dump(parse_json, f)

        print("Data saved as JSON")

    def get_temp_f(self):
        with open("weather.json", "r") as f:
            temp_k = json.load(f)["main"]["temp"]
        temp_f = (temp_k - 273.15) * 9/5 + 32
        return format(temp_f, '.4f')

    def print_json(self):
        with open("weather.json", "r") as f:
            data = json.load(f)
        json_string = json.dumps(data, indent=4)
        print(f'{json_string}\n')
