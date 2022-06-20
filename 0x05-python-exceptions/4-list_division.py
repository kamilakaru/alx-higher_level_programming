#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    i = 0
    for i in range(0, list_length):
        res = 0

        try:
            res = (my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by zero")
        except TypeError:
            print("wrong type")
        finally:
            pass
        result.append(res)
    return result
