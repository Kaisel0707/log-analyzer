counts = {}
filename = input("Log file name: ")
while True:
    try:
        limit = int(input("Alert after how many alert failures? "))
        break
    except ValueError:
        print("please enter a number")
              
try:
    with open(filename, "r") as f:
        for line in f:
            if "failed" in line:
                parts = line.split()
                ip = parts[-1].replace("ip=", "")
                if ip in counts:
                    counts[ip] += 1
                else:
                    counts[ip] = 1
    for ip, n in counts.items():
        if n >= limit:
            print(f"ALERT: {ip} has {n} failed login attempts")
    print("Total failed logins:", sum(counts.values()))
except FileNotFoundError:
    print("file not found")
