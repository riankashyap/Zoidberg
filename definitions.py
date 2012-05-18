#!/usr/bin/env python
from term import Term

class Operation:
	ADDITION="+"
	SUBTRACTION="-"
	MULTIPLICATION="*"
	DIVISION="/"
	ALL=["*", "/", "+", "-"]

	class Defs:
		ADDITION=["+"]
		SUBTRACTION=["-"]
		MULTIPLICATION=["*"]
		DIVISION=["/"]

	@staticmethod
	def do(op, t1, t2):
		if op == "+":
			result = t1 + t2
		if op == "-":
			result = t1 - t2
		if op == "*":
			result = t1 * t2
		if op == "/":
			result = t1 / t2
		return Term(Term.VALUE, result)

class Relation:
	EQUIVALENCE="="

	class Defs:
		EQUIVALENCE=["="]
