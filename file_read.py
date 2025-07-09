def cnt_wrd_file(filename):
    try:
        with open(filename, "r") as file:
            content=file.read()
            wrds=content.split()
            wrd_cnt=len(wrds)
            print("Total number of words:", wrd_cnt)
    except FileNotFoundError:
        print("File not found. Please check the filename.")
cnt_wrd_file("new_py.txt")
