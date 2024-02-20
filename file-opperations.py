file_name = "x-file.txt"
fd = open(file_name, 'a') # a for append (saves everything), w for write, r for read
while True:
    line = input("Enter a line(or just press Enter to quit): ")
    if line:
        fd.write(line + "\n")
    else:
        break
#w means for writing
fd.write("Hello world!")
fd.close()

