# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и
# статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False

    def mark_as_done(self):
        """Отмечает задачу как выполненную"""
        self.status = True

    def is_complete(self):
        """Проверяет, выполнена ли задача"""
        return self.status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Добавляет новую задачу."""
        self.tasks.append(task)

    def complete_task(self, index):
        """Отмечает задачу как выполненную по индексу."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_done()
        else:
            print(f'Задача с индексом {index} не найдена.')

    def get_current_tasks(self):
        """Возвращает список всех невыполненных задач."""
        current_tasks = [task for task in self.tasks if not task.is_complete()]
        return current_tasks

    def print_all_tasks(self):
        """Выводит все задачи с их статусом."""
        for i, task in enumerate(self.tasks):
            status = 'Выполнена' if task.is_complete() else 'Не выполнена'
            print(f'{i + 1}. Описание: {task.description}, Срок: {task.deadline}, Статус: {status}')

"""Создание менеджера задач"""
manager = TaskManager()

"""Добавление новых задач"""
task1 = Task('Написать отчет', '2024-01-03')
task2 = Task('Сделать презентацию', '2024-01-04')
task3 = Task('Сдать домашку', '2024-01-03')

manager.add_task(task1)
manager.add_task(task2)
manager.add_task(task3)

"""Отметка задачи как выполненной"""
manager.complete_task(0)  # Отметим первую задачу как выполненную
manager.complete_task(2)  # Отметим третью задачу как выполненную

"""Получение списка текущих (невыполненных) задач"""
current_tasks = manager.get_current_tasks()
print("Список невыполненных задач")
for task in current_tasks:
    print(f'Описание: {task.description}, Срок: {task.deadline}')

"""Просмотр всех задач со статусом"""
print("Список всех задач")
manager.print_all_tasks()