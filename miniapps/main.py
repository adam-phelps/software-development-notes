# Adam Phelps 2/1/2022
# Load k,v from csv file

import csv
import sys
import random

csv_file = "vim_qa.csv"

# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_quiz_spirit_animal():
	animals = ["tiger", "lion", "dog", "cat", "ferret", "frog", "canary", "sugar glider"]
	animal_of_day = animals[random.randrange(0,len(animals))]
	print("Animal of the day is {}".format(animal_of_day))

class Scorer:

	questions = 0
	correct = 0
	incorrect = 0

	def __init__(self, questions):
		self.questions = questions

	def update_correct(self):
		self.correct = self.correct + 1

	def update_incorrect(self):
		self.incorrect = self.incorrect + 1

	def print_score(self):
		print("Total Questions {}, Correct {}, Incorrect {}".format(
			self.questions, self.correct, self.incorrect))

	def print_final_percentage(self):
		print("Test Percentage: {}%".format((self.correct/self.questions)*100))

if __name__ == "__main__":
	total_questions = sum(1 for line in open(csv_file))
	MyScorer = Scorer(total_questions)
	print_quiz_spirit_animal()
	with open(csv_file) as csvf:
		next(csvf) # Skip the header row
		reader = csv.reader(csvf, delimiter=",")
		for row in reader:
			question = row[0]
			answer = row[1].strip()
			print("Q: {}".format(question))
			user_guess = input()
			if (user_guess == answer):
				MyScorer.update_correct()
				print(bcolors.OKGREEN + "CORRECT!" + bcolors.ENDC)
			else:
				MyScorer.update_incorrect()
				print(bcolors.FAIL + "INCORRECT." + bcolors.ENDC)
				print(bcolors.OKBLUE + "Correct Answer is: {}".format(answer) + bcolors.ENDC)
			MyScorer.print_score()
	MyScorer.print_final_percentage()
	sys.exit(0)
