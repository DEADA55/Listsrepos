import time as t

da_list = ["hello", 110, ["No", "Yes"], "people", True, "%", False]
word = "Superkalafragalisticexpealadocious"
user_list = []
num_list = [2, 6, 10, 14, 18, 22]

print("Printing the Developers List...")
t.sleep(2)
print(da_list)
t.sleep(2)
print("Printing list line by line")
t.sleep(2)
print(da_list[0])
t.sleep(1)
print(da_list[1])
t.sleep(1)
print(da_list[3])
t.sleep(1)
print(da_list[4])
t.sleep(1)
print(da_list[5])
t.sleep(1)
print(da_list[6])
t.sleep(2)
print("Printing Developers nested list...")
t.sleep(2)
print(da_list[2])
t.sleep(2)
print("Printing Nested List by line...")
t.sleep(2)
print(da_list[2][1])
t.sleep(1)
print(da_list[2][0])
t.sleep(2)
print("The developer has a word list...")
t.sleep(2)
print(word)
t.sleep(2)
print("Lets print it without a certain letter, lets try a...")
t.sleep(2)
wds = word.split('a')
print (wds)
t.sleep(2)
print("Now lets get rid of the o...")
abc = word.split('o')
t.sleep(2)
print(abc)
t.sleep(2)
print("Lets break it up letter by letter")
xs = list("Superkalafragalisticexpialadocious")
t.sleep(2)
print(xs)
t.sleep(2)
print("We also have a Number List")
t.sleep(1)
print(num_list)
t.sleep(2)
print("Lets do these to the power of 2.")
t.sleep(2)
num_list2 = [item ** 2 for item in num_list]
print(num_list2)
t.sleep(2)
print("Now lets put these numbers to the power of 3!")
t.sleep(2)
num_list3 = [item ** 3 for item in num_list2]
print(num_list3)
t.sleep(2)
print("Lets print these line by line.")
t.sleep(2)
for anum_list3 in num_list3:
    print(anum_list3)
t.sleep(2)
print("lets delete the last item from our list.")
t.sleep(2)
lastitem = num_list3.pop()
print(lastitem)
print(num_list3)
t.sleep(2)
for anum_list3 in num_list3:
    print(anum_list3)
t.sleep(2)
print("Now lets get rid of a specific item")
t.sleep(2)
num_list3.remove(64)
print(num_list3)
t.sleep(2)
print("Can you guess whats missing?")
t.sleep(2)
print("Its 64 duh...")
t.sleep(2)
print("lets put a number in the middle.")
t.sleep(2)



t.sleep(2)
print("Okay, no more of the developers lists, screw him, let's make some of your own.")
x = True
while x == True:
	print("would you like to add something to your list?")
	answer = raw_input("> ")
	if answer == "yes":
		t.sleep(2)
		print("What would you like to add?")
		item = raw_input("> ")
		user_list.append(item)
		t.sleep(2)
		print("Your list is now:", user_list)
	else:
		t.sleep(2)
		x = False
		

print("Is there anything you would like to delete?")
t.sleep(2)
delete = raw_input("> ")
if delete == "yes":
	x = True
	while x == True:
		print("Would you like to continue?")
		cont = raw_input("> ")
		if cont == "yes":
			print("What would you like to delete?")
			item = raw_input("> ")
			if item in user_list:
					user_list.remove(item)
					print("Your list is now:", user_list)
			else:
				print("Item not found in list")
				t.sleep(2)
				print("Your list is now:", user_list)
		else:
			print("Goodbye!")
			x = False
		
else:
	print("Okay goodbye now")
		














