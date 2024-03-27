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

post_ids = []

with open("D:\\velký dbs fily\\step1\\posts.csv", encoding="utf-8") as posts_in:
    posts_reader = csv.reader(posts_in)
    print("0.0%", end="")
    for linecount, line in enumerate(posts_reader):
        pass
    posts_in.seek(0)
    linecount = (linecount / 1000).__floor__()
    firstline = True
    for row in posts_reader:
        if firstline:
            firstline = False
            continue
        post_ids.append(row[0])

with open("D:\\velký dbs fily\\step3\\wiki_examples.csv", mode="r", encoding="utf-8") as wiki_examples_in:
    with open("D:\\velký dbs fily\\step4\\wiki_examples.csv", mode="w", encoding="utf-8", newline="") as wiki_examples_out:
        with open("D:\\velký dbs fily\\step4\\wiki_examples_unused.csv", mode="w", encoding="utf-8", newline="") as wiki_examples_unused:
            examples_reader = csv.reader(wiki_examples_in)
            examples_writer = csv.writer(wiki_examples_out)
            examples_unused = csv.writer(wiki_examples_unused)

            print("Counting lines...")
            linecount = 0
            for i, line in enumerate(examples_reader):
                linecount = i
            wiki_examples_in.seek(0)
            linecount = (linecount / 10000).__floor__()
            print("Done!")

            for i, row in enumerate(examples_reader):
                if i % linecount == 0:
                    print("\r" + (i / linecount / 100).__str__() + "%", end="")

                if row[1] in post_ids:
                    examples_writer.writerow(row)
                else:
                    examples_unused.writerow(row)

print("\nDone!\n")

print("change the world;")
time.sleep(2)
print("my final message.")
time.sleep(3)
print("goodbye")
time.sleep(3)
winsound.PlaySound("./o95.wav", winsound.SND_FILENAME)
