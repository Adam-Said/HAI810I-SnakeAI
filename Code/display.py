import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def displayScores(scores, moyenne):
    plt.clf()
    plt.title('Entrainement...')
    plt.xlabel('Nombre d\'essais')
    plt.ylabel('Score')
    plt.plot(scores, color="green")
    plt.plot(moyenne, color="blue")
    plt.legend(["Scores", "Moyenne"], loc='upper left')
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(moyenne)-1, moyenne[-1], str(moyenne[-1]))
    
    # On affiche que des valeurs entières, et si il y en a trop on wrap
    y_min, y_max = plt.ylim()
    if y_max < 10:
        plt.yticks(range(int(y_min), int(y_max)+1))
    else:
        plt.yticks(range(int(y_min), int(y_max)+1, int((y_max-y_min)/10)))
    
    plt.show(block=False)
    plt.pause(.1)