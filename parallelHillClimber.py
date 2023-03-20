from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

	def __init__(self):
		os.system("rm brain*.nndf")
		os.system("rm fitness*.txt")

		self.nextAvailableID = 0
		self.parents = {}
		for i in range(c.populationSize):
			self.parents[i] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID += 1

	def Evolve(self):
			self.Evaluate(self.parents)
			for currentGeneration in range(c.numberOfGenerations):
				self.Evolve_For_One_Generation()


	def Evolve_For_One_Generation(self):
		self.Spawn()

		self.Mutate()

		self.Evaluate(self.children)

		# self.Print()

		# #exit(" -- EXIT from solution.Evolve_For_One_Generation")

		# self.Select()

	def Spawn(self):
		self.children = {}
		for key in self.parents:
			self.children[key] = copy.deepcopy(self.parents[key])
			self.children[key].Set_ID(self.nextAvailableID)
			self.nextAvailableID += 1

	def Mutate(self):
		for key in self.children:
			self.children[key].Mutate()

	def Evaluate(self, solutions):
		for key in solutions:
			self.parents[key].Start_Simulation("DIRECT")

		for key in solutions:
			self.parents[key].Wait_For_Simulation_To_End()


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