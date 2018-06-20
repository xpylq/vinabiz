import vinabiz.component.dbComponent as dbComponent
import csv

base_csv_dir = "F:\\vinabiz\\csv"


def excel():
    list = dbComponent.get_all(1, 10000)
    list_1 = []
    list_2 = []
    list_3 = []
    for data in list:
        # 第一个csv
        list_temp_1 = []
        list_temp_1.append(data['guid'])
        list_temp_1.append(data['url'])
        list_temp_1.append(data['name'])
        list_temp_1.append(data['a2'])
        list_temp_1.append(data['a3'])
        list_temp_1.append(data['a4'])
        list_temp_1.append(data['a5'])
        list_temp_1.append(data['a6'])
        list_temp_1.append(data['a7'])
        list_1.append(list_temp_1)
        # 第二个csv
        list_temp_2 = []
        list_temp_2.append(data['guid'])
        list_temp_2.append(data['url'])
        list_temp_2.append(data['name'])
        list_temp_2.append(data['b1'])
        list_temp_2.append(data['b2'])
        list_temp_2.append(data['b3'])
        list_temp_2.append(data['b4'])
        list_temp_2.append(data['b5'])
        list_temp_2.append(data['b6'])
        list_temp_2.append(data['b7'])
        list_temp_2.append(data['b8'])
        list_temp_2.append(data['b9'])
        list_temp_2.append(data['b10'])
        list_temp_2.append(data['b11'])
        list_temp_2.append(data['b12'])
        list_temp_2.append(data['b13'])
        list_temp_2.append(data['b14'])
        list_2.append(list_temp_2)
        # 第三个csv
        list_temp_3 = []
        list_temp_3.append(data['guid'])
        list_temp_3.append(data['url'])
        list_temp_3.append(data['name'])
        list_temp_3.append(data['c1'])
        list_temp_3.append(data['c2'])
        list_temp_3.append(data['c3'])
        list_temp_3.append(data['c4'])
        list_temp_3.append(data['c5'])
        list_temp_3.append(data['c6'])
        list_3.append(list_temp_3)

    with open(base_csv_dir + "\\business_info.csv", "w", encoding="utf-8") as csvfile:
        header = []
        header.append("\"guid\"")
        header.append("\"url\"")
        header.append("\"Official name\"")
        header.append("\"Trading name\"")
        header.append("\"Business Code\"")
        header.append("\"Date Range\"")
        header.append("\"Tax authorities manage\"")
        header.append("\"Date of commencement of operation\"")
        header.append("\"Status\"")
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in list_1:
            writer.writerow(row)
    with open(base_csv_dir + "\\contact_inf.csv", "w", encoding="utf-8") as csvfile:
        header = []
        header.append("\"guid\"")
        header.append("\"url\"")
        header.append("\"Official name\"")
        header.append("\"Office address\"")
        header.append("\"Phone\"")
        header.append("\"Fax\"")
        header.append("\"Email\"")
        header.append("\"Website\"")
        header.append("\"Representative\"")
        header.append("\"Phone\"")
        header.append("\"Representative address\"")
        header.append("\"Manager\"")
        header.append("\"Phone Director\"")
        header.append("\"Address Director\"")
        header.append("\"Accountant\"")
        header.append("\"Phone accounting\"")
        header.append("\"Account address\"")
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in list_2:
            writer.writerow(row)
    with open(base_csv_dir + "\\industry_info.csv", "w", encoding="utf-8") as csvfile:
        header = []
        header.append("\"guid\"")
        header.append("\"url\"")
        header.append("\"Official name\"")
        header.append("\"Main job\"")
        header.append("\"Economic field\"")
        header.append("\"Type of economic\"")
        header.append("\"Type of organization\"")
        header.append("\"Class chapters\"")
        header.append("\"Item type\"")
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in list_3:
            writer.writerow(row)


if __name__ == "__main__":
    excel()
