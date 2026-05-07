import random
import os

# Enabling colors for the game feel
os.system('')
GOLD = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def guessgame():
	secnumber = random.randint(1,100)
	attempts  = 0
	max_score = 100

	print(f"\n {CYAN} -----New Round----- {RESET} ")
	print("I have picked a number between 1 and 100")

	while True:
		try:	
			guess = int(input("Guess a number between 1 and 100: "))
			attempts += 1

			if guess < secnumber:
				print("Too low!")
			elif guess > secnumber:
				print("Too high")
			else:
				#SCORING LOGIC = 100 minus (10 points per attempts)
				# The points will never go below 0
				final_score = max(0, max_score - ((attempts - 1) * 10))

				print(f"\n {GOLD} Correct!! {RESET}")
				print(f"Attempts : {attempts}")
				print(f"Final Score: {GOLD} {final_score}/100 {RESET}")
				break

		except ValueError:
			print("Invalid input, insert a number.")

def main():
	while True:
		guessgame()

		#PLAY AGAIN LOOP
		again = input("\n Do you want to play again? y/n : ").lower()
		if again != 'y':
			print("Thanks for playing. Final points cleared. Have a great day!!")
			break
	

if __name__ == "__main__":
    main()