import csv
import re
import sys
import time
import winsound

maxInt = sys.maxsize
thumb_regex = re.compile(r"thumb #[0-9]+")
thumb_hashtagless_regex = re.compile(r"[0-9]+")


def inTags(string):
    for tag in tags:
        if tag[0] == string:
            return True
    return False


print("Increasing csv field size limit...")
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)
        print(".", end="")

print("\nDone!\n")

tags = []

print("Loading tags.csv")
with open("D:\\velký dbs fily\\step2\\tags_unique.csv", encoding="utf-8") as tags_in:
    tags_reader = csv.reader(tags_in)
    print("0.0%", end="")
    for linecount, line in enumerate(tags_in):
        pass
    tags_in.seek(0)
    linecount = (linecount / 1000).__floor__()
    firstline = True
    for row in tags_reader:
        if firstline:
            firstline = False
            continue
        tags.append(row)
        if tags_reader.line_num % linecount == 0:
            print("\r" + (tags_reader.line_num / linecount / 10).__str__() + "%", end="")
print("\nDone!\n")

with open("D:\\velký dbs fily\\wiki_pages.csv", mode="r", encoding="utf-8") as wikis_in:
    with open("D:\\velký dbs fily\\step3\\wikis.csv", mode="w", encoding="utf-8", newline="") as wikis_out:
        with open("D:\\velký dbs fily\\step3\\wikis_unused.csv", mode="w", encoding="utf-8",
                  newline="") as wikis_unused:
            with open("D:\\velký dbs fily\\step3\\wiki_examples.csv", mode="w", encoding="utf-8",
                      newline="") as wiki_examples:
                with open("D:\\velký dbs fily\\tag_implications.csv", mode="r", encoding="utf-8",
                          newline="") as implications_in:
                    with open("D:\\velký dbs fily\\step3\\tag_implications.csv", mode="w", encoding="utf-8",
                              newline="") as implications_out:
                        wikis_reader = csv.reader(wikis_in)
                        wikis_writer = csv.writer(wikis_out)
                        wikis_unused_writer = csv.writer(wikis_unused)
                        wiki_examples_writer = csv.writer(wiki_examples)
                        implications_reader = csv.reader(implications_in)
                        implications_writer = csv.writer(implications_out)

                        print("Counting lines...")
                        linecount = 0
                        for i, line in enumerate(wikis_reader):
                            linecount = i
                        wikis_in.seek(0)
                        linecount = (linecount / 10000).__floor__()
                        print("Done!")

                        wikis_writer.writerow(["tag", "content"])
                        wiki_examples_writer.writerow(["tag", "post"])
                        implications_writer.writerow(["tag", "implies"])

                        firstline = True
                        for i, row in enumerate(wikis_reader):
                            if i % linecount == 0:
                                print("\r" + (i / linecount / 100).__str__() + "%", end="")

                            if firstline:
                                wikis_unused_writer.writerow(row)
                                firstline = not firstline
                                continue

                            if inTags(row[3]):
                                wikis_writer.writerow([row[3], row[4]])
                                thumbs = thumb_regex.findall(row[4])
                                for thumb in thumbs:
                                    wiki_examples_writer.writerow([row[3], thumb_hashtagless_regex.search(thumb).group()])

                            else:
                                wikis_unused_writer.writerow(row)
                        print("\nFirst half done!\n")

                        print("Counting lines...")
                        linecount = 0
                        for i, line in enumerate(implications_reader):
                            linecount = i
                        implications_in.seek(0)
                        linecount = (linecount / 10000).__floor__()
                        print("Done!")

                        for i, row in enumerate(implications_reader):
                            if i % linecount == 0:
                                print("\r" + (i / linecount / 100).__str__() + "%", end="")

                            if (inTags(row[1])) and (inTags(row[2])):
                                implications_writer.writerow([row[1], row[2]])

print("\nDone!\n")

print("change the world;")
time.sleep(2)
print("my final message.")
time.sleep(3)
print("goodbye")
time.sleep(3)
winsound.PlaySound("./o95.wav", winsound.SND_FILENAME)
