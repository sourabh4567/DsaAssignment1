import time

years = [2023, 2024, 2025]
cities = ["Delhi", "Mumbai", "Bangalore"]

SENTINEL = -1

temperatures = [
    [SENTINEL for _ in range(len(cities))] for _ in range(len(years))
]

def input_temperatures():
    for i in range(len(years)):
        print(f"\nEnter temperatures for year {years[i]}:")
        for j in range(len(cities)):
            value = float(input(f"Temperature for {cities[j]}: "))
            temperatures[i][j] = value

def display_temperatures():
    print("\nTemperature Data:")
    print("Year", *cities, sep="\t")
    print("----------------------------")
    for i in range(len(years)):
        print(years[i], end="\t")
        for j in range(len(cities)):
            if temperatures[i][j] == SENTINEL:
                print("N/A", end="\t")
            else:
                print(temperatures[i][j], end="\t")
        print()

def row_major_access():
    print("\nRow-major access:")
    start = time.time()
    for i in range(len(years)):
        for j in range(len(cities)):
            value = temperatures[i][j]
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")

def column_major_access():
    print("\nColumn-major access:")
    start = time.time()
    for j in range(len(cities)):
        for i in range(len(years)):
            value = temperatures[i][j]
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")

def main():
    print("Welcome to the Temperature Data Manager with Sparse Data Handling")
    input_temperatures()
    display_temperatures()
    row_major_access()
    column_major_access()

if __name__ == "__main__":
    main()