import time

class ATM:
	def ben(self):
		f = open("updated.txt", "r+")
		data = float(f.read())
		print("Your Cuurent Balance is :", data)
		f.close()
		print("\n\nRedirect to main menu")
		time.sleep(5)
		self.menu()

	def wdr(self):
		f = open("updated.txt", "r+")
		data = float(f.read())
		withdraw = int(input("Enter the amount:"))
		if withdraw <= data:
			data -= withdraw
			data = str(data)
			f.seek(0)
			f.write(data)
			choice = input("Press Y/y to check balance")
			if choice == "Y" or choice == "y":
				print("Your Acc Balance is:", data)
		else:
			print("Insufficient Fund")
		f.close()
		print("/n/nRedirect")
		time.sleep(3)
		self.menu()


	def add(self):
		f = open("updated.txt", "r+")
		data = float(f.read())
		amount = float(input("Enter the amount to deposit:"))
		data += amount
		data = str(data)
		f.seek(0)
		f.write(data)
		choice = input("Press Y/y")
		if choice == "Y" and choice == "y":
			print("Your Balance is:", data)
		f.close()
		print('\nRedirect')
		self.menu()




	def menu(self):
		print("1. Balance \n2. withdraw \n3. Add Money")
		ch = input("Enter Choice:")
		if ch == '1':
			self.ben()
		elif ch == "2":
			self.wdr()
		elif ch == "3":
			self.add()

print("Insert Card")
time.sleep(4)
print("Card read success")
pin = input("Enter:")
atm = ATM()
atm.menu()