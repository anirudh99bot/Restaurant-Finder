import requests
import json
import random

def SearchRestaurant() :
    
     params = {
        'entity_id' : city_id,
        'entity_type' : 'city',
        
         }

     response = requests.get('https://developers.zomato.com/api/v2.1/search', headers=headers, params=params)
     data = json.loads(response.text) #converting json file into python list
     n = data['results_shown']
     i= 0
     v=[]
     k=[data['restaurants'][i]['restaurant']['name']]
     for i in range (i,n):        #for loop for getting all the restaurants in one list

          k=data['restaurants'][i]['restaurant']['name']
          v.append(k)
     restaurant= v
     print("Your Restaurant: %s "%random.choice(restaurant))
          
    
    
def LocationAndEstimate() :
    
  
    from geopy.geocoders import Nominatim
    from geopy.distance import geodesic
    geolocator = Nominatim(user_agent="google maps", timeout=None)
  
    x = geolocator.geocode((a))
    c =((x.latitude,x.longitude)) #Coordinates of current city
    print ("Current destination coordinates:  ")
    print(c)
         
    
    city_2 = geolocator.geocode((city2))
    d = ((city_2.latitude,city_2.longitude)) #Coordinates of destination city

    
    e =(geodesic(c,d).km) #Calculate the Distance between the two cities
    

    #Fare estimate w.r.t to Uber
    
    if ( e <= 20 ):
         fare = 60 + (e * 6)
         print("Your estimate fare for ride will be = %d Rs"%(fare))
    elif (e > 20) :
         fare = 60 + (20 * 6 ) + ((e-20)*12)
         print("Your estimate fare for ride will be = %d Rs"%(fare))
    else:
         print("No fare")
         
if __name__ == "__main__":
     print("Welcome to Restaurant Finder")
     a=input("Enter current city : ")
     city2=input("Enter destination city: ")


     headers = {
    'Accept': 'application/json',
    'user-key': '8f43e5828484c5a3673c0ed6b14583b5',
    }
   
     params = {
    'q': city2,
    }



     response = requests.get('https://developers.zomato.com/api/v2.1/cities', headers=headers, params=params)
     data=response.json()
     city_id = data['location_suggestions'][0]['id']
     SearchRestaurant()
     LocationAndEstimate()
     print("Thank you for choosing our service")
