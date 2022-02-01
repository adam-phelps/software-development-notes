# Adam Phelps 2/1/2022
# Load k,v from csv file

import csv
import sys

csv_file = "vim_qa.csv"

if __name__ == "__main__":
	with open(csv_file) as csvf:
		next(csvf) # Skip the header row
		reader = csv.reader(csvf, delimiter=",")
		for row in reader:
			question = row[0]
			answer = row[1].strip()
			print("Q: {}".format(question))
			user_guess = input()
			if (user_guess == answer):
			    print("CORRECT!")
			else:
			    print("INCORRECT.")
	sys.exit(0)
