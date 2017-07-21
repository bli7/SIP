print ("High School Adventure")
print ("")
print ('''PLEASE ANSWER WITH THE SAME WORDING AS THE WORDS INSIDE THE PARENTHESES. MAKE SURE TO SWITCH THE TENSE FROM SECOND TO FIRST PERSON''')
print ("")

first_decision =  input ('''Welcome! You are a regular teenager trying to pass high-school.
It's twelve o'clock in the morning and you still have a test to study for. You
are familiar with 50 percent of the material. Will you (stay up for another
hour) to study or (wake up early tomorrow) to study? ''')

print ("")



# First Round
if first_decision == "stay up for another hour":
    print ('''Make sure you have enough caffeine. It might actually takes
    longer than you expected''')
elif first_decision == "wake up early tomorrow":
    second_decision = input ('''Oh no. You missed the alarm clock, so you decided to study
    on the train. But you are distracted by your friends. Would you (cut
    your first class) to study or (take the test) you know you are going to
    fail?''')

    if second_decision == "cut my first class":
        print ("")
        print ("tsk tsk")
    elif second_decision == "take the test":
        print ("")
        print ("I like your attitude. Try your best on the test.")
    else:
        print ("")
        print ("Please retype your answer. Make sure everything is lower-cased")
else:
    print ('''please retype your answer, sample answer includes 'stay up
    to study' or 'wake up early in the morning' ''')






print ("")
# Second Round
second_round = input ('''Phew! You are done with your test. Now you are
going to your computer science class. You realized you did not upload your
code to your hw account. Unfortunately, the teacher decided to check
homework today. Are going to (ask your friend to send their code) and
copy all their code or (tell your teacher honestly)?''')

if second_round == "ask my friend to send their code":
    print ("")
    print ("That is academic dishonesty. Don't do it next time.")
elif second_round == "tell my teacher honestly":
    print ("")
    print ("Make sure to ask for extension, but your grade may suffer a bit")
else:
    print ("")
    print ("Please retype your answer, make sure everything is lower-cased")





print ("")
#Third Round
third_round = input ('''Yay! Now it's time for swim gym! You had a good
time in the pool. However, it took you a little too long in the stalls
and you will be late to your next class. Your classroom is on the 9th floor,
and your teacher absolutely hates people for being late. Are you going to (sneak
in the elevator) without a pass or (walk to your class) knowing your teacher
will hate you?''')

print ("")
if third_round == "sneak in the elevator":
    print ("")
    print ("tsk, tsk. I hope the dean is not on the elevator.")

    emergency = input('''Oh no, the dean is on the elevator with you. You
    are caught! Will you (pretend you have a headache) and stay in the elevator or
    will you (run out of the elevator) before the dean says anything?''')

    if emergency == "prentend I have a headache":
        print ("")
        print ("Good luck. Your dean is not easily fooled")
    elif emergency == "run out of the elevator":
        print ("")
        print ("Lmao")
    else:
        print ("")
        print ("please retype your answer. Make sure everything is lower-cased")
elif third_round == "walk to my class":
    print ("")
    print ('''You are going to be 10 minutes late and your teacher will hate
    you. Change faster next time when you have swim class.''')
else:
    print ("")
    print ('''please retype your answer. Make sure everything is lower-case''')




# Round four
print ("")
forth_round = input ('''It's time for lunch and you decided to eat outside
of school. But it's raining outside and the weather is chilly. You waited
5 minutes and your friend is still not at the entrance. Will you (go to
the restaurant) and wait for her there or text her again and (wait until he
/ she replies)''')

print ("")
if forth_round == "go to the restaurant":
    print ("")
    print ('''Okay. I totally get your decision because it's freezing out''')

    whoops = input ('''It turns out your friend doesn't have an umbrella and
    now she hates you for ditching her. What will you say to her?''')

    if whoops == "I am sorry, I won't do it the next time":
        print ("")
        print ("good to see you apologized")
    else:
        print ("")
        print ('''You have the rights to what you say. But I hope your friend
        won't be angry at you anymore''')

elif forth_round == "wait until he / she replies":
    print ("")
    print ("You are such a nice friend to have.")

    oh_no = input ('''Your friend is still not out after ten minutes and
    she hasn't respond to any of your messages. Will you (text her again and wait), (cancel the plan to eat outside),
    or (go to the restaurant by yourself).''')

    if oh_no == "text her again and wait":
        print ("")
        print ("You have tons of patience!")
    elif oh_no == "cancel the plan to eat outside":
        print ("")
        print ('''Make sure to tell your friend the plan change and tell her
        she needs to be more considerate next time.''')
    elif oh_no == "go to the restaurant by myself":
        print ("")
        print ("You are not the one to blame.")
    else:
        print ('''please retype your answer. Make sure everything is lower-case''')


#Round five
print ("")
fifth_round = input('''Thank God, it's the end of the day. However, you just received an email that your club will
be holding an important meeting for the competition next week. But you have a big project due tomorrow. Will you
go home and finish the project (p) or go to the meeting(m) ?''')

print("")
if fifth_round == "p":
    print ("")
    print ("Good luck on your project, make sure to talk with your club president though.")

elif fifth_round == "m":
    print("")
    print ("You are a very responsible club member!")

else:
    print("")
    print ("Make sure you type the stuff inside the parentheses correctly.")


print ("")
print ("Time to go home. You have passed all the challenge for today. Keep fighting!")
