import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.pyplot as plt
def plot_with_image(x,y):
    with cbook.get_sample_data('logo2.png') as file:
        im = image.imread(file)

    fig, ax = plt.subplots()

    ax.plot(x,y, '-o', ms=20, alpha=0.7, mfc='orange')
    ax.grid()
    fig.figimage(im, 10, 10, zorder=3, alpha=.5)

    plt.show()
