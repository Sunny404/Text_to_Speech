import pyttsx3

engine = pyttsx3.init()

#print default rate
Rate = engine.getProperty("rate")
print(Rate)

#set custom rate
engine.setProperty('rate',150)
#volume
#Setting up volume level between 0 and 1
volume = engine.getProperty("volume")
print("volume is {0}".format(volume))


#change the default volume
engine.setProperty("volume",.7)

#voices
voice = engine.getProperty("voices")

#male voice of index 0 and female of 1
print("Male voice : {0}".format(voice[0].id))
print("Female voice : {0}".format(voice[1].id))

#setting up voice
engine.setProperty('voice',voice[1].id)

#Type what you wanna listen
engine.say('Hello Python')
engine.runAndWait()
