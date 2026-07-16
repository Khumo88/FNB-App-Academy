# A countdown using while loop

count = 4

while count > 0:
    print(count)
    count = count - 1

print("Blast Off !!!")

# Building a simple rep counter

for rep in range(1, 4):
    print(f"This is rep no. {rep}")

# A guessing game

secret_word = "python"

while True:
    guess = input("Guess the programming language we are using: ").lower()
   
    if guess == secret_word:
        print("You guessed the correct language !!!!")
        break
    else:
        print("Incorrect guess try again !!!!!")

