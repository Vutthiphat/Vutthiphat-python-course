def get_temperatures():
    """Returns a list of daily temperatures for a week."""
    # Predefined temperature values for 7 days
    temperatures = [22.5, 24.0, 28.0, 25.5, 19.0, 21.5, 24.0]
    return temperatures


def analyze_temps(temp_list):
    """Calculates average, highest, and lowest temperatures from a list."""
    # Local variable for average temperature
    avg_temp = sum(temp_list) / len(temp_list)
    high_temp = max(temp_list)
    low_temp = min(temp_list)

    # Returns all three values as a tuple
    return avg_temp, high_temp, low_temp


def display_analysis(avg, high, low):
    """Prints the formatted temperature analysis results."""
    print("Temperature Analysis for the Week:")
    print(f"Average: {avg:.1f}°C")
    print(f"Highest: {high}°C")
    print(f"Lowest: {low}°C")


def main():
    # Retrieve the temperatures
    temps = get_temperatures()

    # Analyze the temperature data
    avg, high, low = analyze_temps(temps)

    # Display the formatted results
    display_analysis(avg, high, low)


if __name__ == "__main__":
    main()
    