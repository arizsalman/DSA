
def func(num_final):
    seem = set()
    for i in num_final:
        if i in seem:
            return True
        else:
            seem.add(i)
    return False


num_final = []
while True:
    nums = input("Enter your number & Exit Type 'done':")
    if nums.strip().lower() == "done":
        break
    try:
        value = int(nums)
        print(f'Your entered {value}')
    except ValueError:
        print("Please Enter in valiad Value")

    num_final.append(value)
    print(f'Your Value {num_final}')

    print(func(num_final))

    if func(num_final):
        print(f'Duplicate Found ')
    else:
        print(f' No Duplicate')
