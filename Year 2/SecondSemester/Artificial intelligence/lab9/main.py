from Utils import Utils
from Retea import ANN


def main():
    nn = ANN([4, 4, 3], Utils.linear, Utils.linear_derivative)
    u, t = Utils.readData()

    for i in range(100):
        for j in range(len(u)):
            nn.backPropag(nn.computeLoss(u[j], t[j]), 0.01)

    for i in range(len(u)):
        predicted = nn.feedForward(u[i])
        if t[i][0] == 1:
            a = "0"
        elif t[i][1] == 1:
            a = "1"
        else:
            a = "2"

        print("Actual: {}, Predicted:{}".format(a, predicted))


main()
