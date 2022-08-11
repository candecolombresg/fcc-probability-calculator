import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for key in kwargs.keys():
            for i in range(kwargs[key]):
                self.contents.append(key)

    def draw(self, number):
        if number >= len(self.contents):
            return self.contents
        list_draw = []
        for i in range(number):
            index = random.randint(0, len(self.contents)-1)
            list_draw.append(self.contents[index])
            self.contents.pop(index)
        list_draw.sort()
        return list_draw
            

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count=0
    for i in range(num_experiments):
        value = True
        copy_hat = copy.deepcopy(hat)
        balls_drawn = copy_hat.draw(num_balls_drawn)
        for color in expected_balls.keys():
            if expected_balls[color] > balls_drawn.count(color):
                value = False
        if value == True:
            count+=1
    return count/num_experiments

hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)

print(str(probability))