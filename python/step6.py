import csv
import random
import sys
import time
import winsound

maxInt = sys.maxsize

wiki_count = 10

print("Increasing csv field size limit...")
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)
        print(".", end="")

print("\nDone!\n")

wikis = []
wikis_header = []

examples = []

with open("D:\\velký dbs fily\\step3\\wikis.csv", mode="r", encoding="utf-8") as wikis_in:
    wikis_reader = csv.reader(wikis_in)

    firstline = True
    for row in wikis_reader:
        if firstline:
            wikis_header.append(row)
            firstline = False
            continue
        wikis.append(row)

with open("D:\\velký dbs fily\\step4\\wiki_examples.csv", mode="r", encoding="utf-8") as examples_in:
    examples_reader = csv.reader(examples_in)

    for row in examples_reader:
        examples.append(row)

with open("D:\\velký dbs fily\\step6\\wikis.csv", mode="w", encoding="utf-8", newline="") as wikis_out:
    with open("D:\\velký dbs fily\\step6\\wiki_examples.csv", mode="w", encoding="utf-8", newline="") as examples_out:
        wikis_writer = csv.writer(wikis_out)
        examples_writer = csv.writer(examples_out)

        chosen_wikis = random.sample(wikis, wiki_count)

        linecount = (chosen_wikis.__len__() / 100).__floor__()
        if linecount == 0:
            linecount = 1
        for i, wiki in enumerate(chosen_wikis):
            if i % linecount == 0:
                print("\r" + (i / linecount / 1).__str__() + "%", end="")

            for example in examples:
                if example[0] == wiki[0]:
                    examples_writer.writerow(example)

            wikis_writer.writerow(wiki)
print("\nDone!\n")

print("change the world;")
time.sleep(2)
print("my final message.")
time.sleep(3)
print("goodbye")
time.sleep(3)
winsound.PlaySound("./o95.wav", winsound.SND_FILENAME)
