from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:

	def __init__(self):
		self.nextAvailableID = 0
		self.parents = {}
		for i in range(c.populationSize):
			self.parents[i] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID += 1

	def Evolve(self):
		for key in self.parents:
			self.parents[key].Evaluate("GUI")

	def Evolve_For_One_Generation(self):
		self.Spawn()

		self.Mutate()

		self.child.Evaluate("DIRECT")

		self.Print()

		#exit(" -- EXIT from solution.Evolve_For_One_Generation")

		self.Select()

	def Spawn(self):
		self.child = copy.deepcopy(self.parent)
		self.child.setID(self.nextAvailableID)
		self.nextAvailableID += 1

	def Mutate(self):
		self.child.Mutate()
		#print(self.parent.weights)
		#print(self.child.weights)
		#exit("-- EXIT from Solution.Mutate")


	def Select(self):
		#print(self.parent.fitness)
		#print(self.child.fitness)
		#exit(" -- EXIT from hillclimber.select")
		if(self.parent.fitness > self.child.fitness):
			self.parent = self.child

	def Print(self):
		print("Parent Fitness = " + str(self.parent.fitness) + ", Child Fitness = " + str(self.child.fitness))

	def Show_Best(self):
		pass