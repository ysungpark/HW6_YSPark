import csv
import matplotlib.pyplot as plt
import random as r

if __name__ == "__main__":
    f = open("random_dice.csv", 'w', newline='')
    wr = csv.writer(f)
    count = [0, 0, 0, 0, 0, 0]
    index = [1, 2, 3, 4, 5, 6]
    for i in range(100000):
        rnum = r.randrange(1, 7)
        wr.writerow([rnum])
    f.close()
