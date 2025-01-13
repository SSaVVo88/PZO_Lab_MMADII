import pandas as pd
import config as cfg
from utils import get_repo_path
import seaborn as sns
import matplotlib.pyplot as plt

MATRIX_PLOT = 'matrix_plot.png'

def main():
    df = pd.read_csv(get_repo_path() / cfg.DATA_PATH / cfg.INPUT_FILE)

    sns.set_theme(style='ticks')
    sns.pairplot(df, hue=cfg.TARGET)
    plt.savefig(get_repo_path() / cfg.PLOTS_PATH / MATRIX_PLOT)

if __main__ == '__name__':
    main()