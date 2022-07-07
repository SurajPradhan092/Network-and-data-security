from imghdr import what
from ntpath import join
import string 

alphabets = string.ascii_lowercase + string.ascii_lowercase

sentence = list(input('enter your text: \n').lower())

what_to_do = input( 'enter enc to ENCRYPT, dec to DECRYPT, exit to EXIT the program \n').lower()

shift_number =  3

end_program = False

while not end_program:
    #search through the enter text
    if what_to_do =='enc':
        for i in range(len(sentence)):
            #get the position of each character within the sentence
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                    new_letter = alphabets.index(sentence[i])+shift_number
                    sentence[i] = alphabets[new_letter]
        #convert the list back to a string
        print(''.join(map(str,sentence)))
        end_program = True
    elif what_to_do == 'dec':
        for i in range(len(sentence)):
            if sentence [i] == '':
                sentence[i] = ''
            else:
               new_letter = alphabets.index(sentence[i])-shift_number
               sentence[i] = alphabets[new_letter]
            #convert the llist back to string

            print(''.join(map(str,sentence)))
            end_program = True
    else:
        decide = input('invalid entry try again y for yes n for no: \n').lover()
        if decide =='y':
            sentence = list(input('enter yput text: \n').lower())
            what_to_do = input('enter enc to ENCRYPT, dec to DECRYPT, exit to EXIT the program \n').lower()
            shift_number = int(input('enter your shift number from 1 to 25; \n'))
        else:
            end_program = True




