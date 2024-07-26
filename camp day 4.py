
questions  =[" what town is ash from?",",what pokemon got ash his win against cyntia?",
"what pokemon got ash his win against leon?"," what is ashes best fire type?",
"what was ashes rarest pokemon?","how did ash die because of mewtwo and mew?",
"how did ashes greninja start the journey with ash?",
"when did ash get his fletchlig"]   

answers = ["pallet town","lucario","pikachu","charizard","solgeleo",
"he got blasted by there energy",
"by helping ash defeat team Rocket as a froakie","in the johto seiries"]


score = 0


for i in range(len(questions)):
    print(questions[i])
    guess = input("Answer: ")
    answer = answers[i]
    if guess.lower() in answer.lower():
        print("good now move on or I will kill you")
        score += 1
    else:
        print ("you got it wrong I will kill everyone you hold dear")
        print("the answer was "+answers[i]+ "\n")
print("you got "+ str (score) + " out of" +str(len(questions))+"!")


































