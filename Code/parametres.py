import snake
import time
import os

try:
    params = [line for line in open(f"parametres.txt", "r")]
    TIME_KEY = int(params[0].strip())
    GAMMA_DISCOUNT_RATE = int(params[1].strip())
    VITESSE_APPRENTISSAGE = int(params[2].strip())
    EPSILON_NB_GAMES = int(params[3].strip())
    HIDDEN_SIZE = int(params[4].strip())

except:
    True


# Tests des meilleurs hyperparamètres
if __name__ == "__main__":

    TIME_KEY = time.strftime("%Y-%m-%d;%H-%M-%S")
    if not os.path.exists("entrainement"):
        os.makedirs("entrainement")

    with open(f"entrainement/{TIME_KEY}.txt", "w") as f:
        f.write(TIME_KEY+"\n")
                            
    gamma_values = [0.8, 0.9, 0.95]
    learning_rate_values = [0.001, 0.01]
    hidden_size_values = [256, 512]
    epsilon_nb_games_values = [80, 100]
    
    positive_reward_values = [10, 20]

    for gamma in gamma_values:
            for learning_rate in learning_rate_values:
                for hidden_size in hidden_size_values:
                    for epsilon_nb_games in epsilon_nb_games_values:
                        
                        GAMMA_DISCOUNT_RATE = gamma
                        VITESSE_APPRENTISSAGE = learning_rate
                        EPSILON_NB_GAMES = epsilon_nb_games
                        HIDDEN_SIZE = hidden_size

                        with open(f"parametres.txt", "w") as f:
                            f.write(f"{TIME_KEY}\n")
                            f.write(f"{GAMMA_DISCOUNT_RATE}\n")
                            f.write(f"{VITESSE_APPRENTISSAGE}\n")
                            f.write(f"{EPSILON_NB_GAMES}\n")
                            f.write(f"{HIDDEN_SIZE}")

                        with open(f"entrainement/{TIME_KEY}.txt", "a") as f:
                            f.write(f"gamma={gamma};learning_rate={learning_rate};epsilon_nb_games={epsilon_nb_games};hidden_size={hidden_size}\n")
                        
                        start_time = time.time()
                        
                        print(f"\nRunning experiment with parameters: gamma={gamma}, learning_rate={learning_rate}, epsilon_nb_games={epsilon_nb_games}, hidden_size={hidden_size}")
                        snake.trainAgent()

                        total_time = time.time() - start_time
                        print(f"Temps de l'entrainement : {round(total_time)}s")
                        with open(f"entrainement/{TIME_KEY}.txt", "a") as f:
                            f.write(f"total_time={round(total_time)}\n")