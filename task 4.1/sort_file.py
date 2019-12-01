def sort_file(filename:str):
    names = []
    with open(filename) as rf:
        with open('data/sorted_names.txt', 'w') as wf:
            for line in rf:
                names.append(line)
            for line in sorted(names):
                wf.write(line)

filename = 'data/unsorted_names.txt'
sort_file(filename)