import csv
import random
import sys
import time
import winsound

pool_count = 5

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

post_ids = []

with open("D:\\velký dbs fily\\step1\\posts.csv", encoding="utf-8") as posts_in:
    posts_reader = csv.reader(posts_in)
    print("Initializing...", end="")
    # for linecount, line in enumerate(posts_reader):
    #     pass
    # posts_in.seek(0)
    # linecount = (linecount / 1000).__floor__()
    firstline = True
    for i, row in enumerate(posts_reader):
        # if i % linecount == 0:
        #     print("\r" + (i / linecount / 100).__str__() + "%", end="")
        if firstline:
            firstline = False
            continue
        post_ids.append(row[0])

with open("D:\\velký dbs fily\\pools.csv", mode="r", encoding="utf-8") as pools_in:
    with open("D:\\velký dbs fily\\step5\\pools.csv", mode="w", encoding="utf-8", newline="") as pools_out:
        with open("D:\\velký dbs fily\\step5\\unused_pools.csv", mode="w", encoding="utf-8", newline="") as pools_unused_out:
            with open("D:\\velký dbs fily\\step5\\pool_posts.csv", mode="w", encoding="utf-8", newline="") as pool_posts_out:
                with open("D:\\velký dbs fily\\step5\\unused_pool_posts.csv", mode="w", encoding="utf-8", newline="") as unused_pool_posts_out:
                    pools_reader = csv.reader(pools_in)
                    pools_writer = csv.writer(pools_out)
                    pools_unused_writer = csv.writer(pools_unused_out)
                    pool_posts_writer = csv.writer(pool_posts_out)
                    pool_posts_unused_writer = csv.writer(unused_pool_posts_out)

                    print("Counting lines...")
                    linecount = 0
                    for i, line in enumerate(pools_reader):
                        linecount = i
                    pools_in.seek(0)
                    linecount = (linecount / 10000).__floor__()
                    print("\nDone!\n")

                    pools_writer.writerow(["id", "name", "description"])
                    pool_posts_writer.writerow(["pool", "post"])
                    pool_posts_unused_writer.writerow(["pool", "post"])
                    loaded_pools = []

                    print("Loading pools...")
                    firstrow = True
                    for i, row in enumerate(pools_reader):
                        if i % linecount == 0:
                            print("\r" + (i / linecount / 100).__str__() + "%", end="")

                        if firstrow:
                            pools_unused_writer.writerow(row)
                            firstrow = False
                            continue

                        loaded_pools.append(row)
                    print("\nDone!\n")

                    chosen_pools = random.sample(loaded_pools, pool_count)

                    print("Saving pools...")
                    emptyPool = True
                    for i, row in enumerate(loaded_pools):
                        if i % linecount == 0:
                            print("\r" + (i / linecount / 100).__str__() + "%", end="")

                        if row in chosen_pools:
                            pools_writer.writerow([row[0], row[1], row[5]])

                            posts_in_chosen_pool = row[8].replace('{', '').replace('}', '').split(',')

                            # adding an empty pool to allow for more queries
                            if not emptyPool or random.random() < 0.99:
                                for post in posts_in_chosen_pool:
                                    if post in post_ids:
                                        pool_posts_writer.writerow([row[0], post])
                                    else:
                                        pool_posts_unused_writer.writerow([row[0], post])
                            else:
                                print("\nPool #" + row[0] + " " + row[1] + " will be empty")
                                emptyPool = False
                        else:
                            pools_unused_writer.writerow(row)
                    if emptyPool:
                        print("ERROR: NO EMPTY POOL ADDED")
                        exit(-1)

print("\nDone!\n")

print("change the world;")
time.sleep(2)
print("my final message.")
time.sleep(3)
print("goodbye")
time.sleep(3)
winsound.PlaySound("./o95.wav", winsound.SND_FILENAME)
