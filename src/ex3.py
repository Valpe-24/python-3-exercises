
def create_files(file_name):
    lines = []
    words_num = 0

    with open(file_name, 'r') as file_1: 
        while True: 
            line = file_1.readline().split()
            if not line:
                break
            lines.append(line)
    

    with open('files/large-words.txt', 'w') as file_2:
        for line in lines: 
            for word in line: 
                if len(word) >= 3:
                    words_num += 1
                    file_2.writelines(f'{word}\n')

    with open('files/small-words.txt', 'w') as file_3:
        for line in lines: 
            for word in line: 
                if len(word) < 3:
                    words_num += 1
                    file_3.writelines(f'{word}\n')
    return words_num




def ex3():
    total_words = create_files("files/words.txt")
    print(f"Total words: {total_words}.")

ex3()