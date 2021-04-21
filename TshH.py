from __future__ import absolute_import
from __future__ import print_function
from six.moves import range
from six.moves import input

import sys 
print('''░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
░  ▒     ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░          ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒       ░░     ░     ░░   ░
░ ░         ░        ░  ░   ░        ░ ░        ░     ░  ░   ░
░                         ░                    ░
''')

heart = '🔒'

print("شفر كلامك بأمان  "+heart+"", file=sys.stderr)

print('')
print('تشفير أضغط رقم [1]')
print('فك الشفير أضغط رقم [2]')

xor = input('أدخل : ')

def crypt():
	
	key  = int(input('مفتاح : '))
	def xor_func( str, key ):
		encript_str = ""
		for letter in str:
			encript_str += chr( ord(letter) ^ key )
		return  encript_str
	strg = input('رسالة : ')
	encr_strg = xor_func( strg, key )
	print(( " DonE ☠️ ", encr_strg ))

def decrypt():
	
	print( '[1] فتح الشفرة')
	print( '[2] التخمين علي الرسالة المشفرة')
	brute = str(input('=>> '))
	if brute == 'one key' or brute == '1':
		
		encrypt = input('  الرساله المشفرة :  ')
		l = int(input('مفتاح الشفرة  : '))
		decrypt=""
		for i in range(l,l+1):
			decrypt = ""
			for j in range(len(encrypt)):
				decrypt += chr(ord(encrypt[j]) ^ i)
			print(('>>> ',decrypt))	
	elif brute == 'التخمين' or brute == '2':
		
		encrypt = input('أدخل الرساله المشفرة : >>> ')
		l = int(input('أدخل المفتاح من رقم واحد: '))
		m = int(input('أدخل المفتاح من رقمين : '))
		decrypt=""
		print( "Key\t\tDecrypted")
		
		for i in range(l,m + 1):
			decrypt = ""
			for j in range(len(encrypt)):
				decrypt += chr(ord(encrypt[j]) ^ i)
			
			print((i, "☠️", decrypt))
	else:
		
		print(' ERROR Wrong input')


if xor == 'crypted' or xor == '1':
	crypt()
	
elif xor == 'decrypted' or xor == '2':
	decrypt()
	
else:
	print(' ERROR Wrong input')

