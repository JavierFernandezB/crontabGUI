import subprocess
import os

crontab_file_name = "/tmp/crontab_file_list"


class gui_inteface():
    def __init__(self):
        self.tableWidget.setColumnWidth(0, 110)
        self.tableWidget.setColumnWidth(1, 190)
        self.tableWidget.setColumnWidth(2, 50)
        self.tableWidget.setColumnWidth(3, 50)
        self.iconDelete = QtWidgets.QWidget().style().standardIcon(
            getattr(QtWidgets.QStyle, "SP_TrashIcon"))
        self.iconEdit = QtWidgets.QWidget().style().standardIcon(
            getattr(QtWidgets.QStyle, "SP_DialogOkButton"))


def clean_files() -> None:
    try:
        os.remove(f"{crontab_file_name}")
        os.remove("/tmp/clean_crons")
    except:
        print("dont exist")


def load_crons(self) -> None:
    self.clean_files()
    os.system(f"crontab -l > {self.crontab_file_name}")
    crons = []
    with open(f"{self.crontab_file_name}", "r") as f:
        lines = f.readlines()
        if(len(lines) != 0):
            for i in lines:
                if not i.startswith("#"):
                    i = i.replace("\n", "")
                    splited = i.split(" ")
                    if splited[0].startswith("@"):
                        crons.append([splited[0], " ".join(splited[1:])])
                    else:
                        crons.append(
                            [" ".join(splited[:5]), " ".join(splited[5:])])
    self.tableWidget.setRowCount(len(crons))
    for idx, item in enumerate(crons):
        # self.tableWidget.setItem(
        #     idx, 0, QtWidgets.QTableWidgetItem(str(idx)))
        self.tableWidget.setItem(
            idx, 1, QtWidgets.QTableWidgetItem(item[0]))
        self.tableWidget.setItem(
            idx, 2, QtWidgets.QTableWidgetItem(item[1]))
        self.tableWidget.setCellWidget(
            idx, 3, QtWidgets.QPushButton(self.iconEdit, ''))
        self.tableWidget.setCellWidget(
            idx, 4, QtWidgets.QPushButton(self.iconDelete, ''))


def save_crons(crons: [str]) -> int:
    clean_files()
    os.system(f"crontab -l > {crontab_file_name}")
    with open(f"{crontab_file_name}", "a") as f:
        for i in crons:
            f.write(i+"\n")
    return os.system(f"crontab {crontab_file_name}")


def delete_crontab(cron: str) -> None:
    clean_files()
    os.system(f"crontab -l > {crontab_file_name}")
    crons_list = []
    with open(f"{crontab_file_name}", "r") as f:
        for i in f.readlines():
            if not i.startswith("#"):
                if i.strip() != cron.strip():
                    crons_list.append(i)
    with open("/tmp/clean_crons", "w") as f:
        for i in crons_list:
            if i.strip() != cron.strip():
                f.write(i)

    os.system(f"crontab /tmp/clean_crons")


# class x:
#     self.reload_crons_btn.clicked.connect(self.load_crons)
#     self.crontab_file_name = "/tmp/crontab_file_list"
#     self.tableWidget.setColumnWidth(0, 110)
#     self.tableWidget.setColumnWidth(1, 190)
#     self.tableWidget.setColumnWidth(2, 48)
#     self.tableWidget.setColumnWidth(3, 48)
#     self.new_cron_time = ""
#     self.new_cront_job = ""
#     self.command_input.textChanged[str].connect(self.change_changed)

#     def clean_files(self) -> None:
#         try:
#             os.remove(f"{self.crontab_file_name}")
#             os.remove("/tmp/clean_crons")
#         except:
#             print("dont exist")

#     def load_crons(self) -> None:
#         self.clean_files()
#         os.system(f"crontab -l > {self.crontab_file_name}")
#         crons = []
#         with open(f"{self.crontab_file_name}", "r") as f:
#             lines = f.readlines()
#             if(len(lines) != 0):
#                 for i in lines:
#                     if not i.startswith("#"):
#                         i = i.replace("\n", "")
#                         splited = i.split(" ")
#                         if splited[0].startswith("@"):
#                             crons.append(
#                                 [splited[0], " ".join(splited[1:])])
#                         else:
#                             crons.append(
#                                 [" ".join(splited[:5]), " ".join(splited[5:])])
#         self.tableWidget.setRowCount(len(crons))
#         for idx, item in enumerate(crons):
#             self.tableWidget.setItem(
#                 idx, 0, QtWidgets.QTableWidgetItem(item[0]))
#             self.tableWidget.setItem(
#                 idx, 1, QtWidgets.QTableWidgetItem(item[1]))
#             self.tableWidget.setCellWidget(
#                 idx, 2, QtWidgets.QPushButton(self.iconEdit, ''))
#             self.tableWidget.setCellWidget(
#                 idx, 3, QtWidgets.QPushButton(self.iconDelete, ''))

#     def change_changed(self):
#         self.new_cront_job = self.command_input.text()
#         self.lineEdit.setText(f"{self.new_cron_time} {self.new_cront_job}")


def test_cron(cron: str) -> True or str:
    os.system('crontab -l > /tmp/goodcron')
    os.system(f'echo "{cron}" > /tmp/testcron')
    valid_cron = subprocess.Popen(
        ['crontab', '/tmp/testcron'], stderr=subprocess.PIPE)
    stderr = valid_cron.communicate()
    exit_code = valid_cron.wait()
    os.system('crontab /tmp/goodcron')
    if exit_code:
        error = " ".join(stderr[1].decode(
            'utf-8').split("\n")[0].split(' ')[1:])
        return error
    return True


print(test_cron('0 0 * * * echo $1'))
