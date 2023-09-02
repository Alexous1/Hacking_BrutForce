import msoffcrypto
import sys
all_passwords = []
running = True
find = False
while running:

    try:  # try to open in 'read mode'
        with open('rockyou.txt', "r") as f:
            # get all line in the file
            lines = f.readlines()
            for line in lines:
                # add all lines in 'all_password'
                all_passwords.append(line.rstrip())  # Use line.rstrip().decode() to convert bytes into strings

    except UnicodeDecodeError:  # opens in 'read binary mode'
        with open('rockyou.txt', "rb") as f:
            # get all line in the file
            lines = f.readlines()
            for line in lines:
                # add all lines in 'all_password'
                all_passwords.append(line.rstrip())  # Use line.rstrip().decode() to convert bytes into strings

    # try to open the file with the password
    with open('locked.docx', "rb") as f:
        # test all passwords contains in 'all_password'
        for this_pass in all_passwords:
            if find == False:
                try:
                    this_pass = str(this_pass, 'utf-8')  # convert binary to utf-8
                except:
                    pass
                try:
                    file = msoffcrypto.OfficeFile(f)
                    file.load_key(password=this_pass, verify_password=True)  # Use password
                    print("File Opened With: " + this_pass)
                    find = True

                except:
                    print("Incorrect Password: " + this_pass)