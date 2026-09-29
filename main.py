import time
import sys
import os
import pygame

activation = input("Do you want time.sleep? Please enter True or False ").casefold()

timbo = (activation == "true")


yes = "yes"
no = "no"

print("Hello You")
order = input("What's your problem, cause I didn't order a side of sass bitch? ")
if timbo:
    time.sleep(3)
print("Oh is that why, I'm crine")
if timbo:
    time.sleep(2)

myReasons = ["bitchy,", "sad,", " and negative"]
print(f"You're so", *myReasons) # * Tar bort de fula karaktärerna

reasonofBeing = input("Why are you even here at the event ")
if timbo:
    time.sleep(2)
print("'",reasonofBeing,"'", "sounds like an excuse to me")


print("Bartender: Hello miss, what can I get you? Here's our menu:")
menu = ["1. cola", "2. fanta", "3. dirty martini", "4. sex on the beach"]
if timbo:
    time.sleep(2)

for item in menu:
    print(item)

while True:
    
    decision = input("So which would you like? ").lower()

    if "cola" in decision:
        print("A coke it is, sadly no cock")
        break 
        
    elif "fanta" in decision:
        print("A fanta it is, sadly no ice though")
        break 
        
    elif "dirty martini" in decision:
        print("A very dirty martini is on it's way")
        break 
    
    elif "sex on the beach" in decision:
        print("Why don't you have sex with me instead, you're a very pretty dude")
        break  
        
    else:
        print("You gotta pick bro, try again alr.")

longStory = input("Do you want to continue the story?")
no = "no"
yes = "yes"
reasonsofContinue = ["It's good", "lots of drama"]
if no in longStory:
    secondChoice = input(f"Are you sure? There's lot's of reasons such as", *reasonsofContinue)
    if yes in secondChoice:
       print("Okay...."); sys.exit
    if no in secondChoice:
        print("I knew it :)")

if yes in longStory:
    print("I knew it, it's going to turn both romantic and lots of drama, it's going to be worth it: Part two")

# Part 2 
aboutU = ["fashion,", "technology,", "and watching movies"]
print("Here's a backstory about you :)")
if timbo:
    time.sleep(1.5)
print("You're a guy that's 18 years old and you live in USA :)", *aboutU)
answerHobbies = input("Is there any hobby you want to add?")
aboutU.append(answerHobbies)
print(f"Okay so now you like","+", *aboutU)
if timbo:
    time.sleep(2.6)
print("\033c", end="") # Clears th terminal


differentYes = ["yeah", "yes", "ofc", "sure"]
differentNo = ["nahh", "no", "nope", "never"]
differentNo.pop(1)
differentNo.insert(1, "fr")
sass_score = int(0)
shakethatAss = input("You're now on the dance floor, do you want to dance?").casefold()
if timbo:
    time.sleep(2)
print("You see a cute boy sitting not to far away from you, ")
pygame.mixer.init()
pygame.mixer.music.load("friends.mp3")
pygame.mixer.music.play()

dancingChoosing = input("You want to meet him, but how do you want to walk there: fast or cute? ")

howtoWalk = ["fast", "cute"]
theReal = ["nonchalant", "tuff"]
if dancingChoosing in howtoWalk:
    print("No, you'll walk", theReal[0], "trust me on this one :)")
if timbo:
    time.sleep(1.9)
print("It seems like he may be the onem")


def age_check(x):
 if   x <= 17:
    return False
 else:
    return True

x = int(input("How old do you want to be btw, it will decide a lot?"))

randomListS = ["yes", "yeah", "sure", "alr", "ofc"]
randomListN = ["nahh", "no", "nope"]
age_check(x) 
yx = age_check(x) # skickar input-variablen till funktionen för att checkas och i detta fall True or False
if yx == True:
    print(f"You two start to talk, you find out you have a lot in common such as", answerHobbies[3])
    if timbo:
        time.sleep(1.5)
    favArtist = input("He asks what you think about L'amour Toujours, have you heard the song before?")
    if favArtist in randomListN:
        decisionMusic = input("Really? Do you want to hear it?")
        if "yes" or "yeah" in decisionMusic:
                print("I like you already, listen for like one minute")
                pygame.mixer.stop
                pygame.mixer.music.load("Lamour.mp3")
                pygame.mixer.music.play()
                time.sleep(65)
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()

                print(("So what do you think about from a scale 1 to 10, but you can only choose even numbers such as:"))
                if timbo:
                    time.sleep(1.3)
                for i in range(0, 11, 2):
                    print(i)
                answerLamour = int(input())
                while answerLamour % 2 != 0: # 
                    print("I said even numbers only")
                    answerLamour = int(input())

                if answerLamour <= 5:
                    finalSong= input("Really, why? You want to give another song last one try before we continue talking about random stuff?")
                    if finalSong in randomListS:
                        pygame.mixer.music.load("Plavi.mp3")
                        pygame.mixer.music.play()
                        print("What do you think of this one? Listen for like another minute")
                        time.sleep(65)
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        print("So what do you think")
                        answerPlavi = input()
                        print("I trust your opinion lol")
                    else:
                        print("I dont think I like you anymore if you can't even listen to a song anymore, goodbye!")
                        sys.exit()
                elif answerLamour > 5:
                    print("I knew it lol, it's a banger right, I gotta go to the toilet but I'll be back in 30 sec")
                
else:
    print("He's way too young for you, look for someone else")
    sys.exit()

print("Do you want to come home with me maybe? I kinda like you then but damm I talk much",)
answertoHome = input("What do you want to reply?")
answertoHomeLen = len(answertoHome)
xyz = 9
zyx = 2
while True:
    if answertoHome in differentYes:
      print("Yeah just a quick question, do you know how many letters it was in the sentance you just said? " \
        "I'm a bit autistic but if you were wondering it's", answertoHomeLen)
      break
    else:
        print("You should really rethink your desicion!")
        answertoHome = input("What do you want to reply?").upper()
        if answertoHome in differentYes:
            break

houseCarachter = ["dark,", "smelling", "creeks."]

print("You're walking on your way home with him")
if timbo:
    time.sleep(1.5)
print("But something seems off about him...")
if timbo:
    time.sleep(1.5)
answeroSomethingIsOff = input("What do you think it is")
print("...we'll see later")
if timbo:
    time.sleep(2.5)
print("You arrive at his house")
if timbo:
    time.sleep(0.5)
print("Everything looks fine at first")
if timbo:
    time.sleep(0.5)
print("So you decide to go in, the house is completly", *houseCarachter[0:2], "and everything", houseCarachter[2]) 
# Om det är mer än två object krävs * annars behövs det inte

time.sleep(3)

friends = ["Oscar,", "Viktor,", "Vincent,", "Freja,", "Ebba"]
print("You start to feel a bit uncomfortable, but you don't want to be rude so you just go with it")
if timbo:
    time.sleep(1.5)
print("he starts to talk about his hobbies and stuff, but you start to feel a bit uncomfortable")
if timbo:
    time.sleep(1.5)
print("You really feel like you should call one of your friends to come and pick you up")
if timbo:
    time.sleep(1.5)

print("Which friend do you want to call:", *friends[0:4], "or maybe", friends[4])
whichFriend = input()

friendsContact = {
    "Oscar":"079-222 83 49",
    "Viktor":"072-853 10 29",
    "Vincent":"072-222 86 03",
    "Freja":"072-854 10 40",
    "Ebba":"073-362 30 18"
}

print(friendsContact[whichFriend])