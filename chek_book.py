import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QLineEdit, QPushButton, QListWidget,
                             QVBoxLayout, QHBoxLayout, QMessageBox)

class MyNotes(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.contacts = []
        
    def initUI(self):
        # Настройка главного окна
        self.setWindowTitle('Записная книжка')
        self.setGeometry(300, 300, 400, 300)
        
        # Создание виджетов
        self.contactName = QLineEdit()
        self.contactName.setPlaceholderText('Введите имя')
        
        self.contactNumber = QLineEdit()
        self.contactNumber.setPlaceholderText('Введите телефон')
        
        self.addContactBtn = QPushButton('Добавить контакт')
        self.addContactBtn.clicked.connect(self.add_contact)
        
        self.contactList = QListWidget()
        
        # Создание layout
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel('Имя:'))
        input_layout.addWidget(self.contactName)
        
        number_layout = QHBoxLayout()
        number_layout.addWidget(QLabel('Телефон:'))
        number_layout.addWidget(self.contactNumber)
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(number_layout)
        main_layout.addWidget(self.addContactBtn)
        main_layout.addWidget(QLabel('Список контактов:'))
        main_layout.addWidget(self.contactList)
        
        self.setLayout(main_layout)
    
    def add_contact(self):
        name = self.contactName.text().strip()
        number = self.contactNumber.text().strip()
        
        if not name or not number:
            QMessageBox.warning(self, 'Ошибка', 'Заполните все поля!')
            return
            
        contact = f"{name}: {number}"
        self.contacts.append(contact)
        self.contactList.addItem(contact)
        
        # Очистка полей ввода
        self.contactName.clear()
        self.contactNumber.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec_())