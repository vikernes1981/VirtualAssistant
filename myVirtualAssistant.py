import speech_recognition as sr
import subprocess
import pyttsx3
import webbrowser
import datetime
from gtts import gTTS
import time

# Put weather and windows support?
# Make a completely new greek version?


name = "mama"

# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommandEnglish(language='en-US'):

	lang = language

	r = sr.Recognizer()

	# from the speech_Recognition module
	# we will use the Microphone module
	# for listening the command
	with sr.Microphone() as source:
		print('Listening')
		
		# seconds of non-speaking audio before
		# a phrase is considered complete
		r.pause_threshold = 2
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		
		# Now we will be using the try and catch
		# method so that if sound is recognized
		# it is good else we will have exception
		# handling
		try:
			print("Processing command")
			Query = r.recognize_google(audio, language=lang) # https://cloud.google.com/speech-to-text/docs/languages
			print("Command : ", Query)
			
		except Exception as e:
			print(e)
			#voice("Please repeat ")
			return "None"
		
		return Query

# Processes greek so that I can query youtube with greek
def youTube():
	voice("What do you want to see?")
	text = takeCommandEnglish('el-GR').lower() # You can change language here to understand exactly what you want in your lang

	return text


# Here we add text-to-speech and saving it in
# the folder of our choice.
def voice(text, lang='en-US'):
	mytext = text
	language = lang
	path = "/home/v1k3rn35/kali/v1k3rn35/Portfolio/VirtualAssistant/" # CHANGE TO YOUR DESIRED PATH
	myVoice = gTTS(text=mytext, lang=language, slow=False)
	myVoice.save(path + text + ".mp3")
	voice = str(path + text + ".mp3")
	temp = subprocess.Popen(['mpg123', voice])

# Function for single word commands
def command(command):
	temp = subprocess.Popen([command])

def tellDay():
	
	# This function is for telling the
	# day of the week
	day = datetime.datetime.today().weekday() + 1
	
	#this line tells us about the number
	# that will help us in telling the day
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		return day_of_the_week

def tellTime():
	
	# This method will give the time
	time = str(datetime.datetime.now())
	
	# the time will be displayed like
	# this "2020-06-05 17:50:14.582630"
	# and then after slicing we can get time
	
	hour = time[11:13]
	minutes = time[14:16]
	return "Time is " + hour + " hours and " + minutes + " minutes"

# This function will listen only to one command
# so that the program won't interfere with whatever
# we are doing. It's the Close And Wait function


def goToSleep():
	sleep = True
	while sleep:
		query = takeCommandEnglish().lower()
		if (name + " wake up") in query:
			voice("Waking up")
			sleep = False
			
		elif (name + " status") in query:
			voice("I'm asleep")
			continue

def Take_query():
	
	# This loop is infinite as it will take
	# our queries continuously unless
	# we say bye or exit to terminate
	# the program or put it to Sleep
	noSleep = True
	while noSleep:

		# taking the query and making it into
		# lower case so that most of the times
		# query matches and we get the perfect
		# output
		query = takeCommandEnglish().lower()

		# Open Youtube
		if (name and "youtube") in query:			
			# give the link
			# of the website and it automatically open
			# it in your default browser
			test = youTube()
			voice("Opening Youtube")
			time.sleep(2)
			webbrowser.open("https://www.youtube.com/results?search_query=" + test)
			continue

		# Gold movies is a streaming movies site
		elif (name and "gold movies") in query:
			test = youTube()
			voice("opening gold movies")
			time.sleep(4)
			webbrowser.open("https://xrysoi.pro//?s=" + test)
			continue
		
		# Tell day	
		elif (name + " day") in query:
			voice(tellDay())
			time.sleep(3)
			continue
		
		# Tell time
		elif (name + " time") in query:
			voice(tellTime())
			time.sleep(3)
			continue
		
		# This will exit and terminate the program
		elif (name + " bye") in query or (name + " exit") in query:
			voice("bye")
			time.sleep(2)
			exit()
		
		# Tells the name you gave to you assistant
		elif (name  + " tell me your name") in query:
			command('clear')
			voice("I am " + name)
			continue
		
		# Open text editor
		elif (name + " opentext") in query:
			voice("opening sublime")
			time.sleep(3)
			command('subl')
			continue
		
		# Open terminal
		elif (name + " open terminator") in query:
			voice("opening terminator")
			time.sleep(3)
			command("terminator")
			#temp = subprocess.Popen(['remotinator', 'hsplit'])
			continue

		# Close browser 
		elif (name + " firefox down") in query:
			voice("Closing firefox")
			time.sleep(3)
			temp = subprocess.Popen(['killall', 'firefox'])
			continue

		# Close text editor
		elif (name + " text down") in query:
			voice("closing sublime")
			time.sleep(3)
			temp = subprocess.Popen(['pkill', '-f', 'subl'])
			continue

		# Close terminal
		elif (name + " terminal down") in query:
			voice("closing terminator")
			time.sleep(3)
			temp = subprocess.Popen(['pkill', '-f', 'terminator'])
			continue
		
		# Open browser in search tab
		elif (name + " open browser") in query:
			voice("opening new search tab")
			time.sleep(3)
			webbrowser.open('https://duckduckgo.com/')
			continue

		# Mute/unmute volume
		elif (name + " volume") in query:
			temp = subprocess.Popen(['amixer', '-q', '-D', 'pulse', 'sset', 'Master', 'toggle'])
			time.sleep(3)
			continue

		# Shut down pc	
		elif (name + " system down") in query:
			voice("Shutting Down")
			time.sleep(3)
			command("poweroff")

		# Reboot pc
		elif (name + " start again") in query:
			voice("Rebooting")
			time.sleep(3)
			command("reboot")
		
		# Put the program in wait mode	
		elif (name + " sleep") in query:
			voice("Going to sleep")
			noSleep = False

		# Update 
		elif (name and "update") in query:
			voice("Updating")
			temp = subprocess.Popen(["sudo", "apt", "update"])
			stderr = temp.communicate()
			time.sleep(3)
			voice("System Updated")
			continue

		# Upgrade
		elif (name and "upgrade") in query:
			voice("Upgrading")
			temp = subprocess.Popen(["sudo", "apt", "dist-upgrade", "-y"])
			stderr = temp.communicate()
			time.sleep(3)
			voice("System Upgraded")
			continue

		# Remove
		elif (name and "remove") in query:
			voice("Removing shit")
			temp = subprocess.Popen(["sudo", "apt", "autoremove", "-y"])
			stderr = temp.communicate()
			time.sleep(3)
			voice("Shit removed")
			continue

		elif (name + " virtualbox") in query:
			voice("Opening virtualbox")
			time.sleep(3)
			temp = subprocess.Popen(["VirtualBox", "&"])
			continue

		elif (name + " virtual down") in query:
			voice("closing virtualbox")
			time.sleep(3)
			temp = subprocess.Popen(["killall", "VirtualBox"])
			continue

		elif (name + " status") in query:
			voice("I'm awake")
			continue

if __name__ == '__main__':
	
	# main method for executing
	# the functions
	time.sleep(5)
	voice("Ahoy, I am " + name + "...your new assistant")
	time.sleep(3)
	while True:
		Take_query()
		goToSleep()

