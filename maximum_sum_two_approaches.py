from random import randint, seed
from timeit import default_timer as timer

infinity = float('inf')

def brute_force (array):
    maximum_sum = -infinity
    
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            current_sum = sum(array[i : j])
            maximum_sum = max(maximum_sum, current_sum)
    
    return maximum_sum

def dynamic_programming (array):
    current_sum = 0
    maximum_sum = -infinity
    
    for number in array:
        current_sum = max(current_sum + number, number)
        maximum_sum = max(maximum_sum, current_sum)
        
    return maximum_sum
    
def calculate_time (array, function):
    start = timer()
    result = function(array)
    end = timer()
    print('Solution obtained with', function.__name__, '=', result)
    print('Execution time using', function.__name__, '=', end - start, 'seconds')
    
def generate_random_array (length):
    seed()
    return [randint(-1000, 1000) for i in range(length)]
    
array = generate_random_array(1500)
print('Maximum sum for a array with length 1500')
calculate_time(array, brute_force)
calculate_time(array, dynamic_programming)