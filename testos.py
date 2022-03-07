import time
import os

jls_extract_var = """
████████████████████████████████████
█─▄─▄─█▄─▄▄─█─▄▄▄▄█─▄─▄─█─▄▄─█─▄▄▄▄█
███─████─▄█▀█▄▄▄▄─███─███─██─█▄▄▄▄─█
▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▄▀
"""
print(jls_extract_var)


jls_extract_var = """
[1] Contunie with TestOS setup
[2] I Have Already Done TestOS Setup
"""
print(jls_extract_var)
setup = input(":")
if setup == '1':
    name = input(str("Enter your name to display: "))
    pas = input(str("Enter your password to login: "))

    lines = [name]
    with open("user/username.txt", "w") as f:
        f.writelines(name)

    lines4 = [pas]
    with open('user/password.txt', 'w') as f:
        f.writelines(pas)
    print("TESTOS Setup has been Completed!!!")
    time.sleep(2)
    input("Press Enter to close the tab...")
    exit()

if setup == '2':
    login_pass = open('user/password.txt')
    login_name = open('user/username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()

while True:
    login = input(str("Enter your password To " + l_n + ": "))
    if login == l_p:
        os.startfile("home.py")
        break
    else:
        print("Wrong password!")