import random
from query import Query
class Binomotron:
    def __init__(self, number_in_group):
        self.people = Query.get_apprenants(self)
        self.number_in_group = number_in_group

    def __call__(self):
        return(self.compute())


    def compute(self):
        crew = {}
        cpt = 0
        random.shuffle(self.people)
        while(len(self.people) >= self.number_in_group):
            cpt+=1
            newarray = []
            for _ in range(self.number_in_group):
                newarray.append(self.people[0])
                self.people.remove(self.people[0])
            crew[cpt] = newarray
        if len(self.people) > 0 :
            crew[cpt+1] = self.people
        return(crew)

