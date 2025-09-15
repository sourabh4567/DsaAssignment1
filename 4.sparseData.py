years = [2023, 2024, 2025]
cities = ["Delhi", "Mumbai", "Bangalore"]

SENTINEL = -1  # Represents missing temperature data

# Initialize temperatures with sentinel
temperatures = [
    [SENTINEL for _ in range(len(cities))] for _ in range(len(years))
]

def input_temperatures():
    for i in range(len(years)):
        print(f"\nEnter temperatures for year {years[i]}:")
        for j in range(len(cities)):
            value = input(f"Temperature for {cities[j]} (press Enter to skip): ").strip()
            if value == "":
                temperatures[i][j] = SENTINEL
            else:
                try:
                    temperatures[i][j] = float(value)
                except ValueError:
                    print("Invalid input, storing as N/A")
                    temperatures[i][j] = SENTINEL

def display_temperatures():
    print("\nTemperature Data:")
    print("Year", *cities, sep="\t")
    print("-" * (8 + len(cities) * 12))
    for i in range(len(years)):
        print(years[i], end="\t")
        for j in range(len(cities)):
            if temperatures[i][j] == SENTINEL:
                print("N/A", end="\t")
            else:
                print(f"{temperatures[i][j]:.2f}", end="\t")
        print()

def main():
    print("Welcome to the Sparse Temperature Data Manager")
    input_temperatures()
    display_temperatures()

if __name__ == "__main__":
    main()
