import random
from statistics import median

class Ant():
    name = 'name'
    position = 0
    direction = 'direction'

    def __init__(self, name, direction, position):
        self.name = name
        self.direction = direction
        self.position = position

    def end_of_life(self):
        if self.position <= 0 or self.position >= 100:
            self.name = 'dead'

def kill_ants():
    if ant_list:
        for ant in ant_list[:]:
            if ant.name == 'dead':
                ant_list.remove(ant)
    else:
        return 'all gone'
    
def go_ants_go():
    for ant in ant_list:
        new_position = ant.position + 1 if ant.direction == 'right' else ant.position - 1
        current_direction = ant.direction
        for other_ant in ant_list:
            if other_ant != ant and other_ant.position == new_position and ant.direction != other_ant.direction:
                ant.direction, other_ant.direction = other_ant.direction, ant.direction                    
                break
        if ant.direction == current_direction:
            ant.position = new_position

    for ant in ant_list:
        ant.end_of_life()        

cycles_list = []
for i in range(100):
    ant_list = []
    for i in range(24):
        name = str(i)
        direction = 'left' if random.randint(0, 1) == 0 else 'right'
        position = random.randint(1, 99)
        new_ant = Ant(name, direction, position)
        ant_list.append(new_ant)
    cycles = 0
    while kill_ants() != 'all gone':
        go_ants_go()
        cycles += 1
    cycles_list.append(cycles)

print(max(cycles_list))
print(min(cycles_list))
print(median(cycles_list))
print(cycles_list)
