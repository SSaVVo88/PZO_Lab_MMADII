
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


# %%
class Population:

    def __init__(self, n=100):
         self.specimens = {Creature() for _ in range(n)}
        
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
        {speciemen.kill() for specimen in self.specimens}
        self.history.append(self.n)
        # Usuwamy z populacji zabite stwory 
        self.specimens = {specimen for specimen in self.specimens
                            if specimen.alive}
        

class Creature:
    alive = True  # Atrybut
    p_death = 0.2 
    p_reproduce = 0.2 

    def kill(self): #Metoda
        if random.random() <= self.p_death:
            self.alive = False

    def reproduce(self):
        if random.random() <= self.p_reproduce and self.alive:
            return Creature()


# %%
# random.random?

# %%
population = Population(5)

# %%
population.specimens = set()

# %%
population.n 

# %%
