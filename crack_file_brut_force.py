import random
import string
import sys
import time

import msoffcrypto

x = 1
length = random.randint(1, 5)

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = digits

chaine = str()

def test(chaine , begin):
    with open('locked.docx', "rb") as f:
            try:
                file = msoffcrypto.OfficeFile(f)
                file.load_key(password=chaine, verify_password=True)  # Use password
                print("File Opened With: " + chaine)
                end = time.time()
                print(f'time : {end - begin}')
                sys.exit()
            except:
               print(chaine)


def brute_force():

    begin = time.time()

    for l in alphabet:
        chaine = l
        test(chaine, begin)

    for l in alphabet:
        chaine = l
        test(chaine, begin)

        for l2 in alphabet:
            chaine = l + l2
            test(chaine, begin)

    for l in alphabet:
        chaine = l
        test(chaine, begin)

        for l2 in alphabet:
            chaine = l + l2
            test(chaine, begin)

            for l3 in alphabet:
                chaine = l + l2 + l3
                test(chaine, begin)

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