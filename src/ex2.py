import csv
list_1 = []
list_2 = []
list_3 = []
visits = 0

def read_csv(input_file, row_list):
    with open(input_file) as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            row_list.append(row)

def find_total_visits():
    read_csv('../files/week-1.csv', list_1)
    read_csv('../files/week-2.csv', list_2)
    read_csv('../files/week-3.csv', list_3)
     
    for i in list: 
        if '1' == i:
            visits += 1



def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()