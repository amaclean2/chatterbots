import os
import datetime

from difflib import SequenceMatcher
from matchText import match
from questionLoader import getData
from calcTime import doTime


def giveAnswer(question) :
	data = getData('./GlobalStatements.json')

	data = data['data']
	submittedQuestion = ''

	for i in data['questions'] :
		if match(question, i) > 0.8 :
			submittedQuestion = i

	if submittedQuestion == '' :
		for i in data['keywords'] :
			if i in question :
				if i == 'start' :
					argsBeg = question.index(i) + len(i) + 1
					arguments = question[argsBeg:]

				elif i == 'open' :
					argsBeg = question.index(i) + len(i) + 1
					arguments = question[argsBeg:]

				submittedQuestion = data['redirects'][i]

	if submittedQuestion != '' :
		response = data['responses'][submittedQuestion]

		if "!Done" in response :
			carryTask(submittedQuestion, arguments)
		elif "!Time" in response :
			response = doTime()
		elif "!Here" in response :
			findMe()
		return response
	else :
		return 'Uhh, I don\'t know'

def carryTask(task, arguments) :
	command = ""

	if "start" in task.lower() :
		print arguments
		command = "open -a \"" + arguments + "\""

	if "open" in task.lower() :
		print arguments

		if 'http://' not in arguments :
			arguments = 'https://' + arguments

		command = "open -a Safari \"" + arguments + "\""

	os.system(command)
	

def findMe() :
	print "you're here"



while True :
	searchQuery = raw_input("Tell me something: ")

	os.system('clear')

	print ''
	print giveAnswer(searchQuery)
	print ''