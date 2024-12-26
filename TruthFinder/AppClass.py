

def NumberOfVars(line):
	return len(line)

def IsVar(c, vars):
	for char in vars:
		if c == char:
			return True
	return False

def IsParent(c):
	if c == '(' or c == ')':
		return True
	return False

def IsOperator(c):
	if c == '&' or c == '|' or c == '!':
		return True
	return False

def NextAllowed(prev, vars):
	sieved = []
	if IsVar(prev, vars):
		sieved.append('&')
		sieved.append('|')
	elif IsOperator(prev) or prev == '(':
		for var in vars:
			sieved.append(var)
		sieved.append('(')
		sieved.append('!')
	elif prev == ')':
		sieved.append('&')
		sieved.append('|')

	return sieved


class Formula:

	def __init__(self, sentence, variables):
		self.sentence = sentence
		self.variables = variables.replace(" ", "")
		self.valid = self.CheckVars() and self.CheckIfValid()
		self.size = NumberOfVars(self.variables)
		self.truthtable = self.CalcTT()
		self.veitch = self.CalcVeitch()
		self.minimal = self.CalcMinimal()

		
	def CheckVars(self):
		for V in self.variables:
			if not V.isalpha():
				return False
		return len(self.variables) < 6 and len(self.variables) > 0


	def CheckIfValid(self):
		if self.CheckVars() == True:
			allowed = []
			for var in self.variables:
				allowed.append(var)
			allowed.append('!')
			allowed.append('(')

			char = ' '

			ParentOpen = 0
			ParentOpened = False

			lenSentence = len(self.sentence)

			for i in range(lenSentence):
				char = self.sentence[i]

				if not (IsOperator(char) or IsVar(char, self.variables) or IsParent(char)):
					return False
				
				if char not in allowed:
					return False

				ParentOpen += (char == '(') - (char == ')')
				ParentOpened = (ParentOpen > 0)

				allowed = NextAllowed(char, self.variables)

				if ParentOpen != 0 and ParentOpened == True and (IsVar(char, self.variables) or char == ')'):
					allowed.append(')')

			return ParentOpen == 0 and ParentOpened == False
		return False


	def CalcTT(self):
		sol = []
		if self.size > 0 and self.size < 6 and self.valid == True:

			func = self.sentence.replace("!", " not ")
			func = func.replace("&", " and ")
			func = func.replace("|", " or ")

			sol = [list(self.variables) + ["f(...)"]]

			wrongReplace = "andort"
			fedUp = False

			for V in self.variables:
				if V in wrongReplace:
					fedUp = True
					break

			#COMBINATIONS
			for i in range(2 ** self.size):
				codeWord = [(i >> j) & 1 for j in range(len(self.variables) - 1, -1, -1)]
				
				funcForThis = func

				if fedUp == True:
					#brine o prvom i zadnjom charu u funkciji
					for j in range(len(self.variables)):
						if funcForThis[0] == self.variables[j]:
							funcForThis = str(codeWord[j]) + funcForThis[1:]
						if funcForThis[-1] == self.variables[j]:
							funcForThis = funcForThis[:-1] + str(codeWord[j])

					#racuna za ostale charove
					for j in range(1, len(funcForThis) - 1, 1):
						for k in range(len(self.variables)):
							if funcForThis[j] == self.variables[k]:
								if funcForThis[j-1] in " ()" and funcForThis[j+1] in " ()":
									funcForThis = funcForThis[:j] + str(codeWord[k]) + funcForThis[j+1:]
				else:
					for j in range(len(self.variables)):
						funcForThis = funcForThis.replace(self.variables[j], str(codeWord[j]))
				
				sol.append(list(codeWord) + list(bin(eval(funcForThis)))[2:])

		return sol


	def CalcVeitch(self):
		sol = []
		if self.size > 0 and self.size < 6 and self.valid == True:
			return
		return sol


	def CalcMinimal(self):
		sol = ""
		if self.size > 0 and self.size < 6 and self.valid == True:
			return
		return sol




# INPUT = Formula("p&q|(p|s|!(q&q))", "p q s")


# for r in INPUT.truthtable:
# 	print(*r)























