import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QLineEdit, QPushButton, QRadioButton, QCheckBox,
    QTextEdit, QVBoxLayout, QHBoxLayout, QComboBox,
    QListWidget, QGroupBox, QMessageBox
)


class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Manager")
        self.resize(700, 750)

        # Список для хранения созданных задач
        self.tasks = []

        # Центральный виджет главного окна
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Название задачи
        self.task_label = QLabel("Task:")
        self.task_edit = QLineEdit()
        self.task_edit.setPlaceholderText("Enter task name")

        # Описание задачи
        self.description_label = QLabel("Description:")
        self.description_edit = QTextEdit()
        self.description_edit.setPlaceholderText(
            "Enter task description"
        )

        # Приоритет задачи
        self.priority_label = QLabel("Priority:")

        self.low_radio = QRadioButton("Low")
        self.medium_radio = QRadioButton("Medium")
        self.high_radio = QRadioButton("High")

        # Дополнительные настройки
        self.important_check = QCheckBox("Important")
        self.notification_check = QCheckBox(
            "Send notification"
        )
        self.favorite_check = QCheckBox("Add to favorites")

        # Кнопки
        self.create_button = QPushButton("Create task")
        self.clear_button = QPushButton("Clear")
        self.delete_button = QPushButton("Delete last task")

        # Статус и счётчик
        self.status_label = QLabel("Status: Ready")
        self.count_label = QLabel("Created tasks: 0")

        # Фильтр задач по приоритету
        self.filter_label = QLabel("Filter by priority:")
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(
            ["All", "Low", "Medium", "High"]
        )

        # Список задач внутри окна
        self.task_list_label = QLabel("Created tasks:")
        self.task_list = QListWidget()

        # Основной layout
        main_layout = QVBoxLayout()

        # Строка названия задачи
        task_layout = QHBoxLayout()
        task_layout.addWidget(self.task_label)
        task_layout.addWidget(self.task_edit)

        # Группа переключателей приоритета
        priority_group = QGroupBox("Select priority")
        priority_layout = QHBoxLayout()
        priority_layout.addWidget(self.low_radio)
        priority_layout.addWidget(self.medium_radio)
        priority_layout.addWidget(self.high_radio)
        priority_group.setLayout(priority_layout)

        # Строка фильтра
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(self.filter_label)
        filter_layout.addWidget(self.filter_combo)

        # Строка кнопок
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.create_button)
        buttons_layout.addWidget(self.clear_button)
        buttons_layout.addWidget(self.delete_button)

        # Добавление элементов в основной layout
        main_layout.addWidget(QLabel("Create your task"))
        main_layout.addLayout(task_layout)
        main_layout.addWidget(self.description_label)
        main_layout.addWidget(self.description_edit)
        main_layout.addWidget(priority_group)
        main_layout.addWidget(self.important_check)
        main_layout.addWidget(self.notification_check)
        main_layout.addWidget(self.favorite_check)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.count_label)
        main_layout.addLayout(filter_layout)
        main_layout.addWidget(self.task_list_label)
        main_layout.addWidget(self.task_list)

        self.central_widget.setLayout(main_layout)

        # Подключение сигналов к обработчикам
        self.create_button.clicked.connect(self.create_task)
        self.clear_button.clicked.connect(self.clear_form)
        self.delete_button.clicked.connect(self.delete_last_task)
        self.filter_combo.currentTextChanged.connect(
            self.show_tasks
        )

    def create_task(self):
        # Получение данных из полей
        name = self.task_edit.text().strip()
        description = self.description_edit.toPlainText().strip()

        # Проверка названия задачи
        if not name:
            QMessageBox.warning(
                self, "Error", "Please enter a task name."
            )
            self.task_edit.setFocus()
            return

        # Проверка выбранного приоритета
        if self.low_radio.isChecked():
            priority = "Low"
        elif self.medium_radio.isChecked():
            priority = "Medium"
        elif self.high_radio.isChecked():
            priority = "High"
        else:
            QMessageBox.warning(
                self, "Error", "Please select a priority."
            )
            return

        # Получение дополнительных настроек
        important = self.important_check.isChecked()
        notification = self.notification_check.isChecked()
        favorite = self.favorite_check.isChecked()

        # Создание словаря с данными задачи
        task = {
            "name": name,
            "description": description,
            "priority": priority,
            "important": important,
            "notification": notification,
            "favorite": favorite
        }

        # Сохранение задачи в список
        self.tasks.append(task)

        # Обновление интерфейса
        self.show_tasks()
        self.count_label.setText(
            f"Created tasks: {len(self.tasks)}"
        )
        self.status_label.setText("Status: Task created")

        # Вывод информации о созданной задаче в консоль
        print("Task created:")
        print(f"Task: {name}")
        print(f"Description: {description}")
        print(f"Priority: {priority}")
        print(f"Important: {'Yes' if important else 'No'}")
        print(f"Send notification: {'Yes' if notification else 'No'}")
        print(f"Favorite: {'Yes' if favorite else 'No'}")
        print("-" * 30)

        self.clear_form()

    def show_tasks(self):
        # Получение выбранного фильтра
        selected_filter = self.filter_combo.currentText()

        self.task_list.clear()

        # Отображение задач с учётом фильтра
        for task in self.tasks:
            if (
                selected_filter != "All"
                and task["priority"] != selected_filter
            ):
                continue

            task_text = (
                f'{task["name"]} | Priority: {task["priority"]}'
            )

            if task["important"]:
                task_text += " | Important"

            if task["favorite"]:
                task_text += " | Favorite"

            self.task_list.addItem(task_text)

    def clear_form(self):
        # Очистка полей формы
        self.task_edit.clear()
        self.description_edit.clear()

        self.low_radio.setAutoExclusive(False)
        self.medium_radio.setAutoExclusive(False)
        self.high_radio.setAutoExclusive(False)

        self.low_radio.setChecked(False)
        self.medium_radio.setChecked(False)
        self.high_radio.setChecked(False)

        self.low_radio.setAutoExclusive(True)
        self.medium_radio.setAutoExclusive(True)
        self.high_radio.setAutoExclusive(True)

        self.important_check.setChecked(False)
        self.notification_check.setChecked(False)
        self.favorite_check.setChecked(False)

        self.status_label.setText("Status: Ready")

    def delete_last_task(self):
        # Проверка наличия задач
        if not self.tasks:
            QMessageBox.information(
                self, "Information", "There are no tasks to delete."
            )
            return

        # Удаление последней созданной задачи
        self.tasks.pop()

        self.show_tasks()
        self.count_label.setText(
            f"Created tasks: {len(self.tasks)}"
        )
        self.status_label.setText("Status: Last task deleted")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TaskManager()
    window.show()

    sys.exit(app.exec())
