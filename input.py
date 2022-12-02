# game environment parameters
width = 540
height = 540
block_length = 20
brainLayer = [24, 18, 4]  # neural network layers that act as brain of snake
                          #24 = 8 directions x distance to wall, apple, body part  

# genetic algorithm parameter
population_size = 500
no_of_generations = 50
per_of_best_old_pop = 10.0  # percent of best performing parents to be included
per_of_worst_old_pop = 1.0  # percent of worst performing parents to be included
mutation_percent = 7.0
mutation_intensity = 0.01

# Run genetics.py --output saved/test.pickle 
# Run game.py --input saved/test.pickle to start game