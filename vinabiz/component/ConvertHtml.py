import threading
import vinabiz.component.dbComponent as dbComponent
import requests
import os

base_html_dir = "F:\\vinabiz\\html"
base_resource_dir = "/Users/youzhihao/Downloads/vinabiz/content"


# 获取数据，并且过滤已经生成的
def get_data_list(min_id, max_id):
    file_name_list = os.listdir(base_html_dir)
    temp_list = []
    data_list = dbComponent.get_all_company_url_by_id(min_id, max_id)
    for data in data_list:
        file_name = data["guid"] + ".html"
        if file_name in file_name_list:
            continue
        temp_list.append(data)
    print("还是%d个html没生成" % temp_list.__len__())
    return temp_list


def convert_html(data):
    url = data['url']
    out_file_name = base_html_dir + "/" + data['guid'] + ".html"
    response = requests.get(url, timeout=5)
    content = str(response.content, encoding="utf-8")
    with open(out_file_name, "w",encoding="utf-8") as f:
        f.write(content)
        f.flush()
        f.close()


class myThread(threading.Thread):
    def __init__(self, data_list):
        threading.Thread.__init__(self)
        self.list = list

    def run(self):
        while list.__len__() > 0:
            try:
                data = list.pop()
                convert_html(data)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    list = get_data_list(1, 10000)
    myThread(list).start()
    myThread(list).start()
    myThread(list).start()
    myThread(list).start()
    myThread(list).start()
    myThread(list).start()
    myThread(list).start()
    myThread(list).start()
    myThread(list).start()
    myThread(list).start()
    myThread(list).start()
    myThread(list).start()
    myThread(list).start()

