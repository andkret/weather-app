import requests
import json
import datetime as dt
import taosrest

# get the data from the API
def get_weather(location, conn):
    payload = {'Key': 'fed028b417bf48408c552501221407', 'q': location, 'aqi': 'yes'}
    r = requests.get("http://api.weatherapi.com/v1/current.json", params=payload)

    # Get the json from the request's result
    r_string = r.json()

    current = r_string['current']
    
    #only take certain columns we are interested in
    #ex = normalized[['last_updated','temp_c','temp_f','wind_mph','wind_kph']]

    #fix time format
    origin_time = dt.datetime.strptime(current['last_updated'],'%Y-%m-%d %H:%M')
    current['last_updated'] = origin_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    #current['last_updated'] = current['last_updated'].strftime('%Y-%m-%d %H:%M:%S.%f')

    #print(current)  
    write_weather(location,current,conn)    

    return current

#open tdengine connection
def open_con():
    # all parameters are optional.
    # if database is specified,
    # then it must exist.
    
    try:
        conn = taosrest.connect(url="https://gw.us-east-1.aws.cloud.tdengine.com",
                    token="aa69a6e75f27bc2c6eda06012013c26d5b36ffad"
                    )
 
    except taosrest.Error as e:
        print(e)

    return conn

def write_weather(location, weather_js, conn):
    no_whitepsace_location = location.replace(" ", "")
    #print(no_whitepsace_location)
    conn.query(f"insert into weather.{no_whitepsace_location} values ('{weather_js['last_updated']}', {weather_js['temp_c']}, {weather_js['temp_f']}, {weather_js['wind_mph']}, {weather_js['wind_kph']})")     
    
# closes the tdengine connection
def close_con(conn):
    conn.close()



if __name__ == "__main__":
    
    conn = open_con()
    
    get_weather("berlin",conn)
    get_weather("san francisco",conn)

    close_con(conn)
