import csv

tags = []
tags_header = []

print("Loading tags.csv")
with open("D:\\velký dbs fily\\tags.csv", encoding="utf-8") as tags_in:
    tags_reader = csv.reader(tags_in)

    print("0.0%", end="")
    for linecount, line in enumerate(tags_in):
        pass
    tags_in.seek(0)
    linecount = (linecount / 1000).__floor__()

    firstline = True
    for row in tags_reader:
        if firstline:
            tags_header.append(row)
            firstline = False
            continue
        tags.append(row)
        if tags_reader.line_num % linecount == 0:
            print("\r" + (tags_reader.line_num / linecount / 10).__str__() + "%", end="")
print("\nDone!\n")

# Tag categories:
# 1 - artist
# 3 - copyright
# 4 - character
#


with open("D:\\non")