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
        list_temp_1.append(data['official_name'])
        list_temp_1.append(data['trading_name'])
        list_temp_1.append(data['business_code'])
        list_temp_1.append(data['date_range'])
        list_temp_1.append(data['tax_authorities_manage'])
        list_temp_1.append(data['date_of_commencement_of_operation'])
        list_temp_1.append(data['status'])
        list_1.append(list_temp_1)
        # 第二个csv
        list_temp_2 = []
        list_temp_2.append(data['guid'])
        list_temp_2.append(data['url'])
        list_temp_2.append(data['official_name'])
        list_temp_2.append(data['office_address'])
        list_temp_2.append(data['phone1'])
        list_temp_2.append(data['fax'])
        list_temp_2.append(data['email'])
        list_temp_2.append(data['website'])
        list_temp_2.append(data['representative'])
        list_temp_2.append(data['phone2'])
        list_temp_2.append(data['representative_address'])
        list_temp_2.append(data['manager'])
        list_temp_2.append(data['phone_director'])
        list_temp_2.append(data['address_director'])
        list_temp_2.append(data['accountant'])
        list_temp_2.append(data['phone_accounting'])
        list_temp_2.append(data['account_address'])
        list_2.append(list_temp_2)
        # 第三个csv
        list_temp_3 = []
        list_temp_3.append(data['guid'])
        list_temp_3.append(data['url'])
        list_temp_3.append(data['official_name'])
        list_temp_3.append(data['main_job'])
        list_temp_3.append(data['economic_field'])
        list_temp_3.append(data['type_of_economic'])
        list_temp_3.append(data['type_of_organization'])
        list_temp_3.append(data['class_chapters'])
        list_temp_3.append(data['item_type'])
        list_3.append(list_temp_3)

    with open(base_csv_dir + "\\business_info.csv", "w", encoding="utf-8") as csvfile:
        header = []
        header.append("guid")
        header.append("url")
        header.append("Official name")
        header.append("Trading name")
        header.append("Business Code")
        header.append("Date Range")
        header.append("Tax authorities manage")
        header.append("Date of commencement of operation")
        header.append("Status")
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in list_1:
            writer.writerow(row)
    with open(base_csv_dir + "\\contact_inf.csv", "w", encoding="utf-8") as csvfile:
        header = []
        header.append("guid")
        header.append("url")
        header.append("Official name")
        header.append("Office address")
        header.append("Phone")
        header.append("Fax")
        header.append("Email")
        header.append("Website")
        header.append("Representative")
        header.append("Phone")
        header.append("Representative address")
        header.append("Manager")
        header.append("Phone Director")
        header.append("Address Director")
        header.append("Accountant")
        header.append("Phone accounting")
        header.append("Account address")
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in list_2:
            writer.writerow(row)
    with open(base_csv_dir + "\\industry_info.csv", "w", encoding="utf-8") as csvfile:
        header = []
        header.append("guid")
        header.append("url")
        header.append("Official name")
        header.append("Main job")
        header.append("Economic field")
        header.append("Type of economic")
        header.append("Type of organization")
        header.append("Class chapters")
        header.append("Item type")
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in list_3:
            writer.writerow(row)


if __name__ == "__main__":
    excel()
