import re
def read_log(filename):
    counts = {}
    with open(filename, "r") as f:
        for line in f:
            if "failed" in line:
                match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
                if match:
                    ip = match.group()
                    if ip in counts:
                        counts[ip] += 1
                    else:
                        counts[ip] = 1
    return counts
def show_alerts(counts, limit):
    for ip, n in counts.items():
        if n >= limit:
            print(f"ALERT: {ip} has {n} failed login attempts")
def ask_limit():
    while True:
        try:
            limit = int(input("Alert after how many failures? "))
            return limit
        except ValueError:
            print("please enter a number")
filename = input("Log file name: ")
limit = ask_limit()
try:
    counts = read_log(filename)
    show_alerts(counts, limit)
    print("Total failed logins:", sum(counts.values()))
except FileNotFoundError:
    print("file not found")
