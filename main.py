from io_data import *

def main(file_in):
    stock, hamsters_count, hamster_bst = input_data(file_in)

    total_hamsters = 0
    total_avarice = 0
    total_daily_norm = 0

    while total_hamsters < hamsters_count:
        current_hamster = hamster_bst.get_min_element().data
        total_daily_norm += current_hamster.daily_norm
        total_avarice += current_hamster.avarice

        if total_daily_norm + total_avarice*total_hamsters > stock:
            break

        hamster_bst.remove_min_element()
        total_hamsters += 1
    return total_hamsters


if __name__ == "__main__":
    file_in_1 = 'io/in/hamstr_1.in'
    file_in_2 = 'io/in/hamstr_2.in'
    file_in_3 = 'io/in/hamstr_3.in'
    file_out_1 = file_in_1.replace('in', 'out')
    file_out_2 = file_in_2.replace('in', 'out')
    file_out_3 = file_in_3.replace('in', 'out')

    result_1 = main(file_in_1)
    result_2 = main(file_in_2)
    result_3 = main(file_in_3)

    print(f'result 1 example: {result_1}')
    print(f'result 2 example: {result_2}')
    print(f'result 3 example: {result_3}')

    output_data(file_out_1, str(result_1))
    output_data(file_out_2, str(result_2))
    output_data(file_out_3, str(result_3))







