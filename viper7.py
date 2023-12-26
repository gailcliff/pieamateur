
with open('notes2.txt', 'r+') as file:

    print(file.read())  # read the whole file at once
    print(file.readlines())  # read the file and pass each line into a list

    for line in file:  # most efficient way of reading line by line.
        print(line)

    file.write("foobar") # write to file
    file.writelines([str(i) for i in range(10)])  # pass in an iterable of strings to write
    file.flush()  # flush

print(file.closed)  # check if file is closed