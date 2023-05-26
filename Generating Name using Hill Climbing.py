#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Sp20-bcs-047 
#Talha Azeem
import random
import string

target_name = "Sana"

max_iterations = 10000
mutation_rate = 0.1

# Generate a random starting name
current_name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(len(target_name)))

# Calculateing the fitness
def calculate_fitness(name):
    return sum(a == b for a, b in zip(name, target_name))

# Hill climbing algorithm
for i in range(max_iterations):
    current_fitness = calculate_fitness(current_name)

    if current_fitness == len(target_name):
        print("Target name found:", current_name)
        break

    # Generate a mutated name
    mutated_name = ""
    for char in current_name:
        if random.random() < mutation_rate:
            mutated_name += random.choice(string.ascii_uppercase + string.ascii_lowercase)
        else:
            mutated_name += char

    # Calculateing the fitness
    mutated_fitness = calculate_fitness(mutated_name)

    if mutated_fitness > current_fitness:
        current_name = mutated_name

if i == max_iterations - 1:
    print("Target name not found.")


# In[ ]:




