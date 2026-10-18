readings = [28, 31, 35, 37, 29]
def add_reading(readings):
    user_input = input("Enter new reading: ")

    if user_input == "":
        print("Invalid input. The reading cannot be empty.")
        return
    if not user_input.isdigit():
        print("Invalid input. Enter a whole number only.")
        return
    new_reading = int(user_input)

    if new_reading > 100:
        print("Invalid reading. Enter a value from 0 to 100.")
        return
    readings.append(new_reading)
    print("Reading added successfully.")

def classify_reading(reading, warning_limit, critical_limit):
    if reading < warning_limit:
        return "NORMAL"
    elif warning_limit <= reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"
def compute_total(readings):
    total = 0.0
    for reading in readings:
        total += reading
    return total

def compute_average(readings):
    return compute_total(readings) / len(readings)

def find_minimum(readings):
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum

def find_maximum(readings):
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum

def count_category(readings, warning_limit, critical_limit, category):
    count = 0
    for reading in readings:
        if reading < warning_limit:
            status = "NORMAL"
        elif warning_limit <= reading <= critical_limit:
            status = "WARNING"
        else:
            status = "CRITICAL"
        if status == category:
            count += 1
    return count

def determine_overall_status(warning_count, critical_count):
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITORING"
    return "NORMAL"

def display_summary(readings):
    print("\nMONITORING SUMMARY")
    print("---------------------")
    warning_limit, critical_limit = 30, 35
    total_count = len(readings)

    total_sum = compute_total(readings)
    average = compute_average(readings)
    lowest = find_minimum(readings)
    highest = find_maximum(readings)

    normals = count_category(readings, warning_limit, critical_limit, "NORMAL")
    warnings = count_category(readings, warning_limit, critical_limit, "WARNING")
    criticals = count_category(readings, warning_limit, critical_limit, "CRITICAL")

    normal_percentage = (normals / total_count) * 100
    warning_percentage = (warnings / total_count) * 100
    critical_percentage = (criticals / total_count) * 100

    overall_status = determine_overall_status(warnings, criticals)

    print(f"Number of readings : {total_count}")
    print(f"Total of readings  : {int(total_sum)}")
    print(f"Average temperature: {average:.2f} °C")
    print(f"Minimum temperature: {int(lowest)} °C")
    print(f"Maximum temperature: {int(highest)} °C")
    print("")
    print(f"NORMAL             : {normals} ({normal_percentage:.2f}%)")
    print(f"WARNING            : {warnings} ({warning_percentage:.2f}%)")
    print(f"CRITICAL           : {criticals} ({critical_percentage:.2f}%)")
    print("")
    print(f"Overall Status     : {overall_status}")

def main_menu():
    while True:
        print("SIMULATED DEVICE MONITORING SYSTEM")
        print("---------------------------------")
        print("[1] View Readings")
        print("[2] Add Reading")
        print("[3] Classify Readings")
        print("[4] Generate Summary")
        print("[5] Exit")

        choice = input("Enter menu choice: ")
        if choice == "1":
            print("CURRENT READINGS")
            print("----------------")
            for index, temp in enumerate(readings, start=1):
                print(f"Reading {index}: {temp}°C")

        elif choice == "2":
            add_reading(readings)

        elif choice == "3":
            print("READING CLASSIFICATION")
            print("-" * 25)
            for temp in readings:
                status = classify_reading(temp, 30, 35)
                print(f"{temp} °C - {status}")

        elif choice == "4":
            display_summary(readings)

        elif choice == "5":
            print("Thank you for using the Simulated Device Monitoring System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main_menu()