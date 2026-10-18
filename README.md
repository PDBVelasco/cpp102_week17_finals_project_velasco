# Simulated Device Monitoring and Alert System
 
**Student Name:** Peter Daniel B. Velasco
**Student Number:** 2601269
**Section:** 1CpE-A
 
## Project Description
This project simulates a menu of a monitoring system. To gain knowledge and experience with how a system menu would be like with real systems integrated.
## Features
- View all stored temperature readings
- Add a new reading (whole numbers from 0 to 100 only)
- Classify every reading
- Generate a numerical summary and overall status
- Reject invalid menu choices and invalid readings
 
## Requirements
- Python 
 
## How to Run
1. Open a terminal inside the Week17 folder.
2. Type: python device_monitor.py
   (On macOS or Linux, type: python3 device_monitor.py)
 
## Sample Output
SIMULATED DEVICE MONITORING SYSTEM
---------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit
 
## Test Cases
I performed 10 tests. 10 passed and 0 failed.
Full details are in test_cases.md.
 
## Known Limitations
- Readings are lost when the program closes.
- Cant add more classifications
- Numbers are only up to 100
 
## Reflection
The hardest part that I struggled with, was how to start the menu itself. I tried to do it without using a while true loop but that proved to be more of a headache. I solved a bug/problem with how to connect the functions. I would probably improve my knowledge more with loops because I stil get confused on how to accomplish what I visionize using loops. 