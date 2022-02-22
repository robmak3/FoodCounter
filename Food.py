class Food:
    def __init__(self, name = "Food", calories = 0, protein = 0, fiber = 0, probiotic = False):
        self.name = name
        self.calories = calories
        self.protein = protein 
        self.fiber = fiber
        self.probiotic = probiotic

    def OpenFoods(name):
        x = Food()
        try:
            f = open("AppData/foods.csv", 'r')
        except:
            print("Your files have been corrupted")
            print("Repairing/recreating name.csv")
            f = open("AppData/foods.csv", "w")
            f.close()
            return x
        for line in f:
            if line.split(", ")[0] == name:
                a = line.split(", ")
                x = Food(name, int(a[1]), int(a[2]), int(a[3]), str(a[4]) == "True\n")
        return x

    def SaveFood(self):
        f = open("AppData/foods.csv", 'a')
        f.write(self.name + ", " + str(self.calories) + ", " + str(self.protein) + ", " + str(self.fiber) + ", " + str(self.probiotic) + "\n")
        f.close
        return
        
 #   def __init__(self):
 #       self.name = "Food"
 #       self.calories = 0
 #       self.protein = 0
 #       self.fiber = 0
 #       self.probiotic = False 