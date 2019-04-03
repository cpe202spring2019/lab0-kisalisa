def weight_on_planets():
    weight = int(input("What do you weigh on earth? "))
    mars = 0.38 * weight
    jup = 2.34 * weight
    print("\nOn Mars you would weigh{0: .2f} pounds.\nOn Jupiter you would weigh{1: .2f} pounds.".format(mars, jup))
   
if __name__ == '__main__':
   weight_on_planets()
