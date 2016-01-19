#from weather import enter_city
import pywapi


class Clothes:
    def __init__(self, clothes):
        self.clothes = clothes

    def enter_clothes(self):
        choose = int(input('do you want to add clothes: 1 - yes 2 - no:'))
        if choose == 1:
            self.clothes = str(input('input clothes: '))
            f = open('clothes.txt', '+a')

            f.write(self.clothes)
            f.close()

            f = open('clothes.txt')
            while True:
                line = f.readline()
                if len(line) == 0:
                    break
                print(line, end='')
                continue

            f.close()
        if choose == 2:
            f = open('clothes.txt')
            f.read()

    def enter_city(self):
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
              print('you should wear warm clothes')


clothes_result = Clothes('')
clothes_result.enter_clothes()
res = Clothes('')
res.enter_city()






