import time
import os
import socket
import psutil
battery = psutil.sensors_battery()
login_pass = open('user/password.txt')
login_name = open('user/username.txt')
l_p = login_pass.read()
l_n = login_name.read()
jls_extract_var = """
████████████████████████████████████
█─▄─▄─█▄─▄▄─█─▄▄▄▄█─▄─▄─█─▄▄─█─▄▄▄▄█
███─████─▄█▀█▄▄▄▄─███─███─██─█▄▄▄▄─█
▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▄▀
"""
print(jls_extract_var)
print("WELCOME " + l_n)
jls_extract_var = "The date is: "
print(jls_extract_var + time.strftime("%d/%m/%Y"))
jls_extract_var = "The time is: "
print(jls_extract_var + time.strftime("%H:%M:%S"))
jls_extract_var = "The battery is: "
print(jls_extract_var + str(battery.percent) + "%")
jls_extract_var = "The battery status is: "
print(jls_extract_var + str(battery.power_plugged))
jls_extract_var = "The battery time is: "
print(jls_extract_var + str(battery.secsleft) + " seconds")
jls_extract_var = """
[1] To Open Google
[2] To Open Text Editor
[3] To Photos Viewer
[4] To Open Confignre and Open BioS
[5] To Open terminal
[6] To Open calculator
[7] To Open File Exploer
[8] To Shutdown
"""
print(jls_extract_var)
jls_extract_var = input
select = jls_extract_var(":")
if select == '1':
    jls_extract_var = "brows.py"
    os.startfile(jls_extract_var)
    jls_extract_var = "home.py"
    os.startfile(jls_extract_var)
    exit()
if select == '2':
    jls_extract_var = "textediter.py"
    os.startfile(jls_extract_var)
    jls_extract_var = "home.py"
    os.startfile(jls_extract_var)
    exit()
if select == '3':
    jls_extract_var = "photos.py"
    os.startfile(jls_extract_var)
    jls_extract_var = "home.py"
    os.startfile(jls_extract_var)
    exit()
if select == '4':
		b_login = input(str("Please Enter The Password To " + l_n + "To Open BioS: "))
		if b_login == l_p:
			print("Opening BioS")
			host_name = socket.gethostname()
			host_ip = socket.gethostbyname(host_name)
			print("[1] USER NAME: " + l_n)
			print("[2] PASSWORD: " + l_p)
			print("Hostname:", host_name)
			print("LOCAL IPS: " + host_ip)
			edit_b = input("Enter [?] to change setting: ")
			if edit_b == '1':
				edit_n = input("Enter New Username: ")
				with open('user/username.txt', 'w') as f:
					f.writelines(edit_n)
				print("Username Changed To " + edit_n)
				input("Press Enter To Restart: ")
				os.startfile('home.py')
				os.system('exit')

			if edit_b == '2':
				edit_p = input("Enter New Password: ")
				with open('user/password.txt', 'w') as f:
					f.writelines(edit_p)

				print("Password Changed To " + edit_p)
				input("Press Enter To Restart: ")
				os.startfile('home.py')
				os.system('exit')
exit()
if select == '5':
	os.startfile('home.py')
	os.startfile('terminal.py')
exit()
if select == '6':
	os.startfile('home.py')
	os.startfile('calc.py')
exit()
if select == '7':
    os.startfile('home.py')
    os.startfile('fileexplorer.py')
if select == '8':
	os.system('exit')
input()
