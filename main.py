import csv


def main():

    with open('абоненты.csv', encoding='utf-8-sig') as file_1:
        reader = csv.DictReader(file_1, delimiter=';')
        results = [item for item in reader]

    with open('Начисления_абоненты.csv', 'w', newline='', encoding='utf-8-sig') as file_2:
        fieldnames = list(results[0].keys()) + ['Начислено']
        writer = csv.DictWriter(file_2, fieldnames=fieldnames, extrasaction='ignore', delimiter=';')
        writer.writeheader()
        for string in results:
            if string['Тип начисления'] == '1':
                string['Начислено'] = float(301.26)
            else:
                string['Начислено'] = int(string['Текущее']) - int(string['Предыдущее'])
            writer.writerow(string)

    with open('Начисления_дома.csv', 'w', newline='', encoding='utf-8-sig') as file_3:
        fieldnames = ['№ строки', 'Улица', '№ дома', 'Начислено']
        write = csv.DictWriter(file_3, fieldnames=fieldnames, extrasaction='ignore', delimiter=';')
        count = 1
        res_dict = dict()
        for line in results:
            if line['№ дома'] not in res_dict.keys():
                line['№ строки'] = count
                count += 1
                res_dict[line['№ дома']] = line
            else:
                res_dict[line['№ дома']]['Начислено'] = res_dict[line['№ дома']]['Начислено'] + line['Начислено']

        grouping_by_house = list(res_dict.values())
        write.writeheader()
        write.writerows(grouping_by_house)


if __name__ == '__main__':
    main()
