import vinabiz.component.dbComponent as dbComponent
import os
import threading
import shutil

base_pdf_dir = "/Users/youzhihao/Downloads/vinabiz/pdf"
base_cmd_dir = "/Users/youzhihao/Downloads/vinabiz/wkhtmltopdf/"


def createCmdFile(min_id, max_id, thread_num):
    list = os.listdir(base_pdf_dir)
    if os.path.exists(base_cmd_dir):
        shutil.rmtree(base_cmd_dir)
    os.makedirs(base_cmd_dir)
    file_list = []
    index = 1
    while index <= thread_num:
        file_list.append(open(base_cmd_dir + "cmd%d" % index, "w"))
        index += 1
    count = 0
    for data in dbComponent.get_all_company_url_by_id(min_id, max_id):
        file_name = data['guid'] + ".pdf"
        if file_name in list:
            continue
        mod = count % thread_num
        cmd = "%s %s" % (data['url'], base_pdf_dir + "/" + file_name)
        file_list[mod].write(cmd + "\n")
        count += 1
    print("还需要生成%d个pdf" % count)


def get_cmd_list():
    cmd_list = []
    file_name_list = os.listdir(base_cmd_dir)
    for file_name in file_name_list:
        cmd_str = "wkhtmltopdf --margin-top 10mm  --margin-bottom 10mm --margin-left 10mm --margin-right 10mm --read-args-from-stdin < %s" % base_cmd_dir + file_name
        cmd_list.append(cmd_str)
    return cmd_list


class myThread(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.popen(self.cmd)


if __name__ == "__main__":
    createCmdFile(1, 10000, 15)
    for cmd in get_cmd_list():
        myThread(cmd).start()
    input()
