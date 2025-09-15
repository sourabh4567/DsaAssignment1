years = [2023, 2024, 2025]
cities = ["Delhi", "Mumbai", "Bangalore"]

SENTINEL = -1
temperatures = [[SENTINEL for _ in cities] for _ in years]

def insert_temperature():
    try:
        year = int(input("Enter year: "))
        if year not in years:
            print("Invalid year. Available years:", years)
            return
        city = input("Enter city: ").strip().title()
        if city not in cities:
            print("Invalid city. Available cities:", cities)
            return
        value = float(input("Enter temperature: "))
        i = years.index(year)
        j = cities.index(city)
        temperatures[i][j] = value
        print("Insert -> Time: O(1), Space: O(1)")
    except ValueError:
        print("Invalid input. Please enter correct values.")

def delete_temperature():
    try:
        year = int(input("Enter year: "))
        if year not in years:
            print("Invalid year. Available years:", years)
            return
        city = input("Enter city: ").strip().title()
        if city not in cities:
            print("Invalid city. Available cities:", cities)
            return
        i = years.index(year)
        j = cities.index(city)
        temperatures[i][j] = SENTINEL
        print("Delete -> Time: O(1), Space: O(1)")
    except ValueError:
        print("Invalid input.")

def retrieve_temperatures():
    print("\nTemperatures:")
    print("Year", *cities, sep="\t")
    for i in range(len(years)):
        print(years[i], end="\t")
        for j in range(len(cities)):
            if temperatures[i][j] == SENTINEL:
                print("N/A", end="\t")
            else:
                print(f"{temperatures[i][j]:.2f}", end="\t")
        print()
    print("Retrieve -> Time: O(R x C), Space: O(1) extra space")

def main():
    while True:
        print("\n===== Temperature Data Manager =====")
        print("1. Insert")
        print("2. Delete")
        print("3. Retrieve")
        print("4. Exit")
        choice = input("Choose: ")
        if choice == '1':
            insert_temperature()
        elif choice == '2':
            delete_temperature()
        elif choice == '3':
            retrieve_temperatures()
        elif choice == '4':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
