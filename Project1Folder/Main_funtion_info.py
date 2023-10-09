### information about the main function##

global monkeys
monkeys = 5
def barrel_monkeys(varible):
    global monkeys
    if monkeys == 1:
        print("1 monkey in the barrel")
    else:
        print(monkeys, "monkeys in the barrel")
        monkeys -= 1
        barrel_monkeys(monkeys)
    return monkeys


def main():
    if __name__ == "__main__":
        barrel_monkeys(monkeys)
        main()