import csv
import sys
import time
import winsound

pool_count = 250

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

with open("D:\\velký dbs fily\\pools.csv", mode="r", encoding="utf-8") as pools_in:
    with open("D:\\velký dbs fily\\step3\\pools.csv", mode="w", encoding="utf-8", newline="") as pools_out:
        with open("D:\\velký dbs fily\\step3\\unused_pools.csv", mode="w", encoding="utf-8", newline="") as pools_unused_out:
            pools_reader = csv.reader(pools_in)
            pools_writer = csv.writer(pools_out)
            pools_unused_writer = csv.writer(pools_unused_out)

            print("Counting lines...")
            linecount = 0
            for i, line in enumerate(posts_in):
                linecount = i
            posts_in.seek(0)
            linecount = (linecount / 10000).__floor__()
            print("Done!")


print("\nDone!\n")

print("change the world;")
time.sleep(2)
print("my final message.")
time.sleep(3)
print("goodbye")
time.sleep(3)
winsound.PlaySound("./o95.wav", winsound.SND_FILENAME)
