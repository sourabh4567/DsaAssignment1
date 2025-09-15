weather_data = []

def insert_weather():
    date = input("Enter Date (DD-MM-YYYY): ")
    location = input("Enter Location: ")

    for record in weather_data:
        if record['date'] == date and record['location'] == location:
            print("Weather record for this date and location already exists!")
            return

    temperature = float(input("Enter Temperature: "))
    humidity = float(input("Enter Humidity (%): "))
    pressure = float(input("Enter Pressure (hPa): "))
    wind_speed = float(input("Enter Wind Speed (km/h): "))
    condition = input("Enter Condition (e.g., Sunny, Rainy): ")

    record = {
        'date': date,
        'location': location,
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure,
        'wind_speed': wind_speed,
        'condition': condition
    }
    weather_data.append(record)
    print("Weather record added successfully.")

def display_weather():
    if not weather_data:
        print("No weather records available.")
        return

    print("\nWeather Records:")
    print("Date\t\tLocation\tTemperature\tHumidity\tPressure\tWind Speed\tCondition")
    print("----------------------------------------------------------------------------------")
    for record in weather_data:
        print(f"{record['date']}\t{record['location']}\t{record['temperature']}\t\t{record['humidity']}\t{record['pressure']}\t{record['wind_speed']}\t\t{record['condition']}")
    print()

def main():
    while True:
        print("\nWeather Record Manager")
        print("1. Add Weather Record")
        print("2. Show Weather Records")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            insert_weather()
        elif choice == '2':
            display_weather()
        elif choice == '3':
            print("Exiting Weather Record Manager.")
            break
        else:
            print("Invalid choice. Please select from 1 to 3.")

main()