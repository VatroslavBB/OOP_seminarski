#
# funkcije za validiranje sintakse inputa
#

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


#
# funkcije za izradu stabla proračuna
#

class BoolNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def FindWeakest(func):
    scale = {"|": 1, "&": 2, "!": 3}
    weakest = 5
    index = -1
    parentCnt = 0
    for i in range(len(func)):
        parentCnt += (func[i] == "(")*1 - (func[i] == ")")*1
        if parentCnt == 0 and func[i] in scale:
            if weakest > scale[func[i]]:
                weakest = scale[func[i]]
                index = i
    return index


def MakeTree(func):
    if func.isalnum():
        return BoolNode(func)

    index = FindWeakest(func)
    #case sa zagradama
    if index == -1:
        return MakeTree(func[1:-1])

    newNode = BoolNode(func[index])
    if func[index] == "!":
        newNode.left = None
    else:
        newNode.left = MakeTree(func[:index])
    newNode.right = MakeTree(func[index + 1:])

    return newNode


def CalculateFromTree(root):
	if root == None:
		return

	if root.left == None and root.right == None:
		return int(root.value)

	L = CalculateFromTree(root.left)
	R = CalculateFromTree(root.right)

	if root.value == "&":
		return int(L and R)
	elif root.value == "|":
		return int(L or R)
	elif root.value == "!":
		return int(not R)



#
# funkcije za kreiranje tablice istine
#

def MakeTruthTable(func, var):
	size = len(var)
	sol = [[]]
	if size > 0 and size < 6:
		for v in var:
			sol[0].append(v)
		sol[0].append("f(" + var + ")")

		for i in range(2 ** size):
			combination = [(i >> j) & 1 for j in range(size - 1, -1, -1)]

			F = func
			for j in range(len(F)):
				for k in range(size):
					if F[j] == var[k]:
						F = F[:j] + str(combination[k]) + F[j + 1:]

			root = MakeTree(F)
			row = list(combination)
			row.append(CalculateFromTree(root))

			sol.append(row)

	return sol


#
# funkcije za racunanje minimalne funkcije
#

def NumOfOnes(codeWord):
	cnt = 0
	for bit in codeWord:
		if bit == '1':
			cnt += 1
	return cnt


def CheckDiff(m1, m2):
	diff = 0
	for i in range(len(m1)):
		if m1[i] != m2[i]:
			diff += 1
	return diff


def CombineMinterms(m1, m2):
	combined = ""
	if CheckDiff(m1, m2) == 1:
		for i in range(len(m1)):
			if m1[i] == m2[i]:
				combined += m1[i]
			else:
				combined += "R"
	return combined


def CheckingImplicants(epi, m):
	for i in range(len(m)):
		if not (epi[i] == m[i] or epi[i] == "R"):
			return False
	return True


class Formula:

	def __init__(self, sentence, variables):
		self.sentence = sentence
		self.variables = variables.replace(" ", "")
		self.valid = self.CheckVars() and self.CheckIfValid()
		self.size = NumberOfVars(self.variables)
		
		if self.valid == True:
			self.TT = MakeTruthTable(self.sentence, self.variables)
		else:
			self.TT = [[]]

		
	def CheckVars(self):
		for V in self.variables:
			if not V.isalpha():
				return False
		return len(self.variables) < 6 and len(self.variables) > 0


	def CheckIfValid(self):
		if self.sentence == "!" or self.sentence == "":
			return False
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


	# def CalcTruthTable(self):
	# 	sol = []
	# 	if self.size > 0 and self.size < 6 and self.valid == True:

	# 		func = self.sentence.replace("!", " not ")
	# 		func = func.replace("&", " and ")
	# 		func = func.replace("|", " or ")

	# 		sol = [list(self.variables) + ["f(...)"]]

	# 		wrongReplace = "andort"
	# 		fedUp = False

	# 		for V in self.variables:
	# 			if V in wrongReplace:
	# 				fedUp = True
	# 				break

	# 		#kreiranje kodnih rici
	# 		for i in range(2 ** self.size):
	# 			codeWord = [(i >> j) & 1 for j in range(len(self.variables) - 1, -1, -1)]
				
	# 			funcForThis = func

	# 			if fedUp == True:
	# 				#brine o prvom i zadnjen charu u funkciji
	# 				for j in range(len(self.variables)):
	# 					if funcForThis[0] == self.variables[j]:
	# 						funcForThis = str(codeWord[j]) + funcForThis[1:]
	# 					if funcForThis[-1] == self.variables[j]:
	# 						funcForThis = funcForThis[:-1] + str(codeWord[j])

	# 				#racuna za ostale charove
	# 				for j in range(1, len(funcForThis) - 1, 1):
	# 					for k in range(len(self.variables)):
	# 						if funcForThis[j] == self.variables[k]:
	# 							if funcForThis[j-1] in " ()" and funcForThis[j+1] in " ()":
	# 								funcForThis = funcForThis[:j] + str(codeWord[k]) + funcForThis[j+1:]
	# 			else:
	# 				for j in range(len(self.variables)):
	# 					funcForThis = funcForThis.replace(self.variables[j], str(codeWord[j]))
				
	# 			sol.append(list(codeWord) + list(bin(eval(funcForThis)))[2:])

	# 	return sol


	def CalcMinimal(self):
		#implementacija Quine-Mcluskey metode
		sol = ""
		if self.size > 0 and self.size < 6 and self.valid == True:
			minterms = []
			for row in self.TT:
				if row[-1] == 1:
					minterms.append(''.join(map(str, row[:-1])))

			groups = {}
			for m in minterms:
				groups.setdefault(NumOfOnes(m), []).append(m)

			PI = set()
			EPI = set()
			ALL = set(minterms)

			while groups:
				new = {}
				used = set()
				for G in sorted(groups):
					if G + 1 in groups:
						for m1 in groups[G]:
							for m2 in groups[G + 1]:
								combined = CombineMinterms(m1, m2)
								if combined != "":
									new.setdefault(NumOfOnes(combined), []).append(combined)
									used.add(m1)
									used.add(m2)
									ALL.add(combined)
				for G in groups:
					for m in groups[G]:
						if m not in used:
							PI.add(m)
				groups = {k: list(set(v)) for k, v in new.items()}

			restMinterms = set(minterms)
			while restMinterms:
				C = {}
				for expr in PI:
					C[expr] = 0
					for m in restMinterms:
						if CheckingImplicants(expr, m) == True:
							C[expr] += 1
				epi = max(C, key = C.get)
				EPI.add(epi)
				RM = set()
				for m in restMinterms:
					if CheckingImplicants(epi, m) == False:
						RM.add(m)
				restMinterms = RM

			for epi in EPI:
				for i in range(self.size):
					if epi[i] == "1":
						sol += self.variables[i]
					elif epi[i] == "0":
						sol += "!" + self.variables[i]
					if epi[i] != "R":
						sol += "&"

				sol = sol[:-1]
				sol += " | "

		return sol[:-3]




# INPUT = Formula("p&q|!(r|s|!(t&r))", "pqrst")

# for row in INPUT.TT:
# 	print(*row)

# for row in INPUT.CalcTruthTable():
# 	print(*row)







