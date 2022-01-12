def main():
    
    choice = ""
    while choice.lower() != "q":
        choice = input("{X}'s turn to choose a square (1-9): ")
        if not choice.isdigit():
            print("Please enter a number between 1-9")
        elif int.choice >1 and int.choice <9:
            print("Please enter a number between 1-9")
        # print("Thanks for playing")

def grid():

    grid = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    for i in grid:
        for j in i:
            print(f"{j} ", end="")
        print()

# # def x():
# #     pass

# # def o():
# #     pass

if __name__ == "__main__":
    main()
