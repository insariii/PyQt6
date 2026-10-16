Task Manager

Это приложение для создания задач на PyQt6
Что можно сделать там :
Ввести название задачи и её описание
Выбрать приоритет: Low, Medium или High
Отметить Important, Send notification и Add to favorites
Создавать задачи и смотреть их в списке
Фильтровать задачи по приоритету
Очищать форму и удалять последнюю задачу

Для создания интерфейса я использовала QMainWindow, QWidget, QLabel, QLineEdit, QTextEdit, QRadioButton, QCheckBox, QPushButton, QComboBox и QListWidget
Для расположения элементов использовала QVBoxLayout и QHBoxLayout

Когда нажимаю Create task, программа проверяет название и выбранный приоритет. Если всё заполнено, задача добавляется в список. Также обновляются счётчик и статус
Кнопка Clear очищает форму, а Delete last task удаляет последнюю созданную задачу
Задачи хранятся в списке Python, поэтому после закрытибя программы они пропадают

Как запустить
Установить PyQt6
python3 -m pip install PyQt6
Запустить программу
python3 main.py
