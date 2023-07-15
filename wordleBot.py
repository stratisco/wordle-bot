f = open("5letterWords.txt", "r")
words = f.read()

def chance(word, wordList): #input type: str, str
    chance = 0
    letters = ''
    for i in word:
        if i not in letters:
            letters += i
    for letter in letters:
        chance += wordList.count(letter)

    return chance #output type: int

def bestChoice(wordLis): #input type: list
    tmp_1 = []

    for i in wordLis:
        tmp_1 += [[i, chance(i, ' '.join(wordLis))]]
        
    return sorted(tmp_1, key=lambda x: x[1]) #output type: list
    
def selection():
    in_ = ''
    notIn_ = ''
    green_ = ''
    notPlace_ = ''
    
    print("for mark stage:")
    print("green = 1")
    print("yellow = 2")
    print("grey = 3")
    print()
    input_ = input("word: ")
    mark = input("mark: ")
    for v, m in zip(input_, mark):
        if m == '1':
            in_ += v
            green_ += v
            
        else:
            green_ += '#'
        
        if m == '3':
            notIn_ += v
            
        if m == '2':
            in_ += v
            notPlace_ += v
        
        else:
            notPlace_ += '#'
    return in_, notIn_, green_, notPlace_ #output type: str, str, str, str
    
        

inWord = ''
notIn = ''
rightPlace = '#####'
notPlace = []

for i in range(6):
    wordList = []
    
    a, b, c, d = selection()
    
    inWord += a
    
    notIn += b
    
    out = ''
    for v, l in zip(rightPlace, c):
        if l != '#':
            out += l
        else:
            out += v
            
    rightPlace = out
    
    notPlace += [d]
    
    print()
    for word in words.split():
        check = 1
        for l in inWord:
            if l not in word:
                check = 0
                
        for l in notIn:
            if l in word:
                check = 0
                
        for l, v in zip([v for v in word], [v for v in rightPlace]):
            if l != v and v != '#':
                check = 0
        
        for l in notPlace:
            for n, w in zip(l, word):
                if n == w:
                    check = 0
        
        if check == 1:
            wordList += [word]
    
    best = bestChoice(wordList)
    for l in best:
        print(l[0], l[1])
    print()
    print()
    print("Best choice:", best[-1][0])
    print()
    print('=========================================')