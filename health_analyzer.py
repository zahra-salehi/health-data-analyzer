
# Health Data Analyzer
# Version 1.2

import csv

threshold_heart_rates = 80
threshold_temperature = 37.0

def read_health_data(filename):
    heart_rates = []
    temperatures = []
    age = None

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                if row["age"]:
                    age = int(row["age"])
            except ValueError:
                pass

            try:
                if row["heart_rate"]:
                    heart_rates.append(int(row["heart_rate"]))
            except ValueError:
                pass

            try:
                if row["temperature"]:
                    temperatures.append(float(row["temperature"]))
            except ValueError:
                pass

    return age, heart_rates, temperatures

def calculate_statistics(measurements):
    if len(measurements) == 0:
        return None

    total = sum(measurements)
    average = total / len(measurements)
    minimum = min(measurements)
    maximum = max(measurements)

    return average, minimum, maximum

def count_above_threshold(measurements, threshold):
    count = 0

    for value in measurements:
        if value > threshold:
            count = count + 1

    return count


def find_above_threshold(measurements, threshold):
    for value in measurements:
        if value > threshold:
            print(value)

def analyze_measurements(name, measurements, threshold):
    print("\n" + name + " Analysis")
    print("Measurements:", measurements)

    stats = calculate_statistics(measurements)

    if stats is None:
        print("No measurements available.")
        return

    average, minimum, maximum = stats

    print("Average:", average)

    if average > threshold:
        print("Average is above the threshold.")
    else:
        print("Average is not above the threshold.")

    print("Minimum:", minimum)
    print("Maximum:", maximum)

    count = count_above_threshold(measurements, threshold)
    print("Measurements above", threshold, ":", count)

    print("Values above the threshold:")
    find_above_threshold(measurements, threshold)

age, heart_rates, temperatures = read_health_data("health_data.csv")
    
# Display the report
print("================================")
print("     HEALTH DATA ANALYZER")
print("================================")

print("Age:", age)

analyze_measurements("Heart Rate", heart_rates, threshold_heart_rates)
analyze_measurements("Temperature", temperatures, threshold_temperature)
