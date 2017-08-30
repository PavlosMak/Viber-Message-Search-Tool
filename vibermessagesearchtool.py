import os
import os.path
import codecs #support for greek(and other) chars. It is not requiered if you are using only english characters

firstDir = os.getcwd()

try:
	os.remove("results.txt")
except:
	pass

os.chdir(firstDir+"/Viber messages")
files = os.listdir()

conversations = []

for i in files:
	if i != '.DS_Store': #ignore this hidden file in Mac OS X
		conversations.append(i.strip(".CSV"))
		
while True:
	messages = []
	dates = []
	hours = []
	senders = []
	results = []
	os.chdir(firstDir+"/Viber messages")

	print("Choose a conversation by typing its number: ")

	for c in range(0,len(conversations)):
		print(str(c + 1) + ". " + conversations[c]) 

	choise = input("Number: ")

	try:
		choise = int(choise)
	except:
		print("Not a valid choise")
		continue
	if choise <= 0:
		print("Not a valid choise")
		continue
	try:
		conToload = conversations[choise-1]
		try:
			os.remove("results.txt")
		except:
			pass
	except:
		print("Not a valid choise")
		continue

	conToload = conToload + ".CSV"

	file = open(conToload,'r',encoding="utf-16le")#the encoding of the files that Viber generated

	print("Your conversation is loading. This might take a while hold on...")

	for row in file:
		try:
			row = row.split("\t")
			message = row[-1].split('\t')[-1]
			messages.append(message.lower())
			dates.append(row[0].strip('='))
			try: #got a strange error for a specific file I was working on this seems to solve it without removing any messages
				hours.append(row[1])
			except:
				continue
			senders.append(row[2].strip('='))
		except UnicodeEncodeError:
			continue

	file.close()

	os.chdir(firstDir)

	print("Choose a finding method: ")
	print("1.By character/word/phrase")
	print("2.By date")
	method = input("Choose by number(1/2) or type something else to return in the main menu: ")
	
	if method == '1':
		toFind = input("Find: ").lower()
			
		fileToWrite = open("results.txt","w",encoding="utf-8")

		for m in range(0,len(messages)):
			if toFind in messages[m]:
				results.append("At {} {} {} wrote: \n \t{}".format(
					dates[m].strip('''"'''),
					hours[m],
					senders[m].strip('''"'''),
					messages[m]))

		fileToWrite.write("Found {} results in a total of {} messages\n\n".format(len(results),len(messages)))
		
		for r in results:
			fileToWrite.write(r)
			fileToWrite.write('\n')

		fileToWrite.close()
	
	elif method == '2':
		dateToFind = input("Date(day/month/year: 13/02/2017): ")
		
		dateToFind = '''"{}"'''.format(dateToFind) 

		fileToWrite = open("results.txt","w",encoding="utf-8")

		for d in range(0,len(dates)):
			if dateToFind == dates[d]:
				results.append("At {} {} {} wrote: \n \t{}".format(
					dates[d].strip('''"'''),
					hours[d],
					senders[d].strip('''"'''),
					messages[d]))

		fileToWrite.write("Found {} results in a total of {} messages\n\n".format(len(results),len(messages)))
		
		for r in results:
			fileToWrite.write(r)
			fileToWrite.write('\n')

		fileToWrite.close()

	else:
		continue