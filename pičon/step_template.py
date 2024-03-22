import csv
import sys
import time
import winsound

maxInt = sys.maxsize

print("Increasing csv field size limit...")
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)
        print(".", end="")

print("\nDone!\n")

with open("D:\\velký dbs fily\\posts.csv", mode="r", encoding="utf-8") as posts_in:
    pass;


print("\nDone!\n")

print("change the world;")
time.sleep(2)
print("my final message.")
time.sleep(3)
print("goodbye")
time.sleep(3)
winsound.PlaySound("./o95.wav", winsound.SND_FILENAME)
