import random

pronoun = ["I", "you", "we", "he", "she", "they", "the dog", "the boy", "the girl" ]
verb = ["like", "run", "walk", "love", "swim","read"]
noun = ["food", "in the sea", "the newspaper", "across the street", "dogs", "around the park"]

acumulate = random.choice(pronoun) + " " + random.choice(verb) + " " + random.choice(noun)
print (acumulate)
print("")

# randomly pick a number between 0 and 500 for a 100 times
def listify():
    g = []
    for counter in range(100):
        randomized = random.randint(0, 500)
        g.append(randomized)
    return g

compiling = listify()
print (compiling)

def mult_of_five():
    mult = []
    for elem in compiling:
        if elem % 5 == 0:
            mult.append(elem)
    return mult

print ("")
print (mult_of_five())
print ("")
print ("There are ", len(mult_of_five()), " multiples of five")


input_limit = input("limit?")
num_limit = int(input_limit)

def prime_number(limit):
    g = []
    for num in range(2, limit):
        prime = True
        for i in range (2,num):
            if (num % i) == 0:
                prime = False
        if prime:
            g.append(num)
    return g

print ("")
print (prime_number(num_limit))

# based on the prime number
def add_prime():
    addition = 0
    for elem in prime_number(num_limit):
        addition += elem
    return addition

print ("")
print ("The sum of all prime numbers between 0 and", num_limit, "is", add_prime())
