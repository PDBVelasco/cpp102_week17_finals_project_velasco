readings = [28, 31, 35, 37, 29]

def main_menu():
    while True:
        print("SMULATED DEVICE MONITORING SYSTEM")
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
                if temp < 30:
                    status = "Normal"
                elif 30 <= temp <= 35:
                    status = "Warning"
                else:
                    status = "Critical"

                print(f"Reading {index}: {temp}°C")
        elif choice == "5":
            print("Thank you for using the Simulated Device Monitoring System. Goodbye!")
            break
main_menu()