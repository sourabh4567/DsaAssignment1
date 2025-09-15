years = [2023, 2024, 2025]
cities = ["Delhi", "Mumbai", "Bangalore"]

# Initialize temperature matrix
temperatures = [
    [0 for _ in range(len(cities))] for _ in range(len(years))
]

def get_float_input(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_temperatures():
    for i in range(len(years)):
        print(f"\nEnter temperatures for year {years[i]}:")
        for j in range(len(cities)):
            temp = get_float_input(f"Temperature for {cities[j]}: ")
            temperatures[i][j] = temp

def display_temperatures():
    print("\nTemperature Data:")
    print("Year   ", end="")
    for city in cities:
        print(f"{city:>12}", end="")
    print()
    print("-" * (8 + len(cities) * 12))
    for i in range(len(years)):
        print(f"{years[i]:<6}", end="")
        for j in range(len(cities)):
            print(f"{temperatures[i][j]:>12.2f}", end="")
        print()

def main():
    print("Welcome to the Year-wise and City-wise Temperature Data Manager")
    input_temperatures()
    display_temperatures()

if __name__ == "__main__":
    main()
