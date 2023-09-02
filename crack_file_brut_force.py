import random
import string
import sys
import time

import msoffcrypto

x = 1
length = random.randint(1, 5)

# create a variable who contains all characters
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = digits + special_chars + letters

chaine = str()

# make a function who test to open the file with the password
def test(chaine , begin):
    # define the file to open
    with open('locked.docx', "rb") as f:
            try:
                # try to open the file
                file = msoffcrypto.OfficeFile(f)
                file.load_key(password=chaine, verify_password=True)  # Use password
                print("File Opened With: " + chaine)
                # print the time took to open the file
                end = time.time()
                print(f'time : {end - begin}')
                # close the python programme
                sys.exit()
            except:
               print(chaine)


def brute_force():

    # start the chronometer
    begin = time.time()

    # try to open the file with one character, test all characters contains in alphabets
    for l in alphabet:
        chaine = l
        test(chaine, begin)

    # try to open the file with two characters
    for l in alphabet:
        chaine = l
        test(chaine, begin)

        for l2 in alphabet:
            chaine = l + l2
            test(chaine, begin)

    # try to open the file with three characters
    for l in alphabet:
        chaine = l
        test(chaine, begin)

        for l2 in alphabet:
            chaine = l + l2
            test(chaine, begin)

            for l3 in alphabet:
                chaine = l + l2 + l3
                test(chaine, begin)

    # try to open the file with four characters
    for l in alphabet:
        chaine = l
        test(chaine, begin)

        for l2 in alphabet:
            chaine = l + l2
            test(chaine, begin)

            for l3 in alphabet:
                chaine = l + l2 + l3
                test(chaine, begin)

                for l4 in alphabet:
                    chaine = l + l2 + l3 + l4
                    test(chaine, begin)

    # try to open the file with five characters
    for l in alphabet:
        chaine = l
        test(chaine, begin)

        for l2 in alphabet:
            chaine = l + l2
            test(chaine, begin)

            for l3 in alphabet:
                chaine = l + l2 + l3
                test(chaine, begin)

                for l4 in alphabet:
                    chaine = l + l2 + l3 + l4
                    test(chaine, begin)

                    for l5 in alphabet:
                        chaine = l + l2 + l3 + l4 + l5
                        test(chaine, begin)


        print('finish')
brute_force()