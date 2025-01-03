### Как использовать этот код

#### Создание менеджера задач:
```python
manager = TaskManager()
```
#### Добавление новых задач:
```python
task1 = Task('Написать отчет', '2024-01-03')
task2 = Task('Сделать презентацию', '2024-01-04')
task3 = Task('Сделать презентацию', '2024-01-03')
manager.add_task(task1)
manager.add_task(task2)
manager.add_task(task3)
```
#### Отметка задачи как выполненной:
```python
manager.complete_task(0)  # Отметим первую задачу как выполненную
```
#### Получение списка текущих (невыполненных) задач:
```python
current_tasks = manager.get_current_tasks()
for task in current_tasks:
    print(f'Описание: {task.description}, Срок: {task.due_date}')
```
#### Просмотр всех задач со статусом:
```python
manager.list_all_tasks()
```