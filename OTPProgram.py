#!/usr/bin/python3

OTPfile = open('6DigitOTP.txt', 'w')

for i in range(0, 1000000):
	if len(str(i)) == 5:
		OTPfile.write('0' + str(i) + '\n')
	if len(str(i)) == 4:
		OTPfile.write('00' + str(i) + '\n')
	if len(str(i)) == 3:
		OTPfile.write('000' + str(i) + '\n')
	if len(str(i)) == 2:
		OTPfile.write('0000' + str(i) + '\n')
	if len(str(i)) == 1:
		OTPfile.write('00000' + str(i) + '\n')
	else:
		OTPfile.write(str(i) + '\n')

OTPfile.close()