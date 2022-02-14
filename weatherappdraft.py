
import requests


def weather_data(zip= None, city = None):
    baseurl= "http://api.openweathermap.org/data/2.5/weather?units=imperial"
    api_key = "21631040e37fda8d6d6d5d9cd0b6964d"
    if zip is not None:
        baseurl += "&zip="+str(zip)+",us"
    else: 
        baseurl += "&q="+str(city)+",us"
        baseurl += "&appid="+str(api_key)
        r = requests.get(baseurl)
        return r

def display(resp):
    if resp.status_code == 200:
        data = resp.json()
        print(f"""{data['name']} Weather Forecast:
        Type: {data['weather'][0]['description']}
        Wind Speed : {data['wind']['speed']} miles/hr
        Visibility : {data['visibility']} m
        Min. Temp : {data['main']['temp_min']} F
        Max Temp : {data['main']['temp_max']} F
        """)
        
    else:
        print("Failed Request, Error:", resp.status_code)

def main():
    while True:
        choice = int(input("Choose a search option :\n1. By Zip Code\n2. By City Name\n3. Exit\n"))
        if choice == 1:
            try:
                zipcode =int(input("Enter Your Zip Code: "))
                resp = weather_data(zipcode, None)
                display(resp)
            except Exception as ex:
                print("Error: ", ex)
        elif choice == 2:
            try:
                cityname = input("Enter Your City Name: ")  
                resp = weather_data(None, cityname)
                display(resp)
            except Exception as ex:
                print("Error: ", ex )
        elif choice == 3:
            break
        else:
            resp = "Exit"
            print ("Not Available try again\n")

if __name__==  "__main__":
    main()



            
            

         

    


