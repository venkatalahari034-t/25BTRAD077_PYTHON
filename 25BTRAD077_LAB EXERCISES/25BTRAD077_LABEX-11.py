error = 0
warning = 0
info = 0

try:
    with open("sample.log", "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("Log file is empty.")
    else:
        for line in lines:
            if "ERROR" in line:
                error += 1
            elif "WARNING" in line:
                warning += 1
            elif "INFO" in line:
                info += 1

        print("Log File Summary")
        print("ERROR:", error)
        print("WARNING:", warning)
        print("INFO:", info)

except FileNotFoundError:
    print("File not found.")