readings =[28, 31, 35, 37, 29]

def readings_classification(readings):
    results = []
    for reading in readings:
        if reading < 30:
            results.append("NORMAL") 
        elif reading <= 35:
            results.append("WARNING")
        else:
            results.append("CRITICAL")
    return results

total_runs = 0
for reading in readings_classification(readings):
    if reading == "NORMAL":
        total_runs += 1

print(total_runs)