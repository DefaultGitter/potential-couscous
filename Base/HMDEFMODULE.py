import random
from statistics import mean


def master(link: str):
    def maximum(rand_list: list):
        return max(rand_list)

    def minimum(rand_list: list):
        return min(rand_list)

    def avg(rand_list: list):
        return mean(rand_list)

    if "max" in link:
        return maximum
    elif "min" in link:
        return minimum
    elif "avg" in link:
        return avg


def action(argument: list, link):
    return link(argument)


def main():
    random_list = []
    for i in range(10):
        random_list.append(random.randint(-10, 10))
    print(f"List of random numbers: {random_list}")
    choice = input("This program can find minimum value, maximum value or average value."
                   "\n{}\n{}\n{}\nEnter your choice: ".format(
                    f"{' max ':|^11}",
                    f"{' min ':|^11}",
                    f"{' avg ':|^11}"))

    if choice != "exit":
        print(f"\n{choice} of random list is: {action(random_list, master(choice))}\n")
    else:
        exit("Program finished.")

    main()


main()
