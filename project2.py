import random
number_to_guess = random.randint(1,100)
count = 0
while True:
    try:
     guess = int(input("guess your number -->"))
     count+=1
     if guess < number_to_guess:
      print("too low")
     elif guess > number_to_guess:
      print("too high")
     else:
      print("congratulations! you did it in -->" , count) 
      break
    except ValueError:
     print("enter valid value!")