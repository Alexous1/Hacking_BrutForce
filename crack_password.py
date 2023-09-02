import random
import string
import sys
import time

from plyer import notification

x = 1
length = random.randint(1, 4)

# create a variable who contains all characters
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

# ask a question if you want a special character
result = input("Veux tu que le mot de passe ait des caractères spéciaux Y/N ")
# if its yes, add special characters
if result == "Y" or result == "y":
    alphabet = letters + digits + special_chars

# if its no, don't add special characters
if result == "N" or result == "n":
    alphabet = letters + digits

# ask if it is you who give the password to find or if it is automatically generated
mode = input("Veux tu que le mot de passe soit generé automatiquement ou que ce soit qui le donne a/b ")

# generate the password
if mode == 'a' or mode == 'A':
    mot = ''
    for i in range(length):
        mot += ''.join(random.choice(alphabet))
    notification.notify(title="ALERT!!!", message=f"LE MOT DE PASSE EST : {mot}", timeout=1)

# keep the password to find
if mode == 'b' or mode == 'B':
    mot = input("Donnez un mot de passe avec 5 caractère maximum ")
    print(mot)


space = " "
chaine = str()
call_counter = 0

def test(chaine ,mot, begin):
    # add 1 to the var nb test
    global call_counter
    call_counter += 1
    # if the chaine is equal to password print the password and stop the timer
    if chaine == mot:
        print('Le mot de passe est : ' + chaine)
        end = time.time()
        print(f'time : {end - begin}')
        print(f'Nb tentative : {call_counter}')
        sys.exit()


def brute_force():

    begin = time.time()

    # try to open the file with one character
    for l in alphabet:
        chaine = l
        test(chaine, mot, begin)

    # try to open the file with two characters
    for l in alphabet:
        chaine = l
        test(chaine, mot, begin)

        for l2 in alphabet:
            chaine = l + l2
            test(chaine, mot, begin)

    # try to open the file with three characters
    for l in alphabet:
        chaine = l
        test(chaine, mot, begin)

        for l2 in alphabet:
            chaine = l + l2
            test(chaine, mot, begin)

            for l3 in alphabet:
                chaine = l + l2 + l3
                test(chaine, mot, begin)

    # try to open the file with four characters
    for l in alphabet:
        chaine = l
        test(chaine, mot, begin)

        for l2 in alphabet:
            chaine = l + l2
            test(chaine, mot, begin)

            for l3 in alphabet:
                chaine = l + l2 + l3
                test(chaine, mot, begin)

                for l4 in alphabet:
                    chaine = l + l2 + l3 + l4
                    test(chaine, mot, begin)


    # try to open the file with five characters
    for l in alphabet:
        chaine = l
        test(chaine, mot, begin)

        for l2 in alphabet:
            chaine = l + l2
            test(chaine, mot, begin)

            for l3 in alphabet:
                chaine = l + l2 + l3
                test(chaine, mot, begin)

                for l4 in alphabet:

                    chaine = l + l2 + l3 + l4
                    test(chaine, mot, begin)

                    for l5 in alphabet:
                        chaine = l + l2 + l3 + l4 + l5
                        test(chaine, mot, begin)
brute_force()