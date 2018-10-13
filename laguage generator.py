from random import randint

def main (length):
    total_random_languge(length, " " , ".")
    corr_spaces_random (length, " ", ".")
    narrow_random (length," ", ".")


def total_random_languge(length, word_del, sentece_del):
    print ("total random")
    output = ""
    for i in range (length):
        x = randint(32,126)        
        if (x == 32):
            to_add = word_del
        else:
            to_add = chr(x)
        output += to_add
    print(output)
        

def corr_spaces_random (length, word_del, sentence_del):
    print()
    print ("correct spaces random")
    output = ""
    for i in range (length):
        x = randint(32,159)        
        if (x >= 126):
            to_add = word_del
        else:
            to_add = chr(x)
        output += to_add
    print(output)


def narrow_random (length, word_del, sentence_del):
    print ()
    print ("narrow random")
    output = " "
    for i in range (length):
        x = randint(33,85)        
        if (x >= 73):
            to_add = word_del
        else:
            to_add = chr(x)
        output += to_add
    print(output)

def gen_alph(word_del, sentence_del):
    alphabet = {}
    for i in range(25):
        x = randint (32,126)
        while(not(chr(x) != word_del and chr (x) != sentence_del and not(chr(x) in alphabet))):
            x = randint (32,126)
        alphabet.update({chr(x): 0})
    return alphabet

def android_letter_freq (alphabet):
    i = 23
    for x in alphabet:
        if (i < 3):
            alphabet[x] = 0
            continue
        else :
            alphabet[x] = i
        i -= 1
    return alphabet

def android_word(alphabet):
    length = randint (1,8)
    word = ""
    lastlast = ""
    last = ""
 
    while length > 0:
        rand = randint (0,345)
        for x in alphabet:
            rand -= alphabet[x]
            if (rand <= 0):
                lastlast = last
                last = x
                if (lastlast == last and last == x):
                    continue
                word += x
                length -= 1
                break
    return word

def android_language(alphabet):
    language = []
    for i in range (150):
        language.append(android_word(alphabet))
    return language
                
def android_text(words_count, word_del, sentence_del):
    sentence_length = randint (3,8)
    text = ""
    alphabet = android_letter_freq(gen_alph(word_del, sentence_del))
    language = android_language(alphabet)
    for i in range(words_count):
        rand = randint(0,len(language)-1)
        text += language[rand]
        sentence_length -= 1
        if (sentence_length <= 0):
            sentence_length = randint (3,8)
            text += sentence_del
            text += word_del
        else:
            text += word_del
    print (text)
    return text
def android_text_1(words_count, word_del, sentence_del):
    sentence_length = randint (1,8)
    if(sentence_length < 3):
        if (randint(1,100)>50):
            sentence_length = randint(3,8)
    text = ""
    alphabet = android_letter_freq(gen_alph(word_del, sentence_del))
    language = android_language(alphabet)
    for i in range(words_count):
        rand = randint(0,len(language)-1)
        text += language[rand]
        sentence_length -= 1
        if (sentence_length <= 0):
            sentence_length = randint (1,8)
            if(sentence_length < 3):
                if (randint(1,100)>50):
                    sentence_length = randint(3,8)
            text += sentence_del
            text += word_del
        else:
            text += word_del
    print (text)
    return text

def AI_letter_freq (alphabet):
    i = 23
    for x in alphabet:
        if (i < 3):
            alphabet[x] = 0
            continue
        else :
            alphabet[x] = i
        i -= 1
    return alphabet

def AI_word(alphabet):
    length = randint (1,14)
    word = ""
    lastlast = ""
    last = ""
 
    while length > 0:
        rand = randint (0,345)
        for x in alphabet:
            rand -= alphabet[x]
            if (rand <= 0):
                lastlast = last
                last = x
                if (lastlast == last and last == x):
                    continue
                word += x
                length -= 1
                break
    return word

def AI_language(alphabet):
    language = []
    for i in range (150):
        language.append(AI_word(alphabet))
    return language
                
def AI_text(words_count, word_del, sentence_del):
    sentence_length = randint (3,14)
    text = ""
    alphabet = AI_letter_freq(gen_alph(word_del, sentence_del))
    language = AI_language(alphabet)
    for i in range(words_count):
        rand = randint(0,len(language)-1)
        text += language[rand]
        sentence_length -= 1
        if (sentence_length <= 0):
            sentence_length = randint (3,14)
            text += sentence_del
            text += word_del
        else:
            text += word_del
    print (text)
    print (alphabet)
    return text

    
    """for i in range(words_count):
        if
        text += android_word(alphabet)
        sentence_length -= 1
        if (sentence_length <= 0):
            text += sentence_del
            text += word_del
        else:
            text += word_del
    print (text)
    return text
"""

def natural_alph(word_del, sentence_del):
    alphabet = []
    for i in range(25):
        x = randint (32,126)
        while(not(chr(x) != word_del and chr (x) != sentence_del and not(chr(x) in alphabet))):
            x = randint (32,126)
        alphabet.append(chr(x))
    return alphabet

def just_caesar (text, word_del, sentence_del):
    alphabet = natural_alph(word_del, sentence_del)
    output = ""
    for x in text.upper():
        if (x == " "):
            output += word_del
            continue
        if (x == "."):
            output += sentence_del
            continue
        if (ord (x)< 65 or ord(x) > 89): #mistake here index out of index shouldnt be 89 but 90
            continue
        output += alphabet[ord(x) - ord ('A')]
    print (output)
    return (output)

