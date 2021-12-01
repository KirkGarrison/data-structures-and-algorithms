

def insertShiftArray(arr_list, n):
    split = len(arr_list)//2
    new_arr = arr_list[:split] + [n] + arr_list[split:]
    return new_arr







