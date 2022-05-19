import random
import array
max_len=12
digits=['0','1','2','3','4','5','6','7','8','9']
upper_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_case=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','%','^','&','*']
combined_list= digits + upper_case + lower_case + symbols
rand_digit = random.choice(digits)
rand_upcase = random.choice(upper_case)
rand_lowcase = random.choice(lower_case)
rand_symbols = random.choice(symbols)
temp_pass = rand_digit + rand_upcase + rand_lowcase + rand_symbols
for x in range(max_len - 4):
	temp_pass = temp_pass + random.choice(combined_list)
	temp_pass_list = array.array('u',temp_pass)
	random.shuffle(temp_pass_list)
password=""
for x in temp_pass_list:
	password=password + x
print(password)
