from vpython import *
from scipy import constants
import pygame as pg
from time import sleep

# accurate proportional orbit radius and proportional speeds of orbit calculated from masses


'''
Every point mass attracts every single other point mass by a force acting along the line intersecting both points.
The force is proportional to the product of the two masses and inversely proportional to the square of the distance between them'''

# vector class
class Vect:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vect(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vect(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, scalar):
        return Vect(self.x * scalar, self.y * scalar, self.z * scalar)
    def __truediv__(self, scalar):
        return Vect(self.x / scalar, self.y / scalar, self.z / scalar)
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    def __repr__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + " z: " + str(self.z)
    

class Body:
    def __init__(self, name:str, mass:float, position:Vect, velocity:Vect, radius=5, forceScale = 1e13):
        self.name = name
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = Vect(0, 0, 0)
        self.force = Vect(0, 0, 0)
        self.lastForce = Vect(0, 0, 0)
        self.radius = radius
        self.forceScale = forceScale
    def __repr__(self):
        return "mass: " + str(self.mass) + " position: " + str(self.position) + " velocity: " + str(self.velocity) + " acceleration: " + str(self.acceleration) + " force: " + str(self.force)
    def update(self, dt:float):
        self.acceleration = self.force / self.mass
        self.velocity = self.velocity + self.acceleration * dt
        self.position = self.position + self.velocity * dt
        #reset force
        self.lastForce = self.force
        self.force = Vect(0, 0, 0)
    def addForce(self, force:Vect):
        self.force = self.force + force
    def setForceArrow(self, arrow):
        self.forceArrow = arrow
        self.lastForce = self.lastForce / self.forceScale
        self.forceArrow.axis = vector(self.lastForce.x, self.lastForce.y, self.lastForce.z)
        self.forceArrow.pos = vector(self.position.x, self.position.y, self.position.z)
    def setViewObj(self, viewObj):
        self.viewObj = viewObj
    def updateViewObj(self):
        self.viewObj.pos = vector(self.position.x, self.position.y, self.position.z)
        self.viewObj.radius = self.radius
        self.lastForce = self.lastForce / self.forceScale
        self.forceArrow.axis = vector(self.lastForce.x, self.lastForce.y, self.lastForce.z)
        self.forceArrow.pos = vector(self.position.x, self.position.y, self.position.z)
    def toggleForceArrow(self):
        self.forceArrow.visible = not self.forceArrow.visible

class NBodySystem:
    def __init__(self, bodies:list, t:float, dt:float):
        self.bodies = bodies
        self.t = t # time
        self.dt = dt # time step
        self.G = 6.67e-11 # gravitational constant
        #intertia of body 1 = G*m2*r12/|r12|**2
        #intertia of body 2 = -G*m1*r12/|r12|**2

    def calculateListOfPositions(self, n:float):
        daySec = 24.0 * 60 * 60
        t = 0.0

        listOfPositions = []
        for i in range(len(self.bodies)):
            listOfPositions.append([])
        for i in range(len(self.bodies)):
            self.bodies[i].update(self.dt)
            listOfPositions[i].append((self.bodies[i].position))
        while t < n * daySec:
            for i in range(len(self.bodies)):
                for j in range(len(self.bodies)):
                    if i != j:
                        r = self.bodies[j].position - self.bodies[i].position
                        
                        R = abs(r)
                        modr3 = R**3

                        forceVect = self.G * self.bodies[j].mass * self.bodies[i].mass / modr3
                        forceVect = Vect(forceVect * r.x, forceVect * r.y, forceVect * r.z)

                        self.bodies[i].addForce(forceVect)

            for i in range(len(self.bodies)):
                self.bodies[i].update(self.dt)
                listOfPositions[i].append((self.bodies[i].position))
            t += self.dt
        
        return listOfPositions
    def calculateNextPosition(self):
        for i in self.bodies:
            for j in self.bodies:
                if i != j:
                    r = j.position - i.position
                    
                    R = abs(r)
                    if R > i.radius + j.radius:
                        modr3 = R**3

                        forceVect = self.G * j.mass * i.mass / modr3
                        forceVect = Vect(forceVect * r.x, forceVect * r.y, forceVect * r.z)
                        #print("Force of gravity on " + i.name + " from " + j.name + ":\t" + "{:,.2f}".format(abs(forceVect)/1e6) + " Meganewtons")

                        i.addForce(forceVect)
                    else:
                        print('collision')
                        i.mass += j.mass
                        i.radius = (i.radius**3 + j.radius**3)**(1/3)
                        j.viewObj.visible = False
                        j.toggleForceArrow()
                        self.bodies.remove(j)

        for i in range(len(self.bodies)):
            self.bodies[i].update(self.dt)
        self.t += self.dt
    def updateCenterOfMass(self):
        weightedPos = Vect(0, 0, 0)
        totalMass = 0
        for body in self.bodies:
            weightedPos = weightedPos + body.position * body.mass
            totalMass += body.mass
        self.centerOfMass = weightedPos / totalMass
        self.COMViewObject.pos = vector(self.centerOfMass.x, self.centerOfMass.y, self.centerOfMass.z)
        scene.center = self.COMViewObject.pos
    def setCenterOfMass(self, COMViewObject):
        self.COMViewObject = COMViewObject
    def draw(self):
        positions = []
        radii = []
        for body in self.bodies:
            positions.append(body.position)
            radii.append(body.radius)
        return positions, radii
sunMass = 2.0e30 #kg
earthMass = 6.0e24 #kg
marsMass = 6.6e23 #kg
mercuryMass = 3.3e23 #kg
venusMass = 4.9e24 #kg
jupiterMass = 1.9e27 #kg
saturnMass = 5.7e26 #kg
uranusMass = 8.7e25 #kg
neptuneMass = 1.0e26 #kg

sunPosVect = Vect(0, 0, 0)
earthPosVect = Vect(1*constants.au, 0, 0) #m
marsPosVect = Vect(1.524*constants.au, 0, 0) #m
mercuryPosVect = Vect(0.387*constants.au, 0, 0) #m
venusPosVect = Vect(0.723*constants.au, 0, 0) #m
jupiterPosVect = Vect(5.203*constants.au, 0, 0) #m
saturnPosVect = Vect(9.539*constants.au, 0, 0) #m
uranusPosVect = Vect(19.18*constants.au, 0, 0) #m
neptunePosVect = Vect(30.06*constants.au, 0, 0) #m

sunVelocityVect = Vect(0, 0, 0)
earthVelocityVect = Vect(0, 29.789*1000, 0) #m/s
marsVelocityVect = Vect(0, 24.077*1000, 0) #m/s
mercuryVelocityVect = Vect(0, 47.87*1000, 0) #m/s
venusVelocityVect = Vect(0, 35.02*1000, 0) #m/s
jupiterVelocityVect = Vect(0, 13.07*1000, 0) #m/s
saturnVelocityVect = Vect(0, 9.69*1000, 0) #m/s
uranusVelocityVect = Vect(0, 6.81*1000, 0) #m/s
neptuneVelocityVect = Vect(0, 5.43*1000, 0) #m/s

sun = Body('Sun', sunMass, sunPosVect, sunVelocityVect, constants.au*0.0047)
earth = Body('Earth', earthMass, earthPosVect, earthVelocityVect, constants.au*4.26343e-5)
mars = Body('Mars', marsMass, marsPosVect, marsVelocityVect, constants.au*2.270086e-5)
mercury = Body('Mercury',mercuryMass, mercuryPosVect, mercuryVelocityVect, constants.au*1.63070503e-5)
venus = Body('Venus',venusMass, venusPosVect, venusVelocityVect, constants.au*4.045512e-5)
jupiter = Body('Jupiter',jupiterMass, jupiterPosVect, jupiterVelocityVect, constants.au*0.000477894503)
saturn = Body('Saturn',saturnMass, saturnPosVect, saturnVelocityVect, constants.au*0.000402866697)
uranus = Body('Uranus',uranusMass, uranusPosVect, uranusVelocityVect, constants.au*0.000170851362)
neptune = Body('Neptune',neptuneMass, neptunePosVect, neptuneVelocityVect, 6)

moonMass = 7.3e22 #kg
moonPosVect = Vect(1*constants.au + 208000000, 0, 0) #m
moonVelocityVect = Vect(0, 1.022*1000, 0) #m/s
moonVelocityVect = moonVelocityVect + earthVelocityVect
moon = Body('Moon', moonMass, moonPosVect, moonVelocityVect, constants.au*1.63070503e-5)

blackHoleMass = 2e30 #kg
blackHolePos = Vect(-1*constants.au, 0, 0) #m
blackHoleVelocity = Vect(0, 0, 10.789*1000) #m/s
blackHole = Body(blackHoleMass, blackHolePos, blackHoleVelocity, constants.au*0.0047)

t = 0
dt = 0.03 * 24 * 60 * 60 # 0.01 days

solarSystem = NBodySystem([sun, earth, mars, mercury, venus, jupiter, saturn, uranus, neptune, moon], t, dt)

star1 = Body('Star1', 1e30, Vect(-1*constants.au, 0, 0), Vect(0, 10000, 0), 6.955e8, 1e16)
star2 = Body('Star2', 1e30, Vect(1*constants.au, 0, 0), Vect(0, -10000, 0), 6.955e8, 1e16)
star3 = Body('Star3', 1e30, Vect(0, 1*constants.au, 0), Vect(-10000, 0, 0), 6.955e8, 1e16)

binarySystem = NBodySystem([star1, star2], t, dt)
#listOfPositions = system.calculateListOfPositions(365)


COLORS = [vector(255, 204, 51)/255, vector(140, 177, 222)/255, vector(226, 123, 88)/255, vector(206, 204, 209)/255, vector(165,124,27)/255, vector(144, 97, 77)/255, vector(164, 155, 114)/255, vector(187, 225, 228)/255, vector(62, 84, 232)/255, vector(255, 255, 0)/255]
class vPythonController:
    def __init__(self):
        self.scene = canvas(title='N-Body Simulation', width=1920, height=1080, center=vector(0, 0, 0), background=color.black, range=constants.au*1.5)
    def run_loop(self, NBodySystem:NBodySystem):
        run = True
        NBodySystem.setCenterOfMass(sphere(radius = 9e8, color=color.green, make_trail=True))
        for body in NBodySystem.bodies:
            body.setViewObj(sphere(pos=vector(body.position.x, body.position.y, body.position.z), radius=body.radius, color=COLORS[NBodySystem.bodies.index(body)]))
            attach_trail(body.viewObj, radius=0.1e9, color=COLORS[NBodySystem.bodies.index(body)])
            body.setForceArrow(arrow(shaftwidth=0.8e9, color=color.green))
        while run:
            rate(200)
            for body in NBodySystem.bodies:
                body.updateViewObj()
            NBodySystem.updateCenterOfMass()
            NBodySystem.calculateNextPosition()
            #print(int(NBodySystem.t/60/60/24))


s = vPythonController()
s.run_loop(solarSystem)
