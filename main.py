# Необходимо реализовать игру «Проверка на чётность». Суть игры в следующем: пользователю показывается случайное число. И ему нужно ответить yes, если число чётное, или no — если нечётное:

# Welcome to the Brain Games!
# May I have your name? Bill
# Hello, Bill!
# Answer "yes" if the number is even, otherwise answer "no".
# Question: 15
# Your answer: yes
# В случае, если пользователь даст неверный ответ, необходимо завершить игру и вывести сообщение:

# 'yes' is wrong answer ;(. Correct answer was 'no'.
# Let's try again, Bill!
# В случае, если пользователь ввел верный ответ, нужно отобразить следующее:

# Correct!
# Далее нужно приступить к следующему числу.

# Пользователь должен дать правильный ответ на три вопроса подряд. После успешной игры нужно вывести:

# Congratulations, Bill!
# Вывод должен получиться следующий:

# brain-even

# Welcome to the Brain Games!
# May I have your name? Sam
# Hello, Sam!
# Answer "yes" if the number is even, otherwise answer "no".
# Question: 15
# Your answer: no
# Correct!
# Question: 6
# Your answer: yes
# Correct!
# Question: 7
# Your answer: no
# Correct!
# Congratulations, Sam!
# Любой некорректный ввод считается ошибкой, например, n, и равносилен неправильному ответу.




# 1. Импортируем модуль рандом и конкретно функцию рандинт
# 2. Создаем функцию сравнения ответа
# 3. Создаем функцию проверки чет/нечет

import random
from random import randint

def comparison_of_the_response(answer):
  if answer == 'yes':
    return 'no'
  elif answer == 'no':
    return 'yes'

def even_or_not(random_number):
  a = random_number
  b = 2
  c = a % b
  if c == 0:
    return True
  else:
    return False

greeting = 'Welcome to the Brain Games!'
print(greeting)

name_question = input('May I have your name? ')
print('Hello, ' + name_question + '!')

task = 'Answer "yes" if the number is even, otherwise answer "no".'
print(task)

random_number = randint(1, 100)
print(f"Question: {random_number}")

answer = input('Your answer: ')

if even_or_not(random_number) is True:
  print("Correct!")
elif even_or_not(random_number) is False:
  opposite_answer = comparison_of_the_response(answer)
  print(f"'{answer}' is wrong answer ;(. Correct answer was '{opposite_answer}'.")