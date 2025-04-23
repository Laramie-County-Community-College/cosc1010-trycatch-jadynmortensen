def steps_to_miles(stepCount):
    # if input is negative
    if stepCount < 0:
        # raise an error
        raise ValueError("Exception: Negative step count entered.")
    # otherwise
    miles = stepCount / 2000
    return miles
# Driver code
if __name__ == "__main__":
    try:
        # taking input from user
        stepCount = int(input())
        # call the function and print returned value
        print(f'{steps_to_miles(stepCount):.2f}')
    # print the error if occurred
    except ValueError as e:
        print(e)
        