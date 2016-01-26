import pywapi


def enter_city():
       choose = int(input('Enter city: 1 - Drogobych 2 - Stryi 3 - Lviv 4 - Boryslav:'))
       if choose == 1:
              print("zip code is: 46106")
       if choose == 2:
              print('zip code is 46112')
       if choose == 3:
              print('zip code is 46101')
       if choose == 4:
              print('zip code is 46103')
       city_value = int()
       city_value = input('enter zip cod: ')
       weather_com_result = pywapi.get_weather_from_weather_com(city_value)
       #yahoo_result = pywapi.get_weather_from_yahoo(city_value)
       print("\nWeather.com says that current weather:\n is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "C now in city" + " and "
             + weather_com_result['current_conditions']['humidity'] + "humidity")
       #print("Yahoo says: It is " + yahoo_result['condition']['text'].lower() + " and " + yahoo_result['condition']['temp'] + "C now in your city.")

       if weather_com_result['current_conditions']['temperature'] < '0':
              print('fuck')
       #weather_com_result['current_conditions']['temperature'] = str(int((weather_com_result)))
       #print(type(weather_com_result['current_conditions']['temperature']))



enter_city()

'''city_value = int()
city_value = input('enter zip cod: ')
weather_com_result = pywapi.get_weather_from_weather_com(city_value)
#weather_com_result = pywapi.get_weather_from_weather_com('46106')
print("\nWeather.com says:\n It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Lviv" + " and " + weather_com_result['current_conditions']['humidity'] + "humidity"
      )'''

