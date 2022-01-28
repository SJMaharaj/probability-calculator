import copy
import random

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for num in range(value):
                self.contents.append(key)
        print(self.contents)

    def draw(self, number_draw):
        all_draw = []
        if(number_draw > len(self.contents)):
            return self.contents
        else:
            for i in range(number_draw):
                all_draw.append(self.contents.pop(random.randrange(len(self.contents))))

        return all_draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    M = 0
    for j in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        draw_balls = copy_hat.draw(num_balls_drawn)
        copy_expected = copy.deepcopy(expected_balls)

        for items in draw_balls:
            if(items in copy_expected):
                copy_expected[items] -= 1

        if(all(value <= 0 for value in copy_expected.values())):
            M += 1

    probability = M/num_experiments

    return probability
