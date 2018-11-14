# Subsitution Cipher. 

import garbage

ref = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"			# Reference Text.
key = "qazwsxedcrfvtgbyhnujmikolp QAZWSXEDCRFVTGBYHNUJMIKOLP7410258963"			# User Defined Key.
k = len(key)

# A function for Encryption.
def encrypt_S():
	#plain_text = input("Enter Words to Encrypt: ")
	cipher_text_output = ''
	for letters in plain_text:
		s = ref.index(letters)
		cipher_text_output = cipher_text_output + key[s]
	garbage.clrscr()
	print('Your Encrypted text is: ')
	return cipher_text_output
	output_file.write(cipher_text_output)	

# A function for Decryption.	
def decrypt_S():
	#cipher_text = input("Enter Words to Dncrypt: ")
	plain_text_output = ''
	for letters in cipher_text:
		s = key.index(letters)
		plain_text_output = plain_text_output + ref[s]
	garbage.clrscr()
	print('Your Decrypted Text is: ')
	return plain_text_output 
	output_file.write(plain_text)
	


# Fuction performed by option.
#def user_opt(option):

	
# File Inputs.	
name = input('File Name: ')
input_file = open(name, 'r')
words = input_file.read()
output_file = open('output_result.txt', 'w')

option = int(input("What you want to do: \n1. Encrypt: \n2. Decrypt: \n "))
#print(user_opt(option))
print(option)

if option == 1:
	plain_text = words
	print(encrypt_S())

elif option == 2:
	cipher_text = words
	print(decrypt_S())
	
"""if option == 1:
	output_file = open('encrypted_result.txt', 'w')	
elif option == 2:
	output_file = open('decrypted_result.txt', 'w')		
"""		

# Diplaying Options to User.	
