import requests
import kivy
kivy.require('1.9.2')

from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Label

api_key = 'get from wunderground.com'

class WU_GridLayout(BoxLayout):
    location = StringProperty("")
    icon_url = StringProperty("")
    condition = StringProperty("")
    temp_string = StringProperty("")
    wind_string = StringProperty("")
    pressure = StringProperty("Pressure:\n  0")
    visibility = StringProperty("Visibility:\n  0")
    clouds = StringProperty("Clouds:\n  0")
    dew_point = StringProperty("Dew Point:\n  0")
    humidity = StringProperty("Humidity:\n  0")
    rainfall = StringProperty("Rainfall:\n  0")
    wu_icon =  StringProperty("")
    
    ob_time = StringProperty("")
    station_id = StringProperty("")
    
    def get_wu_data(self):
        r = requests.get('http://api.wunderground.com/api/' + api_key + '/conditions/q/AK/Eagle_River.json')
        data = r.json()
        return data.get("current_observation")
    
    def update(self): 
        json_data = self.get_wu_data()
        
        self.location = json_data.get("display_location").get("city") + ",\n" + json_data.get("display_location").get("state_name")
        self.icon_url = json_data.get("icon_url")
        self.temp_string = json_data.get("temperature_string")
        self.condition = json_data.get("weather")
        self.wind_string = json_data.get("wind_string")
        
        self.pressure = "Pressure:\n  " + json_data.get("pressure_in")
        self.visibility = "Visibility:\n  " + json_data.get("visibility_mi")
        self.clouds = "Clouds:\n  " + json_data.get("weather")
        self.dew_point = "Dew Point:\n  " + json_data.get("dewpoint_string")
        self.humidity = "Humidity:\n  " + json_data.get("relative_humidity")
        self.rainfall = "Rainfall:\n  " + json_data.get("precip_today_string")
        
        self.ob_time = json_data.get("observation_time")
        self.station_id = json_data.get("station_id")
        
        self.wu_icon = json_data.get("image").get("url")
        
class WU_BoxLayout(BoxLayout):
    pass
        
    
class WU_WidgetApp(App):
    
    def build(self):
        return WU_GridLayout()
    
wuApp = WU_WidgetApp()        
    
if __name__== "__main__":
    wuApp.run()