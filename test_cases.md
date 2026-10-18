# Test Cases – Simulated Device Monitoring and Alert System
 
Tested by: Peter Daniel B. Velasco    Date: 10.18.26
| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
| --- | --- | --- | --- | --- |
|TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | Reading 1: 28°C, Reading 2: 31°C, Reading 3: 35°C, Reading 4: 37°C, Reading 5: 29°C | Pass
|TC02 | Choose 2, enter 33 | “Reading added successfully.” | Reading added successfully. | Pass
|TC03 | Choose 2, enter abc | Rejected; list unchanged | Invalid input. Enter a whole number only. | Pass
|TC04 | Choose 2, enter -5 | Rejected; list unchanged | Invalid input. Enter a whole number only. | Pass
|TC05 | Choose 2, enter 120 | Rejected; list unchanged | Invalid reading. Enter a value from 0 to 100. | Pass
|TC06 | Add 30, then choose 3 | 30 °C -> WARNING | 30 °C - WARNING | Pass
|TC07 | Choose 3 | 35 °C -> WARNING | 35 °C - WARNING | Pass
|TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | Number of readings : 5, Total of readings  : 160, Average temperature: 32.00 °C, Minimum temperature: 28 °C, Maximum temperature: 37 °C
|TC09 | Enter 9 | Error message; menu shown again | same result | Pass
|TC10 | Choose 5 | Exit message; program ends |same result | Pass