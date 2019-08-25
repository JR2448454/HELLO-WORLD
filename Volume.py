def volumeCube(s_1):
    volCube = s_1**3
    print ("Volume of cube with side ",s_1, "is", volCube)

def volumeCuboid(s_1,s_2,s_3):
    volCuboid = s_1*s_2*s_3
    print ("volume of cuboid with length : ", s_1,", breadth :",s_2,"and height :",s_3, "is =",volCuboid)

def volumeSphere(radius):
    volSphere = 4*(22/7)*(radius**2)
    print ("volume of sphere with radius " , radius , "is :", volSphere)

def volumeCylinder(radius,height):
    volCylinder = (22/7)*(radius**2)*height
    print ("volume of cylinder with radius :", radius,"and height :" ,height, "is =",volCylinder)
