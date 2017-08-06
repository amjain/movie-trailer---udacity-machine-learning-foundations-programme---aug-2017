class Parent():
	def __init__(self, colour, eye):
		print ("parent constructor is called")
		self.colour = colour
		self.eye = eye

class Child(Parent):
	def __init__(self, colour, eye, toys):
		print ("child constructor is called")
		Parent.__init__(self, colour, eye)
		self.toys = toys

norton = Parent("brown", "blue")
#print (norton.eye)

#baby_norton = Child("black", "brown", "3")
#print (baby_norton.toys)
