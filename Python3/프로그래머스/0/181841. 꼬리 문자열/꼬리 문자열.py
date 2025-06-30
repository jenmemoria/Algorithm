def solution(str_list, ex):
    return "".join([char for char in str_list if ex not in char])