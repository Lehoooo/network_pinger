# Made by github.com/lehoooo | leho.dev
import time
from pythonping import ping
import datetime

def log_failure(time):
    try:
        file = open("failure.txt", "a")
        file.write("\nPings Failed! | Time: " + str(time))
        file.close()
    except Exception as e:
        print("Failed To Write :( Error: " + str(e))

def log_success(time, output):
    try:
        file = open("success.txt", "a")
        file.write("\nPings Successful! | Time: " + str(time) + " | Avg Ping: " + str(output))
        file.close()
    except Exception as e:
        print("Failed To Write :( Error: " + str(e))


while True:
    results = ping('1.1.1.1', timeout=1) # change this to any server with 100% uptime, really should be kept to 1.1.1.1 (cloudflare) but you could use google (8.8.8.8) too
    if results.success():
        a = datetime.datetime.now()
        log_success(str(a), str(results.rtt_avg_ms)) # will save time and average roundtrip ms (rtt_avg_ms)
        print("success logged | time: " + str(a))
    elif not results.success():
        a = datetime.datetime.now()
        log_failure(str(a))
        print("failure logged | time: " + str(a))
    time.sleep(5) # change this to whatever time (in seconds) you want to wait before doing the next ping check


