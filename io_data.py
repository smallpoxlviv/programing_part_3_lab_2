from bst import BST
from hamster import Hamster
import sys

def input_data(file_name):
    try:
        with open(file_name, 'r') as file:
            stock = int(file.readline())
            hamsters_count = int(file.readline())
            hamster_bst = BST(lambda hamster: (hamster.avarice, hamster.daily_norm))
            for line in file.readlines():
                daily_norm, avarice = line.split()
                hamster_bst.add(Hamster(int(daily_norm), int(avarice)))
        return stock, hamsters_count, hamster_bst
    except (FileNotFoundError):
        sys.exit(f'file "{file_name}" not found')
    except:
        sys.exit(f'check data in "{file_name}"')

def output_data(file_name, output):
    with open(file_name,'w') as file:
        file.write(str(output))