def get_max(numbers:list[float]) -> float:
    if len(numbers) == 0:
        raise Exception('the list is empty')
    
    result = number[0]

    for number in numbers:
        if number > result:
            result = number

    return result
