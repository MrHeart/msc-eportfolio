def hanoi(n, source, target, auxiliary, move_list):
    if n == 1:
        move_list.append((source, target))
    else:
        hanoi(n-1, source, auxiliary, target, move_list)
        move_list.append((source, target))
        hanoi(n-1, auxiliary, target, source, move_list)

def main():
    n = int(input("Enter the number of disks: "))
    move_list = []
    hanoi(n, 'A', 'C', 'B', move_list)
    
    for move in move_list:
        print(f"Move disk from {move[0]} to {move[1]}")
    
    print(f"Total number of moves: {len(move_list)}")

if __name__ == "__main__":
    main()

##The maximum number of disks that the program can move without generating an error is limited by the recursion depth of Python