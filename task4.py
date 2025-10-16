import time

def countdown(start, step, alert_every=5):
    seconds = 0
    while start > 0:
        if seconds == alert_every:
            print(f"{start} seconds left!!!")
            seconds = 0
        else:
            print(start)
        start -= step
        seconds += 1


        time.sleep(0.5)
    print("Time's up!!!")
    exit(0)

lsofinp = [int(n) for n in input("Input start, step, alert_every in spaces pls: ").split() if n.isnumeric()]

if len(lsofinp) == 3:
    countdown(start=lsofinp[0], step=lsofinp[1], alert_every=lsofinp[2])
countdown(start=lsofinp[0], step=lsofinp[1])