import math
import numpy
from numpy.random import seed
from numpy.random import shuffle
map=numpy.zeros((6,6))
ant_map=numpy.zeros((8,8))

def placeAntennas(i,j,map):
    map[i+1][j+1]=1
    map[i+1][j]=1
    map[i+1][j+2]=1
    map[i+2][j+1]=1
    map[i][j+1]=1
    return map


def calculateFitness(AntennaMap):
    sum=0;
    size=numpy.shape(AntennaMap); rows=size[0];cols=size[1]

    for i in range(rows):
        for j in range(cols):
            if AntennaMap[i][j]:
                sum=sum+1
    return sum
def SetMat(x):
   new=numpy.delete(x,(0,7),0)
   new=numpy.delete(new,(0,7),1)
   return new
def randomGene():
    x=numpy.random.randint(6)
    y=numpy.random.randint(6)
    return [x,y]
def randomChromosome():
    arr=[]
    for i in range(5):
            arr.append(randomGene())
    return arr

def T_Chromosome():
    t_arr=[]
    for i in range(20):
        t_arr.append(randomChromosome())
    return t_arr

def AlgoStart():
    #gen 1
    FitnessArr=[]
    InitialPopulation = T_Chromosome()

    print(InitialPopulation)
    InitialArr=[]

    for a in range(1000):

        for i in InitialPopulation:
            # print(i)
            map1 = numpy.zeros((8, 8))
            for j in i:
                temp=placeAntennas(j[0],j[1],map1)
            temp1=SetMat(temp)
            FitnessArr.append(calculateFitness(temp1))
            print("This is temp1")
            print(temp1)
            # print(calculateFitness(temp1))
            # print(temp1,i)
            InitialArr.append([i,calculateFitness(temp1)])

        InitialArr.sort(key=SortySort, reverse=True)

        ##Selecting Initial Best 10
        BestTen=InitialArr[0:12]
        LastTen=InitialArr[12:20]
        #Printing Last ten arr element

        print("Before CrossOver")
        for i in LastTen:
            print(i)
        #CrossOver Code
        for i in range(4):
            print(((LastTen[i])[0])[4])
            temp1=((LastTen[2*i])[0])[4]
            ((LastTen[2*i])[0])[4]= ((LastTen[2*i+1])[0])[3]
            ((LastTen[2 * i + 1])[0])[3]=temp1

            temp2=((LastTen[2*i])[0])[3]
            ((LastTen[2 * i])[0])[3] = ((LastTen[2 * i + 1])[0])[4]
            ((LastTen[2 * i + 1])[0])[4] = temp2
        print("After Crossover")
        for i in LastTen:
            print(i)
        ##Mutation:
        for i in range(4):
            (((LastTen[2 * i])[0])[1])[0]=numpy.random.randint(6)
            (((LastTen[2 * i])[0])[1])[1] = numpy.random.randint(6)

            (((LastTen[2 * i])[0])[0])[0] = numpy.random.randint(6)
            (((LastTen[2 * i])[0])[0])[1] = numpy.random.randint(6)

        print("After Mutation")
        for i in LastTen:
            print(i)

        ##Calculating Fitness again

        NewPopulation=[]
        for i in range(12):
            NewPopulation.append(((BestTen[i])[0]))
        for i in range(8):
            NewPopulation.append(((LastTen[i])[0]))


        InitialPopulation=NewPopulation
        # print("Thats Best ten")
        # print(len(LastTen))
        #
        # print("ENDYYY In")
        # for i in InitialPopulation:
        #     print(i)
        # print("ENDY NEW")
        # for i in NewPopulation:
        #     print(i)




















    return InitialArr
def SortySort(val):
    return val[1]

# ant_map=numpy.zeros((8,8))
#
# ant_map=placeAntennas(0,0,ant_map)
# ant_map=placeAntennas(0,5,ant_map)
# abc=SetMat(ant_map)
# fitnes=calculateFitness(abc)

x=AlgoStart()

















