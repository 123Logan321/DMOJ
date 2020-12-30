screen_size = input()
screen_size = screen_size.split()
positionX = 0
positionY = 0
while True:
    mouse_move = input()
    mouse_move = mouse_move.split()
    if mouse_move [0] == "0" and mouse_move[1] == "0":
        break
    positionX += int(mouse_move[0])
    positionY += int(mouse_move[1])
    if positionX > int(screen_size[0]):
        positionX = int(screen_size[0])
    elif positionX <= 0:
        positionX = 0
    if positionY > int(screen_size[1]):
        positionY = int(screen_size[1])
    elif positionY <= 0:
        positionY = 0

    print(positionX,positionY)
    mouse_move = []
