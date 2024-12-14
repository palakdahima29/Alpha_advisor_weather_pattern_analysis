class WeatherData:
    def _init_(self, name, temp, humidity, rainfall):
        self.name = name
        self.temp = temp
        self.humidity = humidity
        self.rainfall = rainfall


def main():
    total_temp = 0
    total_humidity = 0
    total_rainfall = 0

    # Input the number of regions
    n = int(input("Enter number of regions: "))
    regions = []  # List to store data for 'n' regions

    for i in range(n):
        print(f"\nRegion {i + 1}:")
        name = input("Name: ")
        temp = float(input("Temp (°C): "))
        humidity = float(input("Humidity (%): "))
        rainfall = float(input("Rainfall (mm): "))

        # Create a WeatherData object and append it to the list
        region = WeatherData(name, temp, humidity, rainfall)
        regions.append(region)

        # Accumulate totals
        total_temp += temp
        total_humidity += humidity
        total_rainfall += rainfall

    # Calculate and display averages
    print("\nAverages:")
    print(f"Temp: {total_temp / n:.2f}°C, Humidity: {total_humidity / n:.2f}%, Rainfall: {total_rainfall / n:.2f} mm")


if _name_ == "_main_":
    main()
