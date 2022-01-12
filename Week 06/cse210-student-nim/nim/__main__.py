from game.director import Director
from termcolor import colored
from pyfiglet import Figlet

g = Figlet(font="isometric2")
print(colored(g.renderText("Hello"), "green"))

director = Director()
director.start_game()