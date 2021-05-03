def print_iteration():
    if not hasattr(print_iteration, "_number"):
        print_iteration._number = 0
    print(print_iteration._number)
    print_iteration._number += 1
    return print_iteration._number


if __name__ == "__main__":
    # while print_iteration() < 11:
    #     print_iteration()
    for index in range(0,10):
        # print_iteration._number = 64
        print_iteration()