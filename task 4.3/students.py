import csv

def get_top_performers(file_path, number_of_top_students = 5):
    with open(file_path) as rf:
        reader = csv.reader(rf)
        next(reader, None)
        sorted_list = sorted(list(reader), key = lambda student: student[2], reverse = True)
        return list(map(lambda student: student[0], sorted_list[:number_of_top_students]))
    
def sort_by_age(file_path):
    with open(file_path) as rf:
        with open('data/sorted_students.csv', 'w') as wf:
            reader = csv.reader(rf)
            header = next(reader, None)
            sorted_list = sorted(list(reader), key = lambda student: student[1], reverse = True)
            writer = csv.writer(wf)
            writer.writerow(header)
            writer.writerows(sorted_list)

file_path = 'data/students.csv'
print(get_top_performers(file_path))

file_path = 'data/students.csv'
sort_by_age(file_path)