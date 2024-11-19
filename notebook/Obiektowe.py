# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import random
import matplotlib.pyplot as plt


# %%
class Population:

    def __init__(self, n=100):
         self.specimens = {Creature() for _ in range(n)}
         self.history = []
    @property
    def specimens(self):
        return self._specimens

    @specimens.setter
    def specimens(self, value):
        self._specimens = value 
        self.n = len(value)

    def natural_selection(self):
        # Próbujemy zabić wszystkie stwory (dla każdego odpalamy .kill)
        #for speciemen in self.specimens:
            #speciemen.kill()
        newborns = {specimen.reproduce() for specimen in self.specimens} - {None}
    {specimen.kill() for specimen in self.specimens}
       

        self.history.append(self.n)
        # Usuwamy z populacji zabite stwory 
        self.specimens = {specimen for specimen in self.specimens
                            if specimen.alive} | newborns

    def plot_history(self):
        plt.plot(self.history)

    def plot_histogram(self, parameter): # parameter = 'p_death', na przykład 
       #self.specimens to jest zbiór stworów, a każdy stwór ma swoje p_death
       #Z każdego stwora biorę jego "śmiertelność" -> zbiór śmiertelności
       #i ten zbiór śmiertelności wizualizuje na histogramie
        plt.hist([getattr(specimen, parameter) for specimen in self.specimens])

class Probability:

    def __set_name__(self, owner, name):
        #self.public_name = name  #do wykreslenia 
        self.private_name = '_' + name 

    
    def __get__(self, obj, objtype=None): 
        return getattr(obj, self.private_name) #tutaj powinnia byc dowolna nazwa (np. p_reproduce) private name 
        #będziemy odczytywać wartość zapisaną gdzie indziej
        # wartość będzie zapisana w _p_death
       
       

    def __set__(self, obj, value): #tutaj chcemy pilnować właściwych wartości ( 0 <= value <= 1) 

      setattr(obj, self.private_name, min(1, max(0, value))) #tutaj powinnia byc dowolna nazwa (np. p_reproduce)
        
        #^lepsza wersja 
        #if value < 0:
            #obj._p_death = 0 
        #elif value > 1:
            #obj._p_death = 1
        #else:
            #obj._p_death = value 
            

class Creature:

    sigma = 0.02 
    p_death = Probability()
    p_reproduce = Probability()
    
    def __init__(self, p_death=0.2, p_reproduce=0.2):
        self.p_death = p_death
        self.p_reproduce = p_reproduce
        self.alive = True

    def kill(self): #Metoda
        if random.random() <= self.p_death:
            self.alive = False

    def reproduce(self):
        if random.random() <= self.p_reproduce and self.alive:
            return Creature(p_death=self.p_death + random.gauss(mu=0, sigma=Creature.sigma),
                            p_reproduce=self.p_reproduce + random.gauss(mu=0, sigma=Creature.sigma))


# %%
population = Population()

# %%
population.plot_histogram('p_death')

# %%
for _ in range(50):
    population.natural_selection()

# %%
population.plot_histogram('p_death')

# %%
population.n

# %%
population.history

# %%
population.plot_histogram('p_reproduce')

# %%
population.plot_history()

# %%
