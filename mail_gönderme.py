import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import time
import random
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QHBoxLayout,QPushButton,QVBoxLayout,QTextEdit,QLabel

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.mail_address = QLineEdit()
        self.text_1 = QLabel("From :")
        self.parola = QLineEdit()
        self.text_2 = QLabel("Password :")
        self.parola.setEchoMode(QLineEdit.Password)
        self.mail_content = QTextEdit()
        self.text_3 = QLabel("Content :")
        self.mail_topic = QLineEdit()
        self.text_4 = QLabel("Topic :")
        self.button = QPushButton("Send")
        self.toto = QLineEdit()
        self.text_5 = QLabel("To")
        self.number = QLineEdit()
        self.text_6 = QLabel("How Many ?")
        self.text_area = QLabel("")

        
        h_box_1=QHBoxLayout()
        h_box_1.addWidget(self.text_1)
        h_box_1.addWidget(self.mail_address)
        h_box_2 = QHBoxLayout()
        h_box_2.addWidget((self.text_2))
        h_box_2.addWidget(self.parola)
        h_box_3 = QHBoxLayout()
        h_box_3.addWidget(self.text_4)
        h_box_3.addWidget(self.mail_topic)
        h_box_4=QHBoxLayout()
        h_box_4.addWidget(self.text_3)
        h_box_4.addWidget(self.mail_content)

        v_box_1 = QVBoxLayout()
        v_box_1.addStretch()
        v_box_1.addLayout(h_box_1)
        v_box_1.addLayout(h_box_2)
        v_box_1.addLayout(h_box_3)
        v_box_1.addLayout(h_box_4)
        v_box_1.addStretch()


        h_box_5 = QHBoxLayout()
        h_box_5.addWidget(self.text_5)
        h_box_5.addWidget(self.toto)
        h_box_6 = QHBoxLayout()
        h_box_6.addWidget(self.text_6)
        h_box_6.addWidget(self.number)

        v_box_2 = QVBoxLayout()
        v_box_2.addLayout(h_box_5)
        v_box_2.addLayout(h_box_6)

        v_box_3 = QVBoxLayout()
        v_box_3.addLayout(v_box_1)
        v_box_3.addStretch()
        v_box_3.addLayout(v_box_2)
        v_box_3.addStretch()
        v_box_3.addWidget(self.text_area)
        v_box_3.addWidget(self.button)
        self.setLayout(v_box_3)
        self.setWindowTitle("Gmail Spam Bot")
        self.button.clicked.connect(self.click)
        self.show()
    def click(self):
        for i in range(int(self.number.text())):
            message = MIMEMultipart()
            message["From"] = self.mail_address.text()
            message["To"] = self.toto.text()
            message["Subject"] = self.mail_topic.text() + " -" + str(i)

            texxt = self.mail_content.toPlainText()
            message_content = MIMEText(texxt,"plain")
            message.attach(message_content)

            #wait = random.randint(1, 5)
            #time.sleep(wait)

            try:
                mail = smtplib.SMTP("smtp.gmail.com",587)
                mail.ehlo()
                mail.starttls()
                mail.login(self.mail_address.text(),self.parola.text())
                mail.sendmail(message["From"],message["To"],message.as_string())
                self.text_area.setText("Mails has been sent succesfully...")
                mail.close()
            except:
                sys.stderr.write("There is a problem !!!")
                sys.stderr.flush()
                self.text_area.setText("There is a problem !!!")

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec())


