import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# X = np.linspace(1, 10)
# YT = np.linspace(10, 20)
# YH = np.linspace(90, 100)


def plotSomeData(argX, argYTemp, argYHumi):
    fig = plt.figure()

    plt.plot(argX, argYTemp, 'r--', label='Temperature')
    plt.plot(argX, argYHumi, 'b--', label='Humidity')
    plt.style.use('ggplot')
    plt.grid()
    # plt.legend("Temperature", "Humidity")
    # plt.axes()
    plt.legend(loc="upper left")
    plt.xlabel("Date")
    plt.show()


# plotSomeData(X, YT, YH)
