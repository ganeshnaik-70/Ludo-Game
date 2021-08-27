import pygame
import random
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

pygame.init()

running = True
screen = pygame.display.set_mode((550, 550))
# create title and icon
pygame.display.set_caption("Ludo Game")
icon = pygame.image.load("project.png")
pygame.display.set_icon(icon)

# create a background board
floor = pygame.image.load("ludo_board.gif")

# load piece image
piece_yellow = pygame.image.load("yellow.png")
x, y = 135, 450
initial_position = 0
final_position = 0
yellow_state = "in"

# piece blue
piece_blue = pygame.image.load("blue.png")
blue_x, blue_y = 75, 130
init_pos = 0
fin_pos = 0
blue_state = "in"

# piece red
piece_red = pygame.image.load("red.png")
red_x, red_y = 392, 70
init_position = 0
fin_position = 0
red_state = "in"

# load dice image
dice1 = pygame.image.load("Dice_1.jpg")
dice2 = pygame.image.load("Dice_2.jpg")
dice3 = pygame.image.load("Dice_3.jpg")
dice4 = pygame.image.load("Dice_4.jpg")
dice5 = pygame.image.load("Dice_5.jpg")
dice6 = pygame.image.load("Dice_6.jpg")
dice_list = [dice1, dice2, dice3, dice4, dice5, dice6]

# x & y coordination of moves
piece_listy = [(135, 450), (227, 470), (227, 435), (227, 400), (227, 365), (227, 330), (192, 295), (157, 295),
               (122, 295),
               (87, 295), (52, 295), (17, 295), (17, 260), (17, 225), (52, 225), (87, 225), (122, 225), (157, 225),
               (192, 225), (227, 190), (227, 155), (227, 120), (227, 85), (227, 50), (227, 15), (262, 15), (297, 15),
               (297, 50), (297, 85), (297, 120), (297, 155), (297, 190), (332, 225), (367, 225), (402, 225), (437, 225),
               (472, 225), (507, 225), (507, 260), (507, 295), (472, 295), (437, 295), (402, 295), (367, 295),
               (332, 295), (297, 330), (297, 365), (297, 400), (297, 435), (297, 470), (297, 505), (262, 505),
               (262, 470), (262, 435), (262, 400), (262, 365), (262, 330), (262, 295)]
piece_listb = [(75, 130), (52, 225), (87, 225), (122, 225), (157, 225), (192, 225), (227, 190), (227, 155), (227, 120),
               (227, 85),
               (227, 50), (227, 15), (262, 15), (297, 15), (297, 50), (297, 85), (297, 120), (297, 155), (297, 190),
               (332, 225), (367, 225), (402, 225), (437, 225), (472, 225), (507, 225), (507, 260), (507, 295),
               (472, 295), (437, 295), (402, 295), (367, 295), (332, 295), (297, 330), (297, 365), (297, 400),
               (297, 435), (297, 470), (297, 505), (262, 505), (227, 505), (227, 470), (227, 435), (227, 400),
               (227, 365), (227, 330), (192, 295), (157, 295), (122, 295), (87, 295), (52, 295), (17, 295), (17, 260),
               (52, 260), (87, 260), (122, 260), (157, 260), (192, 260), (227, 260)]
piece_listr = [(392, 70), (297, 50), (297, 85), (297, 120), (297, 155), (297, 190), (332, 225), (367, 225), (402, 225),
               (437, 225), (472, 225), (507, 225), (507, 260), (507, 295), (472, 295), (437, 295), (402, 295),
               (367, 295), (332, 295), (297, 330), (297, 365), (297, 400), (297, 435), (297, 470), (297, 505),
               (262, 505), (227, 505), (227, 470), (227, 435), (227, 400), (227, 365), (227, 330), (192, 295),
               (157, 295), (122, 295), (87, 295), (52, 295), (17, 295), (17, 260), (17, 225), (52, 225), (87, 225),
               (122, 225), (157, 225), (192, 225), (227, 190), (227, 155), (227, 120), (227, 85), (227, 50), (227, 15),
               (262, 15), (262, 50), (262, 85), (262, 120), (262, 155), (262, 190), (262, 225)]
turn = "Yellow Turn"
font = pygame.font.Font("freesansbold.ttf", 24)
over_font = pygame.font.Font("freesansbold.ttf", 64)
blastimg = pygame.image.load("flame.png")
last_turn = " "


