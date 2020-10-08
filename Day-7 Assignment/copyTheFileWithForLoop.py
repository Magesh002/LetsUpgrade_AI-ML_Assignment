with open("originalFile.txt", "r") as of:
    with open("duplicateFile.txt", "w") as df:
        for line in of:
            df.write(line)
of.close()
df.close()