import winsound
import time
import sys

def format_time():
    hours = y_time // 3600
    minutes = (y_time % 3600) // 60
    seconds = y_time % 60
    print(f"timer set for {hours:02d}:{minutes:02d}:{seconds:02d}")




y_time = 0

while True:
    try:
        hours = int(input("enter hours: "))
        if hours < 0:
            print("MUST BE GREATER THAN 0")
            continue

        minutes = int(input("enter minutes: "))
        if minutes < 0:
            print("MUST BE GREATER THAN 0")
            continue

        seconds = int(input("enter seconds: "))
        if seconds < 0:
            print("MUST BE GREATER THAN 0")
            continue

    except ValueError:
        print("ENTER A NUMBER")
        continue

    break

#print(f"Timer set for {hours:02d}:{minutes:02d}:{seconds:02d}")

hs = hours * 3600
ms = minutes * 60
y_time = hs + ms + seconds
format_time()
for i in range(y_time, -1, -1 ):
    secs= i % 60
    mins = (i % 3600) // 60
    hrs= i // 3600
    sys.stdout.write(f"\r{hrs:02d}:{mins:02d}:{secs:02d}")
    time.sleep(1)

print(f"\nHI! it's been {y_time} seconds")
winsound.Beep(1000, 400)
time.sleep(0.25)
winsound.Beep(1000, 400)
time.sleep(0.25)
winsound.Beep(1000, 400)


'''for x in range(3):
    for y in range(3):
        print('*', end="")

    print()'''

