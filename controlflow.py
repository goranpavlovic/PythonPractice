

# if else - grananja
# for / while

def is_grether_then(a: int, b: int) -> bool:
    if a > b:
        return True
    else:
        return False


def print_string_n_times_for_loop(value: str, times: int):
    for count in range(0, times):
        print(f"For loop: Printing {count}: {value}")


def print_string_n_times_while_loop(value: str, times: int):
    count = 0
    while count < times:

        if count == 1:
            count = count + 1
            continue

        print(f"While loop: Printing {count}: {value}")
        #count += 1
        count = count + 1

        if count == 3:
            break


def find_position_for(items: list, elem: str) -> str:
    for position in range(0, len(items)):
        if items[position] == elem:
            return position


def find_position_while(items: list, elem: str) -> str:
    position = 0
    while position < len(items):
        if items[position] == elem:
            return position
        position += 1
        
