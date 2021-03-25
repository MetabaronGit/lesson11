def sum_list(my_list):
    result = 0.0

    for item in my_list:
        try:
            result += float(item)
        except:
            continue

    return result


test = [1, 'asda', {'zvire': 'kocka'}, '3.0', 2.0, [], '\\n', '4']
print(sum_list(test))