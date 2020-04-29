import math

for i in range(10):
    try:
        input_number = input("write a number: \n")
        if input_number == 'quit':
            break
        result = 1/math.log(float(input_number))
        print('log is', result)
    # except ValueError:
    except Exception:
        print('ValueError: input is invalid')
    finally:
        print('最终结果')
