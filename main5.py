#!/usr/bin/env python3

import utils, open_color, arcade    # import utils for python version check
                                    # import open_color for color the drawings
                                    # import arcade to draw stuff
utils.check_version((3,7))          # python version check

SCREEN_WIDTH = 800                  # setup the window width
SCREEN_HEIGHT = 600                 # setup the window height
SCREEN_TITLE = "Smiley Face Example"    # setup the title of the window

class Faces(arcade.Window): # A class of Faces
    """ Our custom Window Class"""

    def __init__(self): # constructor of the class
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Show the mouse cursor
        self.set_mouse_visible(True)

        self.x = SCREEN_WIDTH / 2   # set the starting width position of the mouse cursor
        self.y = SCREEN_HEIGHT / 2  # set the starting height position of the mouse cursor

        arcade.set_background_color(open_color.white)   # set the background color to white

    def on_draw(self):  # A function to draw
        """ Draw the face """
        arcade.start_render()   # start the drawing render
        face_x,face_y = (self.x,self.y) #set the face position to the mouse cursor
        smile_x,smile_y = (face_x + 0,face_y - 10)  # set the smile position in the face
        eye1_x,eye1_y = (face_x - 30,face_y + 20)   # set the eye1 position in the face
        eye2_x,eye2_y = (face_x + 30,face_y + 20)   # set the eye2 position in the face
        catch1_x,catch1_y = (face_x - 25,face_y + 25) # set the catch1 position in the face
        catch2_x,catch2_y = (face_x + 35,face_y + 25) # set the catch2 position in the face

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3) # draw a circle filled with yellow color for the face
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4) # draw a black circle outline which is not filled
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black)    # draw a ellipse filled with black color for eye1
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)    # draw a ellipse filled with black color for eye2
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)    # draw a circle filled with gray color for the catch1
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)    # draw a circle filled with gray color for the catch2
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)   # draw an black arc as the smile


    def on_mouse_motion(self, x, y, dx, dy):    # override the on_mouse_motion function
        """ Handle Mouse Motion """
        self.x = x  # set the self.x position to the new x position
        self.y = y  # set the self.y position to the new y position



window = Faces()    # run the Faces class and store it into the window
arcade.run()    # run the arcade code