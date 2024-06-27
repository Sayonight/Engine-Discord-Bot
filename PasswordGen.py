import random

wordlist =[]

with open('words.txt','r') as file:
    for line in file:
        wordlist.append(line)

def gen_words():
    global generated_words, total_words
    while len(generated_words) < 4:
        randomnumber = random.randint(0,8258)  #letzte Nummer= Anzahl der Wörter in der Wortliste
        randomword = wordlist[randomnumber]
        generated_words.append(randomword)
    #print(generated_words)

def caps_words():
    global generated_words, captialized_words
    for word in generated_words:
        capword = word.capitalize()
        captialized_words.append(capword)
    #print(captialized_words)

def add_rest():
    global captialized_words, finished_words
    randomnumber = random.randint(1,9)
    for word in captialized_words:
        finished_words.append(word)
        finished_words.append(str(randomnumber))
    finished_words.append('.')

def generate_password():
    global wordlist,generated_words,captialized_words, finished_words, passwordstring
    generated_words = []
    captialized_words = []
    finished_words = []
    gen_words()
    caps_words()
    add_rest()
    passwordstring = finished_words[0] + finished_words[1] + finished_words[2] + finished_words[3] + finished_words[4] + finished_words[5] + finished_words[6] + finished_words[7] + finished_words[8]
    passwordstring = passwordstring.replace('\n','')

    return passwordstring