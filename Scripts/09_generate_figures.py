import matplotlib.pyplot as plt
import seaborn as sns

def plot_pdf(obs, model):

    sns.kdeplot(obs,label="Observation")
    sns.kdeplot(model,label="Model")

    plt.legend()
    plt.show()