def natural_without_3 (text, word_del, sentence_del):
    alphabet = natural_alph(word_del, sentence_del)
    output = ""
    for x in text.upper():
        if (x == " "):
            output += word_del
            continue
        if (x == "."):
            output += sentence_del
            continue
        if (x == 'Z'):
            output += alphabet[0]
        if (x == 'Q'):
            output += alphabet[19]
        if (x == 'X'):
            output += alphabet[4]
        if (ord (x)< 65 or ord(x) > 89):
            continue
        output += alphabet[ord(x) - ord ('A')]
    print (output)
    return (output)    

def natural_8max(text, word_del, sentence_del):
    alphabet = natural_alph(word_del, sentence_del)
    output = ""
    sentence_length = randint (3,8)
    word_length = 8
    word_count = 0
    prev = ""
    
    for x in text.upper():
        if (word_count == 500):
            break
        if (x == " " or word_length <= 0):
            if (prev == word_del and x == " "):
                output = output[:-1]
                word_length +=1
                word_count -=1
            prev = word_del
            word_length -= 1
            word_count +=1
            sentence_length -=1
            output += word_del
            word_length = 8
        if ((prev == word_del and x == ".") or (sentence_length <= 0 and prev == word_del)):
            output = output[:-1]
            output += sentence_del
            output += word_del
            prev = word_del
            sentence_length = randint(3,8)
            word_length = 8
            if (x !=  "." and x != " " and ord (x)> 65 and ord(x) < 89):
                output += alphabet[ord(x) - ord ('A')]
                prev = alphabet[ord(x) - ord ('A')]
                word_length -= 1
            continue
        if (x == "." or sentence_length <= 0):
            output += sentence_del
            sentence_length = randint(3,8)
            word_length = 8
            output += word_del
            prev = word_del
            word_count +=1
            if (x !=  "." and x != " " and ord (x)> 65 and ord(x) < 89):
                output += alphabet[ord(x) - ord ('A')]
                prev = alphabet[ord(x) - ord ('A')]
                word_length -= 1
            continue
        if (ord (x)< 65 or ord(x) > 89): 
            continue
       
        output += alphabet[ord(x) - ord ('A')]
        prev = alphabet[ord(x) - ord ('A')]
        word_length -= 1
    print (output)
    return (output)

def corr_freq (length):
    pass
    
text = "Together, we will determine the course of America and the world for many, many years to come. We will face challenges. We will confront hardships. But we will get the job done. Every four years, we gather on these steps to carry out the orderly and peaceful transfer of power, and we are grateful to President Obama and First Lady Michelle Obama for their gracious aid throughout this transition. They have been magnificent. Thank you. Todayâ€™s ceremony, however, has very special meaning. Because today we are not merely transferring power from one Administration to another, or from one party to another â€“ but we are transferring power from Washington DC and giving it back to you, the people. For too long, a small group in our nationâ€™s Capital has reaped the rewards of government while the people have borne the cost. Washington flourished â€“ but the people did not share in its wealth.Politicians prospered â€“ but the jobs left, and the factories closed.The establishment protected itself, but not the citizens of our country.Their victories have not been your victories; their triumphs have not been your triumphs; and while they celebrated in our nationâ€™s capital, there was little to celebrate for struggling families all across our land.But for too many of our citizens, a different reality exists: mothers and children trapped in poverty in our inner cities; rusted-out factories scattered like tombstones across the landscape of our nation; an education system, flush with cash, but which leaves our young and beautiful students deprived of all knowledge; and the crime and the gangs and the drugs that have stolen too many lives and robbed our country of so much unrealized potential. For many decades, weâ€™ve enriched foreign industry at the expense of American industry; subsidized the armies of other countries while allowing for the very sad depletion of our military; weâ€™ve defended other nationsâ€™ borders while refusing to defend our own; and spent trillions and trillions of dollars overseas while Americaâ€™s infrastructure has fallen into disrepair and decay. We do not seek to impose our way of life on anyone, but rather to let it shine as an example for everyone to follow. We will reinforce old alliances and form new ones â€“ and unite the civilized world against radical Islamic terrorism, which we will eradicate from the face of the Earth. At the bedrock of our politics will be a total allegiance to the United States of America, and through our loyalty to our country, we will rediscover our loyalty to each other. When you open your heart to patriotism, there is no room for prejudice.The Bible tells us: â€śHow good and pleasant it is when Godâ€™s people live together in unity.â€ť We must speak our minds openly, debate our disagreements honestly, but always pursue solidarity. When America is united, America is totally unstoppable. Fuck you We will be protected by the great men and women of our military and law enforcement and, most importantly, we are protected by God."    
gen_alph(" ", ".")
android_word(android_letter_freq (gen_alph(" ", ".")))

print ("androidi text")
android_text(500, " ", ".")
print()
print ("androidi text 2")
android_text(500, ":", "(")
print()
print ("androidi text 3 1111111")
android_text_1(500, "0", "1")
print()
print("just caesar text")
just_caesar(text, " ", ".")
print()
print("8 max text")
natural_8max(text, ":", "(")
print()
print("natural_without_3")
natural_without_3 (text, " ", ".")
print ()
print ("AI")
AI_text(500, "0", "1")
