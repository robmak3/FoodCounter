import sys
from time import process_time_ns
from Food import Food
from datetime import date

class TodayFood:
 
    def __init__(self):
        self.file_ = "FoodLogs/" + date.today().strftime("%Y-%m-%d") + ".csv"
        self.FoodObjects_ = self.ReadFoodObjects()

    def ReadFoodObjects(self):
        try:
            f = open(self.file_, 'r')
        except:
            return []
        foodObjects = []
        for line in f:
            linearr = line.split(', ')
            foodObjects.append(Food(linearr[0], int(linearr[1]), int(linearr[2]), int(linearr[3]), str(linearr[4]) == "True\n"))
#            print("blah" + linearr[4] + 'blah')
        f.close()
        return foodObjects

    def WriteFoodObjects(self):
        f = open(self.file_, 'w')
        for line in self.FoodObjects_:
 #           print(line.name + " " + str(line.probiotic))
            f.write(line.name + ", " + str(line.calories) + ", " + str(line.protein) + ", " + str(line.fiber) + ", " + str(line.probiotic) + "\n")
        f.close()

    def TotalCalories(self):
        cals = 0
        for i in self.FoodObjects_:
            cals += i.calories
        return cals
    
    def TotalProtein(self):
        prot = 0
        for i in self.FoodObjects_:
            prot += i.protein
        return prot

    def TotalFiber(self):
        fib = 0
        for i in self.FoodObjects_:
            fib += i.fiber
        return fib
    
    def TotalProbiotics(self):
        prob = 0
        for i in self.FoodObjects_:
            if i.probiotic:
                prob += 1
        return prob

    def Totals(self):
        arrtotals = [0, 0, 0, 0]
        for i in self.FoodObjects_:
            arrtotals[0] += i.calories
            arrtotals[1] += i.protein
            arrtotals[2] += i.fiber
            if i.probiotic:
                arrtotals[3] += 1
        return arrtotals
    
    def Flags(self):
        x = self.Totals()
        toRet = ""
        if (x[2] > 45):
            toRet += "You have eaten too much fiber today. DO NOT EAT MORE. "
        else:
            if (x[2] >= 35):
                toRet += "You have eaten enough fiber today, DO NOT EAT MORE. "
            else:
                if (x[2] >= 25):
                    toRet += "You are getting close to fiber limits, do not eat much more fiber"
        return toRet
        