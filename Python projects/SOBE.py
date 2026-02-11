import time
import random

score = 0

def main():
    while True:

        global score

        random1 = random.randint(1, 100)
        random2 = random.randint(1, 100)
        print(f"A addition game point: {score}")
        print(f" what is the sum of {random1} and {random2}")
        total = random1 + random2

        answer = total

        time.sleep(1)
        if answer == total:
            score = score + 1
            print(f"The answer is {total} correct")
        elif answer == "clear":
            break
        else:
            score = 0
            print(f"wrong the answer is {total}")
if __name__== "__main__":
    main()
              