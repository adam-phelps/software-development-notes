#!/bin/bash
# Adam Phelps 2/1/22

function check_answer {
	if [[ $1 == $2 ]]; then
		echo "Correct"
	else
		echo "INCORRECT: answer is $2"
	fi
}

echo "You are taking a vim test."
echo "====START TEST====="

echo "How do you go left in VIM? (which letter?)"
read answer
check_answer $answer "h"

echo "Right in VIM? (which letter?)"
read answer
check_answer $answer "l"

echo "Jump to end of line"
read answer
check_answer $answer "$"

echo "Paste BEFORE cursor"
read answer
check_answer $answer "p"

echo "Write and quit a file"
read answer
check_answer $answer ":wq!"

echo "What is the mode you enter VIM in? (respond answer one word lowercase)"
read answer
check_answer $answer "command"

echo "How do you move UP 10 lines in VIM?"
read answer
check_answer $answer "10k"

echo "How do you move DOWN 10 lines in VIM?"
read answer
check_answer $answer "10j"
echo "====END TEST===="
