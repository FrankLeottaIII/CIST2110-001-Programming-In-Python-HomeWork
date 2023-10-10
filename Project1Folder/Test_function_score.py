#testing out  test varible for adding to scorecard
SCORE = 0
test = 0
varible = 0
def testing(varible:int):
    global test
    test +=1
    print(test)
    return int(test + 1)

test = testing(varible)
test = testing(varible)

## I figured out why my score was not adding up, I was not calling the function correctly, I was calling it without a global varible