import random
random.seed(123)
n = 3+1
counter = 0

## TODO: REFACTOR THE CODE INTO DIFFERENT CLASSES


def isCorrect():
    result = raw_input("Enetr yes or no to indicate if you got this problem right: ")
    return result
    

def setDict():
    init_counter = [0]*n
    originalBank = {}
    for i in range(1,n):
        originalBank[i] = init_counter[i]
    return originalBank
    
    
def randomChoose(originalBank):
    problem = random.choice(originalBank.keys())
    print "You are now working on problem", problem
    return problem
    
    
def updateComments(originalBank, i):
    reviewBank = {}
    problem = randomChoose(originalBank)
    originalBank[i] = originalBank[i]+1
    user_feedback = raw_input("Input your remark about the problem: easy, i got it but do again, or tricky: ")
    reviewBank[i] = user_feedback
    return (originalBank, reviewBank)


def updateProblemBank():
    global counter
    counter = counter + 1
    problem = randomChoose(originalBank)
    if isCorrect() == "yes":
        (currentBank, reviewBank) = updateComments(originalBank, problem)
        print originalBank
        del originalBank[problem]
    else:
        (currentBank, reviewBank) = updateComments(originalBank, problem)
    return (currentBank, counter)

    

def calculateSuccessRate():
    (currentBank, counter) = updateProblemBank()
    c = len(currentBank.keys())
    p = float(n-1-c)/counter
    print "Percentage of accuracy: ", p
    print "currentBank", currentBank
    print "counter", counter
    return (c,p)



originalBank = setDict()
doContinue = True
while (doContinue == True):
    (c, p) = calculateSuccessRate()
    user_command = raw_input("Continue? yes or no: ")
    if (user_command == "no") or (c == 0):
        doContinue = False
        print "Done! Good Bye!"
