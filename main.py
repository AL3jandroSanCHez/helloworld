print("Hello, world!!!")
def fibonacci_numbers(size):
  num1 = 0
  num2 = 1
  fibonacci_list = []
  while len(fibonacci_list) < size:
    fibonacci_sequence = num1+num2
    fibonacci_list.append(num2)
    num1 = num2
    num2 = fibonacci_sequence

  return fibonacci_list

print("Fibonacci numbers")
print(fibonacci_numbers(5))
print(fibonacci_numbers(10))



def divisors(user_number):
  possible_divisors = range(1, user_number+1)
  divisors_list = []
  for number in possible_divisors:
    if user_number%number == 0:
      divisors_list.append(number)
  return divisors_list

print("Devisors of 2")
print(divisors(2))
print("Devisors of 20")
print(divisors(20))
print("Devisors of 230")
print(divisors(230))




