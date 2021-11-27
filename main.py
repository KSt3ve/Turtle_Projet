from labyrinthe import TurtleClass
from labyrinthe import Maze
import turtle

turtle.tracer(10)
test = TurtleClass(21,21,1)

var = Maze("Maze"+input("Entrez le numéro du labyrinthe (1, 2 ou 3):")+".txt")


test.DessinerCarte(var)


turtle.fillcolor('blue')
turtle.shape("turtle")
turtle.goto(-var.getWeight()*10+30, var.getWeight()*10-30)
turtle.down()

test.ParcourirCarte(var, 1, 1)
turtle.exitonclick()

