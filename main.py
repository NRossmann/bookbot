
def main():
    path_to_file = "books/frankenstein.csv"
    
    with open(path_to_file) as f:
        file_contents = f.read()
        #print(file_contents)
        print(len(file_contents.split()))
main()