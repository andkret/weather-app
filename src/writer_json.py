import requests
import json
import datetime as dt
import taosrest

# get the data from the API
def get_weather(location, conn):

    # Create your key and replace mine with it
    payload = {'Key': 'fed028b417bf48408c552501221407', 'q': location, 'aqi': 'yes'}
    r = requests.get("http://api.weatherapi.com/v1/current.json", params=payload)

    # Get the json from the request's result
    r_string = r.json()

    # Take only the current part of the JSON
    current = r_string['current']

    # Fix time format from YYYY-MM-DD hh:mm:ss to -> YYYY-MM-DDThh:mm:ssZ
    # create datetime object from string
    origin_time = dt.datetime.strptime(current['last_updated'],'%Y-%m-%d %H:%M') 
    
    #turn datetime into formated string for tdengine
    # Keep in mind this will create timestamps in zulu time. The api only sends you local time.
    # We should fix this, but I can't be bothered right now
    current['last_updated'] = origin_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    #print(current)  
    # write the weather data to tdengine
    write_weather(location,current,conn)    

    # we don't need this right now, but I kept it
    return current

#open tdengine connection
def open_con():
 
    # Open a connection to tdengine cloud. Use the url and token specified in the instance
    try:
        conn = taosrest.connect(url="https://gw.us-east-1.aws.cloud.tdengine.com",
                    token="aa69a6e75f27bc2c6eda06012013c26d5b36ffad"
                    )
 
    except taosrest.Error as e:
        print(e)

    return conn

# Writes the weather data to tdengine
def write_weather(location, weather_js, conn):
    
    # Remove the whitespaces from the locations (tdengine tables don't have whitespaces -> "sanfrancisco" instead of "san francisco")
    no_whitepsace_location = location.replace(" ", "")

    # For debugging    
    # print(no_whitepsace_location)

    # write measurement to tdengine
    conn.query(f"insert into weather.{no_whitepsace_location} values ('{weather_js['last_updated']}', {weather_js['temp_c']}, {weather_js['temp_f']}, {weather_js['wind_mph']}, {weather_js['wind_kph']})")     
    
# closes the tdengine connection
def close_con(conn):
    conn.close()



if __name__ == "__main__":
    
    # open connection
    conn = open_con()
    
    # write data for berlin
    get_weather("berlin",conn)

    # write data for san francisco
    get_weather("san francisco",conn)

    # close connection and end the program
    close_con(conn)
