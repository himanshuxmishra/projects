import requests

# Function to get weather data
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    
    # Send a GET request to the API
    response = requests.get(complete_url)
    
    # Check if the response is valid (status code 200)
    if response.status_code == 200:
        data = response.json()
        
        # Extracting and displaying data
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        print(f"City: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description'].capitalize()}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("City not found or invalid API key. Please check your input.")

# Main function to run the weather app
def main():
    city = input("Enter city name: ")
    api_key = "47b455f1e2814998dd6e1860fdd62b09"  # Replace with your OpenWeatherMap API key
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
