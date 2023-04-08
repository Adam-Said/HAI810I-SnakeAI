import snake
import time
import os

os.system('cls||clear')

TIME_KEY = time.strftime("%Y-%m-%d;%H-%M-%S")

if not os.path.exists("entrainement"):
    os.makedirs("entrainement")

with open(f"entrainement/{TIME_KEY}.txt", "w") as f:
    f.write(TIME_KEY+"\n")
                        
gamma_values = [0.8, 0.9, 0.95]
learning_rate_values = [0.001, 0.01]
hidden_size_values = [256, 512, 1024]
epsilon_nb_games_values = [80, 100, 150]

positive_reward_values = [10, 20]

for gamma in gamma_values:
        for learning_rate in learning_rate_values:
            for hidden_size in hidden_size_values:
                for epsilon_nb_games in epsilon_nb_games_values:

                    with open(f"entrainement/parametres.txt", "w") as f:
                        f.write(f"{TIME_KEY}\n")
                        f.write(f"{gamma}\n")
                        f.write(f"{learning_rate}\n")
                        f.write(f"{epsilon_nb_games}\n")
                        f.write(f"{hidden_size}")

                    with open(f"entrainement/{TIME_KEY}.txt", "a") as f:
                        f.write(f"gamma={gamma};learning_rate={learning_rate};epsilon_nb_games={epsilon_nb_games};hidden_size={hidden_size}\n")
                    
                    start_time = time.time()
                    
                    print(f"\n\nEntrainement avec les parametres : gamma={gamma}, learning_rate={learning_rate}, epsilon_nb_games={epsilon_nb_games}, hidden_size={hidden_size}")
                    snake.trainAgent()

                    total_time = time.time() - start_time
                    print(f"Temps de l'entrainement : {round(total_time)}s")
                    with open(f"entrainement/{TIME_KEY}.txt", "a") as f:
                        f.write(f"total_time={round(total_time)}\n")