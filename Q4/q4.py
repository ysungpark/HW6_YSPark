import matplotlib.pyplot as plt
import csv

plt.rc('font', family='Malgun Gothic')

if __name__ == "__main__":
    # 데이터 파일 읽기
    data = []
    with open('subway.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        next(reader)

        for row in reader:
            data.append(row)

    commute_data = []
    for row in data:
        commute_data.append([row[0], row[1], row[2], row[6], row[12], row[18], row[24]])

    boarding_top_30 = sorted(commute_data, key=lambda x: int(x[3]) if x[3].isdigit() else 0, reverse=True)[:30]
    alighting_top_30 = sorted(commute_data, key=lambda x: int(x[4]) if x[4].isdigit() else 0, reverse=True)[:30]
    commute_top_30 = sorted(commute_data, key=lambda x: int(x[3]) + int(x[4]) if x[3].isdigit() and x[4].isdigit() else 0, reverse=True)[:30]

    plt.figure(figsize=(12, 18))

    plt.subplot(3, 1, 1)
    plt.bar(range(len(boarding_top_30)), [int(row[3]) if row[3].isdigit() else 0 for row in boarding_top_30])
    plt.xticks(range(len(boarding_top_30)), [row[0] for row in boarding_top_30], rotation=90)
    plt.xlabel('지하철역')
    plt.ylabel('승차 수')
    plt.title('출근 시간대 최대 승차역 Top 30')

    plt.subplot(3, 1, 2)
    plt.bar(range(len(alighting_top_30)), [int(row[4]) if row[4].isdigit() else 0 for row in alighting_top_30])
    plt.xticks(range(len(alighting_top_30)), [row[0] for row in alighting_top_30], rotation=90)
    plt.xlabel('지하철역')
    plt.ylabel('하차 수')
    plt.title('출근 시간대 최대 하차역 Top 30')

    plt.subplot(3, 1, 3)
    plt.bar(range(len(commute_top_30)), [int(row[3]) + int(row[4]) if row[3].isdigit() and row[4].isdigit() else 0 for row in commute_top_30])
    plt.xticks(range(len(commute_top_30)), [row[0] for row in commute_top_30], rotation=90)
    plt.xlabel('지하철역')
    plt.ylabel('승하차 수')
    plt.title('출근 시간대 최대 승하차역 Top 30')

    plt.tight_layout()
    plt.show()
