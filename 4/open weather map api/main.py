import requests

URL = "http://api.weatherapi.com/v1/current.json?key=bbce8d91bde04460a0f110446240807&q=Szczecin&aqi=no"
#URL to klucz do API dzięki któremu możemy połączyć się z bazą danych
response = requests.get(URL) # linijka odpowiadająca za request GET z url podanego wyżej
weather_json = response.json() # linijka przetwarzająca treść odpowiedzi (będąca w formacie JSON) oraz zwraca ją jako słownik pythona
#powyższe 2 linijki odpowiadają za połączenie do API za pomocą biblioteki requests 
temperatura = weather_json.get("current").get("temp_c")
town = weather_json.get('location').get('name')
country = weather_json.get('location').get('country')
desc = weather_json.get("current").get("condition").get('text')

print("witaj w " + town + ", które znajduje się w " + country + "!\n")
print("obecnie jest "+str(temperatura)+" stopni celsjusza a ogólna pogoda to "+desc+"!" )