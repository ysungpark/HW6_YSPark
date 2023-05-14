import csv
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

def process_csv(file_name):
    areas = []
    male_ratios = []
    female_ratios = []

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for i, row in enumerate(reader):
            if i >= 1:
                break

            area = row[0]
            male_population = int(row[3].replace(',', ''))
            female_population = int(row[4].replace(',', ''))
            total_population = int(row[1].replace(',', ''))

            male_ratio = male_population / total_population
            female_ratio = female_population / total_population

            areas.append(area)
            male_ratios.append(male_ratio)
            female_ratios.append(female_ratio)

    return areas, male_ratios, female_ratios

if __name__ == "__main__":
    file_names = ["2008_jeju.csv", "2013_jeju.csv", "2018_jeju.csv", "2022_jeju.csv"]

    fig, axs = plt.subplots(len(file_names), 1, figsize=(10, 2*len(file_names)))  

    for i, file_name in enumerate(file_names):
        areas, male_ratios, female_ratios = process_csv(file_name)

        ax = axs[i]

        ax.barh(areas, male_ratios, label='남성', color='b')
        ax.barh(areas, female_ratios, left=male_ratios, label='여성', color='r')

        
        for j in range(len(areas)):
            x = male_ratios[j] + female_ratios[j]
            ax.text(x + 0.01, j, f'{male_ratios[j]*100:.1f}%', color='black', va='center', weight='bold', fontsize=10)
            ax.text(x - female_ratios[j] - 0.04, j, f'{female_ratios[j]*100:.1f}%', color='black', va='center', weight='bold', fontsize=10)

        ax.set_xlabel('비율')
        ax.set_title(f'남녀 구성비 ({file_name})')
        ax.legend()

    plt.tight_layout()
    plt.show()
