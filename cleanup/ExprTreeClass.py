

class Node:

	def __init__(self, val, L = None, R = None, P = None):
		self.value = val
		self.left = L
		self.right = R
		self.parent = P


class ExprTree:

	def __init__(self, expr):