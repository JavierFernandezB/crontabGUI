Q='utf-8'
P='crontab'
O=False
N=getattr
L=open
J='\n'
G=None
A=' '
F=''
D=True
C='Frame'
import subprocess as I
from PyQt5 import QtCore as E,QtGui,QtWidgets as B
import os as H
class R:
	def setupUi(A,Frame):F=Frame;F.setObjectName(C);F.setEnabled(D);F.setFixedSize(480,640);A.label=B.QLabel(F);A.label.setGeometry(E.QRect(200,10,91,31));A.label.setObjectName('label');A.save_button=B.QPushButton(F);A.save_button.setGeometry(E.QRect(270,590,80,23));A.save_button.setObjectName('save_button');A.cancel_button=B.QPushButton(F);A.cancel_button.setGeometry(E.QRect(360,590,80,23));A.cancel_button.setObjectName('cancel_button');A.frame=B.QFrame(F);A.frame.setGeometry(E.QRect(20,290,421,261));A.frame.setStyleSheet('#Frame{border:"5px solid black"}');A.frame.setFrameShape(B.QFrame.StyledPanel);A.frame.setFrameShadow(B.QFrame.Raised);A.frame.setObjectName('frame');A.horizontalLayoutWidget=B.QWidget(A.frame);A.horizontalLayoutWidget.setGeometry(E.QRect(20,60,311,41));A.horizontalLayoutWidget.setObjectName('horizontalLayoutWidget');A.horizontalLayout=B.QHBoxLayout(A.horizontalLayoutWidget);A.horizontalLayout.setContentsMargins(0,0,0,0);A.horizontalLayout.setObjectName('horizontalLayout');A.minute_input=B.QLineEdit(A.horizontalLayoutWidget);A.minute_input.setObjectName('minute_input');A.horizontalLayout.addWidget(A.minute_input);A.hour_input=B.QLineEdit(A.horizontalLayoutWidget);A.hour_input.setObjectName('hour_input');A.horizontalLayout.addWidget(A.hour_input);A.day_input=B.QLineEdit(A.horizontalLayoutWidget);A.day_input.setObjectName('day_input');A.horizontalLayout.addWidget(A.day_input);A.month_input=B.QLineEdit(A.horizontalLayoutWidget);A.month_input.setObjectName('month_input');A.horizontalLayout.addWidget(A.month_input);A.week_input=B.QLineEdit(A.horizontalLayoutWidget);A.week_input.setObjectName('week_input');A.horizontalLayout.addWidget(A.week_input);A.horizontalLayoutWidget_2=B.QWidget(A.frame);A.horizontalLayoutWidget_2.setGeometry(E.QRect(20,40,311,21));A.horizontalLayoutWidget_2.setObjectName('horizontalLayoutWidget_2');A.horizontalLayout_2=B.QHBoxLayout(A.horizontalLayoutWidget_2);A.horizontalLayout_2.setContentsMargins(0,0,0,0);A.horizontalLayout_2.setObjectName('horizontalLayout_2');A.label_6=B.QLabel(A.horizontalLayoutWidget_2);A.label_6.setObjectName('label_6');A.horizontalLayout_2.addWidget(A.label_6);A.label_5=B.QLabel(A.horizontalLayoutWidget_2);A.label_5.setObjectName('label_5');A.horizontalLayout_2.addWidget(A.label_5);A.label_4=B.QLabel(A.horizontalLayoutWidget_2);A.label_4.setObjectName('label_4');A.horizontalLayout_2.addWidget(A.label_4);A.label_3=B.QLabel(A.horizontalLayoutWidget_2);A.label_3.setObjectName('label_3');A.horizontalLayout_2.addWidget(A.label_3);A.label_2=B.QLabel(A.horizontalLayoutWidget_2);A.label_2.setObjectName('label_2');A.horizontalLayout_2.addWidget(A.label_2);A.add_button=B.QPushButton(A.frame);A.add_button.setGeometry(E.QRect(340,70,71,23));A.add_button.setObjectName('add_button');A.label_7=B.QLabel(A.frame);A.label_7.setGeometry(E.QRect(20,100,81,31));A.label_7.setObjectName('label_7');A.command_input=B.QLineEdit(A.frame);A.command_input.setGeometry(E.QRect(20,130,311,31));A.command_input.setObjectName('command_input');A.label_8=B.QLabel(A.frame);A.label_8.setGeometry(E.QRect(20,170,81,31));A.label_8.setObjectName('label_8');A.lineEdit=B.QLineEdit(A.frame);A.lineEdit.setGeometry(E.QRect(20,210,311,31));A.lineEdit.setReadOnly(D);A.lineEdit.setObjectName('lineEdit');A.pushButton_7=B.QPushButton(A.frame);A.pushButton_7.setGeometry(E.QRect(340,210,80,23));A.pushButton_7.setObjectName('pushButton_7');A.horizontalLayoutWidget_3=B.QWidget(A.frame);A.horizontalLayoutWidget_3.setGeometry(E.QRect(20,0,392,31));A.horizontalLayoutWidget_3.setObjectName('horizontalLayoutWidget_3');A.horizontalLayout_3=B.QHBoxLayout(A.horizontalLayoutWidget_3);A.horizontalLayout_3.setSizeConstraint(B.QLayout.SetDefaultConstraint);A.horizontalLayout_3.setContentsMargins(0,0,0,0);A.horizontalLayout_3.setObjectName('horizontalLayout_3');A.startup=B.QPushButton(A.horizontalLayoutWidget_3);A.startup.setMaximumSize(E.QSize(60,23));A.startup.setCheckable(D);A.startup.setAutoExclusive(D);A.startup.setDefault(O);A.startup.setObjectName('startup');A.horizontalLayout_3.addWidget(A.startup);A.hourly=B.QPushButton(A.horizontalLayoutWidget_3);A.hourly.setMaximumSize(E.QSize(60,23));A.hourly.setCheckable(D);A.hourly.setAutoExclusive(D);A.hourly.setObjectName('hourly');A.horizontalLayout_3.addWidget(A.hourly);A.daily=B.QPushButton(A.horizontalLayoutWidget_3);A.daily.setMaximumSize(E.QSize(60,23));A.daily.setCheckable(D);A.daily.setAutoExclusive(D);A.daily.setObjectName('daily');A.horizontalLayout_3.addWidget(A.daily);A.weekly=B.QPushButton(A.horizontalLayoutWidget_3);A.weekly.setMaximumSize(E.QSize(60,23));A.weekly.setCheckable(D);A.weekly.setAutoExclusive(D);A.weekly.setObjectName('weekly');A.horizontalLayout_3.addWidget(A.weekly,0,E.Qt.AlignLeft);A.monthly=B.QPushButton(A.horizontalLayoutWidget_3);A.monthly.setMaximumSize(E.QSize(60,23));A.monthly.setCheckable(D);A.monthly.setAutoExclusive(D);A.monthly.setObjectName('monthly');A.horizontalLayout_3.addWidget(A.monthly);A.yearly=B.QPushButton(A.horizontalLayoutWidget_3);A.yearly.setMaximumSize(E.QSize(60,23));A.yearly.setCheckable(D);A.yearly.setAutoExclusive(D);A.yearly.setObjectName('yearly');A.horizontalLayout_3.addWidget(A.yearly);A.tableWidget=B.QTableWidget(F);A.tableWidget.setGeometry(E.QRect(30,50,411,192));A.tableWidget.setMinimumSize(E.QSize(411,192));A.tableWidget.setMaximumSize(E.QSize(411,192));A.tableWidget.setHorizontalScrollBarPolicy(E.Qt.ScrollBarAlwaysOff);A.tableWidget.setSizeAdjustPolicy(B.QAbstractScrollArea.AdjustIgnored);A.tableWidget.setEditTriggers(B.QAbstractItemView.NoEditTriggers);A.tableWidget.setSelectionBehavior(B.QAbstractItemView.SelectRows);A.tableWidget.setWordWrap(D);A.tableWidget.setObjectName('tableWidget');A.tableWidget.setColumnCount(4);A.tableWidget.setRowCount(0);G=B.QTableWidgetItem();A.tableWidget.setVerticalHeaderItem(0,G);G=B.QTableWidgetItem();A.tableWidget.setHorizontalHeaderItem(0,G);G=B.QTableWidgetItem();A.tableWidget.setHorizontalHeaderItem(1,G);G=B.QTableWidgetItem();A.tableWidget.setHorizontalHeaderItem(2,G);G=B.QTableWidgetItem();A.tableWidget.setHorizontalHeaderItem(3,G);G=B.QTableWidgetItem();A.tableWidget.setItem(0,3,G);A.horizontalLayoutWidget_4=B.QWidget(F);A.horizontalLayoutWidget_4.setGeometry(E.QRect(130,250,201,31));A.horizontalLayoutWidget_4.setObjectName('horizontalLayoutWidget_4');A.horizontalLayout_4=B.QHBoxLayout(A.horizontalLayoutWidget_4);A.horizontalLayout_4.setContentsMargins(0,0,0,0);A.horizontalLayout_4.setObjectName('horizontalLayout_4');A.pushButton_8=B.QPushButton(A.horizontalLayoutWidget_4);A.pushButton_8.setObjectName('pushButton_8');A.horizontalLayout_4.addWidget(A.pushButton_8);H=B.QSpacerItem(40,20,B.QSizePolicy.Expanding,B.QSizePolicy.Minimum);A.horizontalLayout_4.addItem(H);A.reload_crons_btn=B.QPushButton(A.horizontalLayoutWidget_4);A.reload_crons_btn.setObjectName('reload_crons_btn');A.horizontalLayout_4.addWidget(A.reload_crons_btn);A.retranslateUi(F);E.QMetaObject.connectSlotsByName(F)
	def retranslateUi(A,Frame):H='*';D=E.QCoreApplication.translate;Frame.setWindowTitle(D(C,'Crontab GUI'));A.label.setText(D(C,'Crontab-GUI'));A.save_button.setText(D(C,'Save'));A.cancel_button.setText(D(C,'Close'));A.minute_input.setText(D(C,H));A.hour_input.setText(D(C,H));A.day_input.setText(D(C,H));A.month_input.setText(D(C,H));A.week_input.setText(D(C,H));A.label_6.setText(D(C,' Minute'));A.label_5.setText(D(C,' Hour'));A.label_4.setText(D(C,' Day'));A.label_3.setText(D(C,' Month'));A.label_2.setText(D(C,' Week'));A.add_button.setText(D(C,'Set'));A.label_7.setText(D(C,'Command: '));A.label_8.setText(D(C,'Job Preview:'));A.pushButton_7.setText(D(C,'Apply'));A.startup.setText(D(C,'Startup'));A.hourly.setText(D(C,'Hourly'));A.daily.setText(D(C,'Daily'));A.weekly.setText(D(C,'Weekly'));A.monthly.setText(D(C,'Monthly'));A.yearly.setText(D(C,'Yearly'));G=A.tableWidget.horizontalHeaderItem(0);G.setText(D(C,'Time'));G=A.tableWidget.horizontalHeaderItem(1);G.setText(D(C,'Command'));G=A.tableWidget.horizontalHeaderItem(2);G.setText(D(C,'Edit'));G=A.tableWidget.horizontalHeaderItem(3);G.setText(D(C,'Delete'));I=A.tableWidget.isSortingEnabled();A.tableWidget.setSortingEnabled(O);A.tableWidget.setSortingEnabled(I);A.pushButton_8.setText(D(C,'BackUp'));A.reload_crons_btn.setText(D(C,'ReloadCrons'));'\n        Custom section\n        ';A.cron_list=[];A.iconDelete=B.QWidget().style().standardIcon(N(B.QStyle,'SP_TrashIcon'));A.iconEdit=B.QWidget().style().standardIcon(N(B.QStyle,'SP_DialogOkButton'));A.reload_crons_btn.clicked.connect(A.load_crons);A.crontab_file_name='/tmp/crontab_file_list';A.tableWidget.setColumnWidth(0,110);A.tableWidget.setColumnWidth(1,190);A.tableWidget.setColumnWidth(2,48);A.tableWidget.setColumnWidth(3,48);A.new_cron_time=F;A.new_cront_job=F;A.command_input.textChanged.connect(lambda:A.changed_cron(F));A.startup.clicked.connect(lambda:A.changed_cron('@reboot'));A.yearly.clicked.connect(lambda:A.changed_cron('@yearly'));A.monthly.clicked.connect(lambda:A.changed_cron('@monthly'));A.weekly.clicked.connect(lambda:A.changed_cron('@weekly'));A.daily.clicked.connect(lambda:A.changed_cron('@daily'));A.hourly.clicked.connect(lambda:A.changed_cron('@hourly'));A.add_button.clicked.connect(A.set_custom_time);A.cancel_button.clicked.connect(K.exit);A.pushButton_7.clicked.connect(A.handle_add_cron_button);A.save_button.clicked.connect(A.save_crons_to_file);A.pushButton_8.clicked.connect(A.back_up_crons);A.clean_files()
	def clean_files(A):
		try:H.remove(f"{A.crontab_file_name}");H.remove('/tmp/clean_crons')
		except:print('dont exist')
	def add_crons_new(A,crons):
		for D in crons:C=A.tableWidget.rowCount();A.cron_list.append(D);A.tableWidget.setRowCount(C+1);A.tableWidget.setItem(C,0,B.QTableWidgetItem(D[0]));A.tableWidget.setItem(C,1,B.QTableWidgetItem(D[1]));A.tableWidget.setCellWidget(C,2,B.QPushButton(A.iconEdit,F));A.delete=B.QPushButton(A.iconDelete,F);A.delete.clicked.connect(lambda:A.remove_cron(C));A.tableWidget.setCellWidget(C,3,A.delete)
	def handle_add_cron_button(C):
		H=C.lineEdit.text();E=F
		if C.lineEdit.text().startswith('@'):E=C.lineEdit.text().split(A)[0]
		else:E=A.join([C.minute_input.text(),C.hour_input.text(),C.day_input.text(),C.month_input.text(),C.week_input.text()])
		I=C.command_input.text()
		if H==F or I==F:return
		J=C.test_cron(H)
		if J==D:C.add_crons_new([[E,I]])
		else:B.QMessageBox.warning(G,'Syntax Error',J)
	def load_crons(C):
		if C.cron_list:
			M=B.QMessageBox.warning(G,'Unchanged crons will be deleted','this is going to load only the crons from the file',B.QMessageBox.StandardButton.Ok|B.QMessageBox.StandardButton.Cancel)
			if M!=B.QMessageBox.StandardButton.Ok:return
		C.clean_files();H.system(f"crontab -l > {C.crontab_file_name}");E=[]
		with L(f"{C.crontab_file_name}",'r')as N:
			K=N.readlines()
			if len(K)==0:return
			for I in K:
				if I.startswith('#'):continue
				I=I.replace(J,F);D=I.split(A)
				if D[0].startswith('@'):E.append([D[0],A.join(D[1:])])
				elif D[0]!=F:E.append([A.join(D[:5]),A.join(D[5:])])
		if not E:B.QMessageBox.information(G,'No crons','this user has no crons');return
		C.clear_crons_gui();C.add_crons_new(E)
	def changed_cron(A,time=F):
		B=time;A.new_cront_job=A.command_input.text()
		if B!=F and B!=A.new_cron_time:A.new_cron_time=B
		A.lineEdit.setText(f"{A.new_cron_time} {A.new_cront_job}")
	def set_custom_time(B):C=A.join([B.minute_input.text(),B.hour_input.text(),B.day_input.text(),B.week_input.text(),B.month_input.text()]);B.changed_cron(C)
	def test_cron(G,cron):
		H.system('crontab -l > /tmp/goodcron');H.system(f'echo "{cron}" > /tmp/testcron');B=I.Popen([P,'/tmp/testcron'],stderr=I.PIPE);C=B.communicate();E=B.wait();H.system('crontab /tmp/goodcron')
		if E:F=A.join(C[1].decode(Q).split(J)[0].split(A)[1:]);return F
		return D
	def remove_cron(A,row):A.tableWidget.removeRow(row);A.cron_list.pop(row)
	def clear_crons_gui(A):A.cron_list=[];A.tableWidget.setRowCount(0)
	def save_crons_to_file(C):
		with L(C.crontab_file_name,'w')as D:
			if C.cron_list:
				for H in C.cron_list:D.write(A.join([*(H)])+J)
			else:D.write(F)
		E=I.Popen([P,C.crontab_file_name],stderr=I.PIPE);K=E.communicate();M=E.wait()
		if M:B.QMessageBox.warning(G,'Error saving file',K[1].decode(Q));return
		B.QMessageBox.information(G,'Saved correctly','crons saved')
	def back_up_crons(C):
		D=B.QFileDialog.Options();E,K=B.QFileDialog.getSaveFileName(G,'QFileDialog.getSaveFileName()',F,'All Files (*);;Text Files (*.txt)',options=D)
		try:
			with L(E,'w')as H:
				for I in C.cron_list:H.write(A.join([*(I)])+J)
			B.QMessageBox.information(G,'Backup Saved','Backup saved Correctly')
		except PermissionError:B.QMessageBox.warning(G,'No permisions','this user dont have permisions to save the file here')
		except:B.QMessageBox.warning(G,'Error','Error was found cant save the file')
if __name__=='__main__':import sys as K;S=B.QApplication(K.argv);M=B.QFrame();T=R();T.setupUi(M);M.show();K.exit(S.exec_())