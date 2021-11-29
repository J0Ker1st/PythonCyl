from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
# PyQt5 - библиотека оконных приложений
# QApplication - управляет потоком управления и основными настройками приложения с граф интер
# QWidget - класс является базовым классом всех объектов
# QLineEdit - виджет который разрешает вводить и редактировать одну строку текста
# QHBoxLayout и QVBoxLayout - классы компоновки которые выстраивают виджеты по горизонтали и вертикали
# QPushButton - виджет предоставляет командную строку

# Импорту модуля sys предоставляет системе особые параметры и функции
import sys

# Создаем класс который принимает аргумент QWidget в качестве параметра и инициализируем основное окно в подпрограмме класса
class Calculator(QWidget):
    # В подпрограмме __init__ есть вызов другой вызываемой подпрограммы это программы содержит настройки пользовательского интерфейса
    def __init__(self):
        super(Calculator, self).__init__()

        # Настройка заголовка
        self.setWindowTitle('calculator')


        self.input = QLineEdit()
        # Создание необходимых кнопок
        self.b_0 = QPushButton("0")
        self.b_1 = QPushButton("1")
        self.b_2 = QPushButton("2")
        self.b_3 = QPushButton("3")
        self.b_4 = QPushButton("4")
        self.b_5 = QPushButton("5")
        self.b_6 = QPushButton("6")
        self.b_7 = QPushButton("7")
        self.b_8 = QPushButton("8")
        self.b_9 = QPushButton("9")
        self.b_plus = QPushButton("+")
        self.b_minus = QPushButton("-")
        self.b_div = QPushButton("/")
        self.b_multiply = QPushButton("*")
        self.b_result = QPushButton("=")
        self.b_clear = QPushButton("clear")
        self.b_del = QPushButton("del")

        # Добавление кнопки в экземпляр QVBoxLayout
        self.main_box = QVBoxLayout()

        # Добавление кнопки в экземпляр QHBoxLayout
        self.input_box = QHBoxLayout()
        self.first_box = QHBoxLayout()
        self.result_box = QHBoxLayout()
        self.clear_box = QHBoxLayout()
        self.del_box = QHBoxLayout()


        self.main_box.addLayout(self.input_box)
        self.main_box.addLayout(self.first_box)
        self.main_box.addLayout(self.result_box)
        self.main_box.addLayout(self.clear_box)
        self.main_box.addLayout(self.del_box)

        # С помощью метода addWidget создаются и добавляются кнопки к макету
        self.input_box.addWidget(self.input)
        self.first_box.addWidget(self.b_0)
        self.first_box.addWidget(self.b_1)
        self.first_box.addWidget(self.b_2)
        self.first_box.addWidget(self.b_3)
        self.first_box.addWidget(self.b_4)
        self.first_box.addWidget(self.b_5)
        self.first_box.addWidget(self.b_6)
        self.first_box.addWidget(self.b_7)
        self.first_box.addWidget(self.b_8)
        self.first_box.addWidget(self.b_9)
        self.first_box.addWidget(self.b_plus)
        self.first_box.addWidget(self.b_minus)
        self.first_box.addWidget(self.b_div)
        self.first_box.addWidget(self.b_multiply)
        self.result_box.addWidget(self.b_result)
        self.clear_box.addWidget(self.b_clear)
        self.del_box.addWidget(self.b_del)



        # Добавление вкладки в виджет
        self.setLayout(self.main_box)

        # Добавление действия к каждой кнопке
        self.b_0.clicked.connect(lambda: self._addNum('0'))
        self.b_1.clicked.connect(lambda: self._addNum('1'))
        self.b_2.clicked.connect(lambda: self._addNum('2'))
        self.b_3.clicked.connect(lambda: self._addNum('3'))
        self.b_4.clicked.connect(lambda: self._addNum('4'))
        self.b_5.clicked.connect(lambda: self._addNum('5'))
        self.b_6.clicked.connect(lambda: self._addNum('6'))
        self.b_7.clicked.connect(lambda: self._addNum('7'))
        self.b_8.clicked.connect(lambda: self._addNum('8'))
        self.b_9.clicked.connect(lambda: self._addNum('9'))
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_div.clicked.connect(lambda: self._operation("/"))
        self.b_multiply.clicked.connect(lambda: self._operation("*"))
        self.b_result.clicked.connect(self._result)
        self.b_clear.clicked.connect(self._clear)
        self.b_del.clicked.connect(self._del)


    # Функция позволяет вводить числа в калькулятор и видеть их на экране
    def _addNum(self, param):
        line = self.input.text()
        self.input.setText(line + param)


    def _operation(self, op):
        self.num1 = int(self.input.text())
        self.op = op
        self.input.setText('')

    # Функция для производа различных арифметических действий
    def _result(self):
        self.num2 = int(self.input.text())
        self.input.setText('')
        if self.op == "+":
            self.input.setText(str(self.num1 + self.num2))
        elif self.op == "-":
            self.input.setText(str(self.num1 - self.num2))
        elif self.op == "/":
            self.input.setText(str(self.num1 / self.num2))
        elif self.op == "*":
            self.input.setText(str(self.num1 * self.num2))


    # Очистка текста метки
    def _clear(self):
        self.input.setText('')

    # Очистка одной цифры
    def _del(self):
        line = self.input.text()
        self.input.setText(line[:len(line)-1])




# Создание объекта приложения, в объект приложения необходимо передавать списки аргументов
app = QApplication(sys.argv)

# Создаем виджет
win = Calculator()
# Чтобы его увидел пользователь используем метод show
win.show()
# Командой app.exec - запускается приложение, а командой sys.exit обеспечивается чистый выход
sys.exit(app.exec_())
