import Area as c
import Volume as a

def Finished():
    print("~"*20,"Have You Finished Your Work ?","~"*20)
    Ans =input('Enter Yes or No :')
    if Ans == "Yes" or Ans == "yes" or Ans == "YES":
        print("Thank You For Using Our Calculator")

    elif Ans == "No" or Ans == "NO" or Ans == "no":
        print("Select Again")
        print("~"*50)
        AreaVolume()

    else :
        print("Sorry!!! You Have Selected A Wrong Input!!!")
        print("Select Again")
        print("~"*50)
        Finished()
        
def AreaVolume():
    print("~"*20,"Welcome TO Area $ Volume calculator","~"*20)
    print("1 = area of Square")
    print("2 = area of Circle")
    print("3 = area of Rectangle")
    print("4 = area of Triangle")
    print("5 = volume of Cube")
    print("6 = volume of Cuboid")
    print("7 = volume of Sphere")
    print("8 = volume of Cylinder")
    num = (input("Enter The Number Corresponding To The Operation You Want To Perform :"))

    
    if num == '1':
        print("~"*20,"You Have Selected Area Of Square","~"*20)
        side =float(input("Enter The Side Of Square :"))
        c.areaSquare(side)

        Finished()

    elif num == '2':
        print("~"*20,"You Have Selected Area Of Circle","~"*20)
        radius =float(input("Enter The Radius Of Circle :"))
        c.areaCircle(radius)

        Finished()

    elif num == '3':
        print("~"*20,"You Have Selected Area Of Rectangle","~"*20)
        s_1 =float(input("Enter The Length Of Rectangle :"))
        s_2 =float(input("Enter The Breadth Of Rectangle :"))
        c.areaRectangle(s_1,s_2)

        Finished()

    elif num == '4':
        print("~"*20,"You Have Selected Area Of Triangle","~"*20)
        s_1 =float(input("Enter The Base Of Triangle :"))
        s_2 =float(input("Enter The Height Of Triangle :"))
        c.areaTriangle(s_1,s_2)

        Finished()

    elif num == '5':
        print("~"*20,"You Have Selected Volume Of Cube","~"*20)
        s_1 =float(input("Enter The Side Of Cube :"))
        a.volumeCube(s_1)

        Finished()

    elif num == '6':
        print("~"*20,"You Have Selected volume Of Cuboid","~"*20)
        s_1 =float(input("Enter The Length Of Cuboid :"))
        s_2 =float(input("Enter The Breadth Of Cuboid :"))
        s_3 =float(input("Enter The Height Of Cuboid :"))
        a.volumeCuboid(s_1,s_2,s_3)

        Finished()

    elif num == '7':
        print("~"*20,"You Have Selected Volume Of Sphere","~"*20)
        s_1 =float(input("Enter The Radius Of Sphere :"))
        a.volumeSphere(s_1)

        Finished()

    elif num == '8':
        print("~"*20,"You Have Selected Volume Of Cylinder","~"*20)
        s_1 =float(input("Enter The Radius Of Cylinder :"))
        s_2 =float(input("Enter The Height Of Cylinder :"))
        a.volumeCylinder(s_1,s_2)

        Finished()

    else :
        print("~"*10,"You have selected an invalid input please try again!!!","~"*10)
        print("Do You Still Wish To Continue???")
        con = input("Enter Yes Or No :")
        if con == "Yes" or con == "yes" or con == "YES":
            print("Select Again")
            AreaVolume()

        elif con == "no" or con == 'NO' or con == "No":
            print("Thank You For Using Our Calculator")
        else :
            print("Sorry!!! You Have Selected A Wrong Input!!!")
            print("Setup Is Restarting")
            print("~"*50)
            AreaVolume()        
            
            
        
AreaVolume()