def background(x, y):
    screen.blit(floor, (x, y))


def dice(a):
    screen.blit(dice_list[a - 1], (245, 245))


def yellow(x, y):
    screen.blit(piece_yellow, (x, y))


def blue(x, y):
    screen.blit(piece_blue, (x, y))


def red(x, y):
    screen.blit(piece_red, (x, y))


def show_turn(text):
    turn_text = font.render(text, True, (255, 255, 255))
    screen.blit(turn_text, (40, 15))


def move_blue(piece_img, final_pos, ypos, rpos, turn):
    if blue_state == "in":
        screen.blit(piece_img, (blue_x, blue_y))
    else:
        global init_pos
        screen.blit(piece_img, piece_listb[final_pos])
        init_pos = final_pos
    if last_turn == "Blue Turn" and turn == "Blue Turn":
        iscollision(final_pos, ypos, rpos)
    if turn == "Red Turn" and last_turn != "Red Turn":
        iscollision(final_pos, ypos, rpos)
    game_over(final_pos, ypos, rpos)


def move_yellow(piece_img, final_pos, bpos, rpos, turn):
    # print(turn)
    if yellow_state == "in":
        screen.blit(piece_img, (x, y))
    else:
        global initial_position
        screen.blit(piece_img, piece_listy[final_pos])
        initial_position = final_pos
    if last_turn == "Yellow Turn" and turn == "Yellow Turn":
        iscollision(final_pos, bpos, rpos)
    if turn == "Blue Turn" and last_turn != "Blue Turn":
        iscollision(final_pos, bpos, rpos)
    game_over(bpos, final_pos, rpos)


def move_red(piece_img, final_pos, ypos, bpos, turn):
    if red_state == "in":
        screen.blit(piece_img, (red_x, red_y))
    else:
        global init_position
        screen.blit(piece_img, piece_listr[final_pos])
        init_position = final_pos
    if last_turn == "Red Turn" and turn == "Red Turn":
        iscollision(final_pos, ypos, bpos)
    if turn == "Yellow Turn" and last_turn != "Yellow Turn":
        iscollision(final_pos, ypos, bpos)
    game_over(bpos, ypos, final_pos)


def iscollision(first_pos, op1_pos, op2_pos):
    global initial_position, final_position, init_pos, fin_pos, yellow_state, blue_state, init_position, fin_position, red_state, turn
    if turn == "Yellow Turn":
        # distance = math.sqrt(math.pow(enemyx - bulletx, 2) + math.pow(enemyy - bullety, 2))
        if piece_listr[first_pos][0] == piece_listy[op1_pos][0] and piece_listr[first_pos][1] == piece_listy[op1_pos][
            1]:
            print("collision R to Y")
            print(piece_listr[first_pos][0], piece_listy[op1_pos][0], ":", piece_listr[first_pos][1],
                  piece_listy[op1_pos][
                      1])
            initial_position = 0
            final_position = 0
            yellow_state = "in"
            turn = "Red Turn"
        if piece_listr[first_pos][0] == piece_listb[op2_pos][0] and piece_listr[first_pos][1] == piece_listb[op2_pos][
            1]:
            print("collision R to B")
            print(piece_listr[first_pos][0], piece_listb[op2_pos][0], ":", piece_listr[first_pos][1],
                  piece_listb[op2_pos][
                      1])
            init_pos = 0
            fin_pos = 0
            blue_state = "in"
            turn = "Red Turn"
    elif turn == "Blue Turn":
        if piece_listy[first_pos][0] == piece_listb[op1_pos][0] and piece_listy[first_pos][1] == piece_listb[op1_pos][
            1]:
            print("collision Y to B")
            print(piece_listy[first_pos][0], piece_listb[op1_pos][0], ":", piece_listy[first_pos][1],
                  piece_listb[op1_pos][1])
            init_pos = 0
            fin_pos = 0
            blue_state = "in"
            turn = "Yellow Turn"
        if piece_listy[first_pos][0] == piece_listr[op2_pos][0] and piece_listy[first_pos][1] == piece_listr[op2_pos][
            1]:
            print("collision Y to R")
            print(piece_listy[first_pos][0], piece_listr[op2_pos][0], ":", piece_listy[first_pos][1],
                  piece_listr[op2_pos][1])
            init_position = 0
            fin_position = 0
            red_state = "in"
            turn = "Yellow Turn"
    elif turn == "Red Turn":
        if (piece_listb[first_pos][0] == piece_listr[op2_pos][0] and piece_listb[first_pos][1] == piece_listr[op2_pos][
            1]):
            print("collision B to R")
            print(piece_listb[first_pos][0], piece_listr[op2_pos][0], ":", piece_listb[first_pos][1],
                  piece_listr[op2_pos][1])
            init_position = 0
            fin_position = 0
            red_state = "in"
            turn = "Blue Turn"
        if (piece_listb[first_pos][0] == piece_listy[op1_pos][0] and piece_listb[first_pos][1] == piece_listy[op1_pos][
            1]):
            print("collision B to Y")
            print(piece_listb[first_pos][0], piece_listy[op1_pos][0], ":", piece_listb[first_pos][1],
                  piece_listy[op1_pos][1])
            initial_position = 0
            final_position = 0
            yellow_state = "in"
            turn = "Blue Turn"


