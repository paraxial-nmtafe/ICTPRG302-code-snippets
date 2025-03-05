rj_file_handler = open("./text_files/romeojuliet.txt", "r")
for line in rj_file_handler:
    if('From' in line):
        print(line.strip())
rj_file_handler.close()

