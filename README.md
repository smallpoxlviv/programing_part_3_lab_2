# programing_part_3 lab_2 - "Hamsters"
### main.py

Ініціалізуємо змінні:
```python
file_in = 'io/in/hamstr_1.in' 
```
```python
stock, hamsters_count, hamster_bst = input_data(file_in)
```
### io_data.py
Створюємо двійкове дерево, де значення порівнюються за "жадністю", в першу чергу, і 
"денною нормою":
```python
def input_data(file_name):  
    with open(file_name, 'r') as file:
        stock = int(file.readline())
        hamsters_count = int(file.readline())
        hamster_bst = BST(lambda hamster: (hamster.avarice, hamster.daily_norm))
        for line in file.readlines():
            daily_norm, avarice = line.split()
            hamster_bst.add(Hamster(int(daily_norm), int(avarice)))
    return stock, hamsters_count, hamster_bst
```
### main.py
Шукаємо найменший елемент дерева:
```python
total_hamsters = 0
total_avarice = 0
total_daily_norm = 0

while total_hamsters < hamsters_count:
    current_hamster = hamster_bst.get_min_element().data
```
Додаємо до загальної кількості споживаної хом'яками норми та до загальної "жадності" дані поточного хом'яка:
```python
    total_daily_norm += current_hamster.daily_norm
    total_avarice += current_hamster.avarice
```
Виходимо з циклу, якщо загальна споживана їжа перевищує запас,
якщо ні - видаляємо поточного (мінімального) хом'яка з дерева:
```python
    if total_daily_norm + total_avarice*total_hamsters > stock:
        break

    hamster_bst.remove_min_element()
    total_hamsters += 1
```
Виводимо результат:
```python
file_out = file_in.replace('in', 'out')
```
```python
print(total_hamsters)
output_data(file_out, str(total_hamsters))
```
## Installation
Copy repository with command:                                                         
`git clone https://github.com/smallpoxlviv/programing_part_3_lab_2.git`
or another method.                        
To run script, enter this command in root directory: `python main.py`      
To run unit tests, enter this command in root directory: `python test.py`
###  
[Instagam](https://www.instagram.com/logic_bomb.exe/)