def game_over(blue_pos, yellow_pos, red_pos):
    global turn
    if (piece_listb[blue_pos][0], piece_listb[blue_pos][1]) == (227, 260) or (
            piece_listy[yellow_pos][0], piece_listy[yellow_pos][1]) == (262, 295) or (
            piece_listr[red_pos][0], piece_listr[red_pos][1]) == (262, 225):
        game_over_text = over_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (80, 250))
        turn = "No Turn"


a = 0
d = 0
# game loop
while running:

    # fill the screen with black colour
    screen.fill((0, 0, 0))
    # check for the event happen in pygame
    for event in pygame.event.get():

        # check if exit key is pressed
        if event.type == pygame.QUIT:
            running = False

        # check if key is pressed
        if event.type == pygame.KEYDOWN:
            # space key to change the dice
            if event.key == pygame.K_SPACE:
                # pygame.time.wait(800)
                a = random.randint(1, 6)
                d = a
                last_turn = turn
                if turn == "Yellow Turn":
                    # Piece will out first only when 6 appears
                    if a == 6 and yellow_state == "in":
                        yellow_state = "out"
                        final_position = 1
                    # if piece are already out
                    elif yellow_state == "out":
                        last_posy = final_position
                        final_position = initial_position + a
                        if final_position > 57:
                            final_position = last_posy
                    # if initially 6 is not appears then make a=0
                    else:
                        a = 0
                    turn = "Blue Turn"
                    if a == 6:
                        turn = "Yellow Turn"

                elif turn == "Blue Turn":
                    # Piece will out first only when 6 appers
                    if a == 6 and blue_state == "in":
                        blue_state = "out"
                        fin_pos = 1
                    # if piece are already out
                    elif blue_state == "out":
                        last_posb = fin_pos
                        fin_pos = init_pos + a
                        if fin_pos > 57:
                            fin_pos = last_posb
                    # if initially 6 is not appears then make a=0
                    else:
                        a = 0
                    turn = "Red Turn"
                    if a == 6:
                        turn = "Blue Turn"
                elif turn == "Red Turn":
                    # Piece will out first only when 6 appears
                    if a == 6 and red_state == "in":
                        red_state = "out"
                        fin_position = 1
                    # if piece are already out
                    elif red_state == "out":
                        last_posr = fin_position
                        fin_position = init_position + a
                        if fin_position > 57:
                            fin_position = last_posr
                    # if initially 6 is not appears then make a=0
                    else:
                        a = 0
                    turn = "Yellow Turn"
                    if a == 6:
                        turn = "Red Turn"

    background(0, 0)
    screen.blit(blastimg, (84, 295))
    screen.blit(blastimg, (294, 435))
    screen.blit(blastimg, (224, 82))
    screen.blit(blastimg, (437, 225))

    show_turn(turn)
    # to show dice
    if d != 0:
        dice(d)
    # to show piece
    if a == 0:
        if yellow_state == "in":
            yellow(x, y)
        if blue_state == "in":
            blue(blue_x, blue_y)
        if red_state == "in":
            red(red_x, red_y)

    # to move piece
    move_blue(piece_blue, fin_pos, final_position, fin_position, turn)
    move_yellow(piece_yellow, final_position, fin_pos, fin_position, turn)
    move_red(piece_red, fin_position, final_position, fin_pos, turn)

    # update the display
    pygame.display.update()
