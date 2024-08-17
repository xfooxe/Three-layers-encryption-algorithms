import random


# simple diffie-hellman p and g
primes = {
	1: {
		"g": 3,
		"p": 353
	},
	2:{
		"g": 2,
		"p": 4294967291
	},
	3:{
		"g": 2,
		"p": 4294967231
	}
}


class DiffieHellman:
    
	def __init__(self, group, user):
		if group in primes:
			self.p = primes[group]["p"]
			self.g = primes[group]["g"]
		else:
			raise Exception("!Group not existing my library!")

		if user=="A":
			self.__a = random.randint(2, self.p - 1) 
			print(f"Alice's secret key = {self.__a}")
		else:
			self.__a = random.randint(2, self.p - 1)


	#method to generate public key
	def genPublicKey(self):
		#y = G^a mod p
		return pow(self.g, self.__a, self.p)

	#method to generate shared key
	def genSharedKey(self, receiver):
		# shared = yb^a mod p
		self.sharedKey = pow(receiver, self.__a, self.p)
		return self.sharedKey

	# method to convert the integer shared key to letters using chunks
	def convertKey(self, key):
		stringKey = str(key) # Convert key to string
		chunks = [stringKey[i:i+2] for i in range(0, len(stringKey))]  # Split into chunks for str Number length
		intChunks = [int(i) for i in chunks] # Convert chunks to integers
		charList = [chr(97+(i%26)) for i in intChunks] 	# Convert to letters a-z
		k = ''.join(charList) # Join letters into string
		return k

def DH():
		print("Diffie-Hellman exchange key:")
		group = input("Enter group number(1-3): ")

		# Alice
		d1 = DiffieHellman(int(group),"A")
		print(f"p = {d1.p} \ng = {d1.g}")
		d1_PU = d1.genPublicKey()
		print(f"Alice public key = {d1_PU}")

		#Bob
		d2 = DiffieHellman(int(group),"B")
		d2_PU = d2.genPublicKey()
		print(f"Bob public key = {d2_PU}")

		#generate shared key
		sharedkey = d1.genSharedKey(d2_PU)
		print(f"Shared key = {sharedkey}")

		# key after convert to string
		key = d1.convertKey(sharedkey)
		print(f"Shared key after convert: {key}")
		return key





