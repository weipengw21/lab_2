def display_main_menu():
    print('Enter some numbers separated by commas (e.g. 5,67, 32)')


def get_user_input():
    num_list = []

    str = input()

    str_list = str.split(",")

    for item in str_list:
        num_list.append(int(item))

    return num_list


def main():
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print(str(type(num_list[0])))

if __name__ == "__main__":
    main()
