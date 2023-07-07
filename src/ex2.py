import csv
list_1 = []
# list_2 = []
# list_3 = []

def read_csv(input_file, row_list):
    with open(input_file) as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            row_list.append(row)

def find_total_visits():
    visits = 0
    read_csv('files/week-1.csv', list_1)
    read_csv('files/week-2.csv', list_1)
    read_csv('files/week-3.csv', list_1)
     
    for index, item in enumerate(list_1): 
        if index != 0:
            for i in item: 
                if '1' in i:
                    visits += 1

    # for index, item in enumerate(list_2): 
    #     if index != 0:
    #         for i in item: 
    #             if '1' in i:
    #                 visits += 1

    # for index, item in enumerate(list_3): 
    #     if index != 0:
    #         for i in item: 
    #             if '1' in i:
    #                 visits += 1
    return visits

    



def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()