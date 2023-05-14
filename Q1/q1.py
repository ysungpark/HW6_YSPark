import csv
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

def process_csv(file_name):
    month_data = {}

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            date = row['날짜']
            temperature = float(row['평균기온(℃)'])
            month = date.split('-')[1]

            if month not in month_data:
                month_data[month] = [temperature]
            else:
                month_data[month].append(temperature)

    months = []
    avg_temperatures = []

    for month, temperatures in month_data.items():
        avg_temperature = sum(temperatures) / len(temperatures)
        months.append(month)
        avg_temperatures.append(avg_temperature)

    return months, avg_temperatures

if __name__ == "__main__":
    file_names = ["seoul.csv", "jeju.csv", "korea.csv", "daejun.csv", "busan.csv"]

    all_months = []
    all_avg_temperatures = []

    for file_name in file_names:
        months, avg_temperatures = process_csv(file_name)
        all_months.append(months)
        all_avg_temperatures.append(avg_temperatures)

    plt.figure(figsize=(10, 6))

    for months, avg_temperatures, file_name in zip(all_months, all_avg_temperatures, file_names):
        plt.plot(months, avg_temperatures, label=file_name[:-4])

    plt.xlabel('월')
    plt.ylabel('평균기온(℃)')
    plt.title('지역별 월별 평균기온')
    plt.legend()
    plt.show()
