import turtle


class Maze:
    """Class Maze"""

    def __init__(self, CheminVersFichier):
        f = open(CheminVersFichier, 'r')
        line = f.readlines()
        self.__LargeurTableau = len(line[0]) - 1
        self.__HauteurTableau = len(line)
        self.__data = [[-1] * self.__LargeurTableau for i in range(0, self.__HauteurTableau)]
        for i in range(0, self.__LargeurTableau):
            for j in range(0, self.__HauteurTableau):
                self.__data[i][j] = int(line[i][j])

    def ObtenirChiffreCase(self, x, y):
        return self.__data[y][x]

    def ObtenirLargeur(self):
        return self.__LargeurTableau

    def ObtenirHauteur(self):
        return self.__HauteurTableau

    def PlacerChiffreCase(self, x, y, valeur):
        self.__data[y][x] = valeur

    def getWeight(self):
        return len(self.__data[0])

class TurtleClass:
    """Class Turtle"""

    def __init__(self, LargeurCarte, HauteurCarte, TailleCarre):
        self.__largeurCarte = LargeurCarte
        self.__hauteurCarte = HauteurCarte
        self.__tailleCarre = TailleCarre



    def DessinerCarre(self, DebutX, DebutY, color):
        turtle.pencolor('white')
        turtle.goto(DebutX, DebutY)
        if color == 1:
            turtle.pencolor('red')
            turtle.fillcolor('red')
        if color == 0:
            turtle.pencolor('black')
            turtle.fillcolor('black')
        if color == 3:
            turtle.pencolor('green')
            turtle.fillcolor('green')
        turtle.begin_fill()
        turtle.down()
        for i in range(4):
            turtle.forward(20)
            turtle.right(90)  # 90 degrés.
        turtle.up()
        turtle.end_fill()

    def DessinerCarte(self, maze):
        self.__largeurCarte = 20 * maze.ObtenirLargeur() + 100
        self.__hauteurCarte = 20 * maze.ObtenirHauteur() + 100
        self.__tailleCarre = self.__largeurCarte * self.__hauteurCarte

        turtle.setup(self.__hauteurCarte, self.__largeurCarte)

        for i in range(maze.ObtenirHauteur()):
            for j in range(maze.ObtenirLargeur()):
                case = maze.ObtenirChiffreCase(i, j)
                if not case:
                    self.DessinerCarre((j - (maze.ObtenirLargeur() / 2)) * 20, (-i + (maze.ObtenirHauteur() / 2)) * 20,0)

    def ParcourirCarte(self, maze, X,Y):
        while int(maze.ObtenirChiffreCase(X, Y)) != 3:
            if turtle.heading() == 0:
                if int(maze.ObtenirChiffreCase(X - 1, Y)) != 0:
                    turtle.left(90)
                elif int(maze.ObtenirChiffreCase(X, Y + 1)) != 0:
                    turtle.right(0)
                elif int(maze.ObtenirChiffreCase(X + 1, Y)) != 0:
                    turtle.right(90)
                elif int(maze.ObtenirChiffreCase(X, Y - 1)) != 0:
                    turtle.left(180)
            elif turtle.heading() == 90:
                if int(maze.ObtenirChiffreCase(X, Y - 1)) != 0:
                    turtle.left(90)
                elif int(maze.ObtenirChiffreCase(X - 1, Y)) != 0:
                    turtle.right(0)
                elif int(maze.ObtenirChiffreCase(X, Y + 1)) != 0:
                    turtle.right(90)
                elif int(maze.ObtenirChiffreCase(X + 1, Y)) != 0:
                    turtle.left(180)
            elif turtle.heading() == 270:
                if int(maze.ObtenirChiffreCase(X, Y + 1)) != 0:
                    turtle.left(90)
                elif int(maze.ObtenirChiffreCase(X + 1, Y)) != 0:
                    turtle.right(0)
                elif int(maze.ObtenirChiffreCase(X, Y - 1)) != 0:
                    turtle.right(90)
                elif int(maze.ObtenirChiffreCase(X - 1, Y)) != 0:
                    turtle.left(180)
            elif turtle.heading() == 180:
                if int(maze.ObtenirChiffreCase(X + 1, Y)) != 0:
                    turtle.left(90)
                elif int(maze.ObtenirChiffreCase(X, Y - 1)) != 0:
                    turtle.right(0)
                elif int(maze.ObtenirChiffreCase(X - 1, Y)) != 0:
                    turtle.right(90)
                elif int(maze.ObtenirChiffreCase(X, Y + 1)) != 0:
                    turtle.left(180)
            if turtle.heading() == 270:
                X += 1
            elif turtle.heading() == 180:
                Y -= 1
            elif turtle.heading() == 0:
                Y += 1
            elif turtle.heading() == 90:
                X -= 1
            turtle.forward(20)