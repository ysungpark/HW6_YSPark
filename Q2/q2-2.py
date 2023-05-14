import csv
import matplotlib.pyplot as plt
import itertools

plt.rc('font', family='Malgun Gothic')

if __name__ == "__main__":
    f = open("random_dice.csv", 'r')
    data = csv.reader(f)
    header = next(data)

    counts = [[0, 0, 0, 0, 0, 0] for _ in range(4)]

    index = [1, 2, 3, 4, 5, 6]

    for i, limit in enumerate([101, 1001, 10001, 100001]):
        f.seek(0)
        next(data)
        for row in itertools.islice(data, limit):
            for j in range(6):
                if index[j] == int(row[0]):
                    counts[i][index[j] - 1] += 1

    labels = ['1', '2', '3', '4', '5', '6']
    colors = ['r', 'g', 'b', 'c']

    fig, axes = plt.subplots(nrows=2, ncols=2)
    fig.suptitle('Histogram of Dice Numbers')

    for i, ax in enumerate(axes.flat):
        ax.bar(labels, counts[i], color=colors[i])
        ax.set_xlabel('')
        ax.set_ylabel('해당 눈이 나온 횟수')
        ax.set_title('주사위 {}번 던졌을 때'.format(10**(i+2)))
        ax.set_ylim(0, max(counts[i]) + 1)

    plt.tight_layout()
    plt.show()
