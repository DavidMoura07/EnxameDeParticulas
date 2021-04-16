import math
import constants
from utils import setInRange
from random import random


class Particle:
    def __init__(self, x, y, velocity):
        self.x = 0
        self.y = 0
        self.velocity = [0, 0]
        self.fitness = 0

        self.setX(x)
        self.setY(y)
        self.setVelocity(velocity)
        self.pBest = [self.x, self.y]

    def setX(self, x):
        xRange = constants.X_RANGE
        self.x = setInRange(x, xRange)
        if(self.x == xRange[0] or self.x == xRange[1]):
            self.velocity = [0, 0]

    def getX(self):
        return self.x

    def setY(self, y):
        yRange = constants.Y_RANGE
        self.y = setInRange(y, yRange)
        if(self.y == yRange[0] or self.y == yRange[1]):
            self.velocity = [0, 0]

    def getY(self):
        return self.y

    def getPosition(self):
        return [self.getX(), self.getY()]

    def setPosition(self, position):
        self.setX(position[0])
        self.setY(position[1])

    def setVelocity(self, velocity):
        vRange = constants.V_RANGE
        vX = setInRange(velocity[0], vRange)
        vY = setInRange(velocity[1], vRange)
        self.velocity = [vX, vY]

    def getVelocity(self):
        return self.velocity

    def setPBest(self, pBest):
        self.pBest = pBest

    def getPBest(self):
        return self.pBest

    def setFitnessValue(self, fitnessValue):
        self.fitness = fitnessValue

    def getFitnessValue(self):
        return self.fitness

    def printParticle(self):
        # print("Position: [", self.getX(), ",", self.getY(), "]")
        # print("Velocity: ", self.getVelocity())
        # print("Best Position: [", self.getPBest()
        #       [0], ",", self.getPBest()[1], "]")
        # print("Fitness Value: ", self.getFitnessValue())

        print("[", self.getX(), ",", self.getY(), "]; ", self.getVelocity(), "; [", self.getPBest()
              [0], ",", self.getPBest()[1], "]; ", self.getFitnessValue())


# particle = Particle(0, 0, 0)
# particle.printParticle()
