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
    with open("D:\\velký dbs fily\\step1\\posts.csv", mode="w", encoding="utf-8", newline="") as posts_out:
        with open("D:\\velký dbs fily\\step1\\user_ids.csv", mode="w", encoding="utf-8", newline="") as users_out:
            with open("D:\\velký dbs fily\\step1\\extracted_tags.csv", mode="w", encoding="utf-8", newline="") as extracted_tags_out:
                posts_reader = csv.reader(posts_in)
                posts_writer = csv.writer(posts_out)
                users_writer = csv.writer(users_out)
                extracted_tags_writer = csv.writer(extracted_tags_out)

                print("Counting lines...")
                linecount = 0
                for i, line in enumerate(posts_in):
                    linecount = i
                posts_in.seek(0)
                linecount = (linecount / 10000).__floor__()
                print("Done!")

                print("Writing valid posts to D:\\velký dbs fily\\step1\\posts.csv")
                print("Writing user ids to D:\\velký dbs fily\\step1\\user_ids.csv")
                print("Writing tags to D:\\velký dbs fily\\step1\\extracted_tags.csv")
                users_writer.writerow(["user_id"])
                extracted_tags_writer.writerow(["tags"])

                firstline = True
                for i, row in enumerate(posts_reader):
                    if i % linecount == 0:
                        print("\r" + (i / linecount / 100).__str__() + "%", end="")

                    if firstline:
                        posts_writer.writerow(row)
                        firstline = False
                        continue

                    users_writer.writerow([row[1]])

                    if row[14] != "":
                        users_writer.writerow([row[14]])

                    if row[20] == "f":
                        posts_writer.writerow(row)

                        temp_tags = row[8].split(" ")

                        for tag in temp_tags:
                            extracted_tags_writer.writerow([tag])

print("\nDone!\n")

print("change the world;")
time.sleep(2)
print("my final message.")
time.sleep(3)
print("goodbye")
time.sleep(3)
winsound.PlaySound("./o95.wav", winsound.SND_FILENAME)
