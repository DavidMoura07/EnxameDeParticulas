import math
import constants
from Particle import Particle
import random


def f(x, y):
    return -(y+47) * math.sin(math.sqrt(abs((x/2) + (y+47)))) - x * math.sin(math.sqrt(abs(x - (y+47))))


def calculateFitnessValue(position):
    x = position[0]
    y = position[1]
    return f(x, y)


def calculateBestPosition(particle):
    actualPosition = particle.getPosition()
    bestPosition = particle.getPBest()

    fitnessActual = calculateFitnessValue(actualPosition)
    bestFitness = calculateFitnessValue(bestPosition)

    if(fitnessActual < bestFitness):
        return actualPosition
    return bestPosition


def getBestParticle(population):
    population.sort(
        key=lambda particle: particle.getFitnessValue())
    return population[0]


def subPositions(posA, posB, c=1):
    a = (posA[0] - posB[0]) * c
    b = (posA[1] - posB[1]) * c
    return [a, b]


def sumPositions(posA, posB, c=1):
    a = (posA[0] + posB[0]) * c
    b = (posA[1] + posB[1]) * c
    return [a, b]


def updateVelocity(particle, gBest):
    actualPosition = particle.getPosition()
    bestPosition = particle.getPBest()
    bestParticlePosition = gBest.getPosition()

    phi1 = random.uniform(0.0, 1.0) * constants.C1
    phi2 = random.uniform(0.0, 1.0) * constants.C2
    newVelocity = sumPositions(
        subPositions(bestPosition, actualPosition, phi1),
        subPositions(bestParticlePosition, actualPosition, phi2)
    )
    return newVelocity


def updatePosition(particle):
    velocity = particle.getVelocity()
    position = particle.getPosition()
    return sumPositions(position, velocity)


def main():
    # Determine o número de partículas P da população.
    particlesAmount = constants.POPULATION_SIZE

    population = []
    iterations = constants.ITERATIONS
    xRange = constants.X_RANGE
    yRange = constants.Y_RANGE
    vRange = constants.V_RANGE

    # Atribua uma velocidade inicial (v) igual para todas as partículas.
    vX = random.uniform(vRange[0], vRange[1])
    vY = random.uniform(vRange[0], vRange[1])
    initialVelocity = [vX, vY]

    # Inicialize aleatoriamente a posição inicial (x) de cada partícula p de P.
    for seq in range(particlesAmount):
        x = random.randint(xRange[0], xRange[1])
        y = random.randint(yRange[0], yRange[1])
        particle = Particle(x, y, initialVelocity)
        population.append(particle)

    for iteration in range(iterations):
        # Se condição de término não for alcançada
        for particle in population:
            # Calcule sua aptidão fp = f (p).
            fitnessValue = calculateFitnessValue(particle.getPosition())
            particle.setFitnessValue(fitnessValue)

            # Calcule a melhor posição da partícula p até o momento (pΒ).
            bPosition = calculateBestPosition(particle)
            particle.setPBest(bPosition)

        # Descubra a partícula com a melhor aptidão de toda a população (gΒ).
        bParticle = getBestParticle(population)

        for particle in population:
            # Atualize a velocidade da partícula
            newVelocity = updateVelocity(particle, bParticle)
            particle.setVelocity(newVelocity)

            # Atualize a posição da particula
            newPosition = updatePosition(particle)
            particle.setPosition(newPosition)

        # print("\n\n\n")
        # print("ITERATION ", iteration)
        # for particle in population:
        #     print("############")
        #     particle.printParticle()

    print("Population result: \n")
    for particle in population:
        print("############")
        particle.printParticle()


main()
