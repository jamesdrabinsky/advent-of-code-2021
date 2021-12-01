fp = 'advent_of_code_2021/2015_example/input.txt'

def get_floor():
    return sum(1 if i == '(' else -1 for i in open(fp).read())
    
get_floor()