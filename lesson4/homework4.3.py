
import random
numbers = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
new_list = [numbers[0], numbers[2], numbers[-2]]
print(numbers)
print(new_list)
