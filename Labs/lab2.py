#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = 'armando'

        #
        # Enter your own print statements below:
        print('This is a test message '+ message + ' is the best')
        #

        # print only first and last of the sentence:
        print('The first character is: '+ message[0])
        print('The last character is: ' + message[-1])

        # use slice notation:
        print('print from position 3 to the end: ' + message[3:])
        print('print to position 3 from the star: ' + message[:3])
        print('print all the position: ' + message[:])


        # escaping a character:
        print("He says \" that\'s fantastic\"!")


        # find all a's in the input word and count how many there are
        lower_message = message.lower()
        print('full lower message is: '+ lower_message)

        print('In the message there are: '+ str(lower_message.count('a'))+ ' times a')

        print('In the message, the word a appears at position: '+ str(lower_message.find('a')))

        print('The total number of character is: '+ str(len(lower_message)))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():

        print(lower_message.replace('a','-'))


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:
        li = list(message.split(' '))
        print(li)

        print(li[0])

        print(li[1])



        # append a new element to the list and print:

        li.append('new element')
        print(li)


        # remove from the list in 3 ways:
        print(li.pop())

        print(li.remove('cake'))

        del li[-1:-2]
        print(li)


        # check if the word cake is in your input list:

        print('cake' in li)


        # reverse the items in the list and print:
        li.reverse()
        print(li)


        # reverse the list with the slicing trick:

        li[::-1]
        print(li)


        # print the list 3 times by using multiplication:
        print(li*3)


tas = Types_and_Strings()
tas.play_with_strings()
tas.play_with_lists()
