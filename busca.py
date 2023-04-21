import csv
import time
start_time = time.time()
with open(r'dados.csv', 'r') as fp:
    lines = fp.readlines()
    for row in lines:
        # check if string present on a current line
        word = 'TOODAY CONSULTORIA EM TECNOLOGIA DA INFORMACAO LTDA'
        #print(row.find(word))
        # find() method returns -1 if the value is not found,
        # if found it returns index of the first occurrence of the substring
        if row.find(word) != -1:
            print('string exists in file')
            print('line Number:', lines.index(row))
            print("--- %s seconds ---" % (time.time() - start_time))
            exit
