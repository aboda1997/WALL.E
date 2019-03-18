from  OpenGL .GL import *
from OpenGL.GLUT import *
import numpy as np
from math import *
def DrawCircle( r ,xc ,yc , R,G, B ,fm =0, to = 2*pi):
    glColor3f(R,G, B)
    glBegin(GL_POLYGON)
    for d in np.arange(fm, to, .001):
        x = r* cos(d)
        y = r * sin(d)
        glVertex(x + xc, y + yc )
    glEnd()
def Drawline(x1,y1,x2 ,y2,R ,G ,B ,w= 1) :

    glColor3f(R, G, B)
    glEnable(GL_LINE_SMOOTH)
    glLineWidth(w)

    glBegin(GL_LINES)

    glVertex(x1, y1)
    glVertex(x2, y2)




    glEnd()

def DrawHand(x,r=1,g=1,b=0):
    glColor3f(r,g,b)
    for type in (GL_POLYGON ,GL_LINE_LOOP):

        glBegin(type )
        glVertex(x[0])
        glVertex(x[1])
        glVertex(x[2])
        glVertex(x[3])
        glVertex(x[4])
        glVertex(x[5])

        glColor3f(0,0,0)
        glEnd()



def DrawTriangle(x1 ,y1 ,x2 ,y2 ,step , R,G,B):
    glColor3f(R,G,B)
    glBegin(GL_POLYGON)
    glVertex(x1 ,y1 )
    glVertex(x2 , y2)
    glVertex(x2, y2-step)
    glVertex(x1 , y1-step)
    glEnd()
def drawside(x , type, r=0,g=0,b=0):
    glColor3f(r, g, b)

    glBegin(type )
    glVertex(x[0])
    glVertex(x[1])
    glVertex(x[2])
    glVertex(x[3])
    glVertex(x[4])
    glVertex(x[5])
    glVertex(x[6])

    glEnd()


def Draw():
    glClearColor(0,1,1,0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,1,1)
    glBegin(GL_LINES)
    glVertex(0, 1)
    glVertex(0, -1)

    glVertex(1, 0)
    glVertex(-1, 0)
    glEnd()

    DrawTriangle(.1,.79,-.1,.79,.09,0,0,0)

    DrawTriangle(.1,.78,-.1,.78,.07,1,1,0)
    Drawline(.02,.74,-.02,.74,0,0,0)
    DrawCircle(.039,0,.7,0,0,0 , -pi, 0)
    DrawCircle(.03,0,.7,1,1,0 , -pi, 0)
    DrawTriangle(.01,.67,-.01,.67,.07,0,0,0)
    DrawTriangle(.008,.66,-.008,.66,.07,1,1,0)
    DrawTriangle(.026,.61,-.026,.61,.09,0,0,0)
    DrawCircle(.027,0,.601,0,0,0 )

    DrawTriangle(.022,.61,-.022,.61,.09,1,1,0)
    Drawline(.018,.6,-.018,.6,0,0,0)
    Drawline(.018,.58,-.018,.58,0,0,0)
    Drawline(.018,.56,-.018,.56,0,0,0)
    Drawline(.018,.54,-.018,.54,0,0,0)
    ###draw witetriangle and buttons
    DrawTriangle(.11,.53,-.11,.53,.137,0,0,0)
    DrawTriangle(.105,.523,-.105,.523,.13,.9,.9,.9)
    DrawCircle(0.005 ,.1,.5108,0,0,0 )
    DrawCircle(0.005 ,.1,.405,0,0,0 )
    DrawCircle(0.005 ,-.1,.5108,0,0,0  )
    DrawCircle(0.005 ,-.1,.405,0,0,0 )
    DrawCircle(0.01 ,-.05,.43,0,0,0 )
    DrawCircle(0.01 ,-.02,.43,0,0,0 )
    DrawCircle(0.008 ,-.05,.43,1,0,0 )
    DrawCircle(0.008 ,-.02,.43,0,1,0 )
    Drawline(-.06,.46,-.01,.46,0,0,0)
    Drawline(-.06,.48,-.01,.48,0,0,0)
    DrawTriangle(.03,.48,.09,.48,.07,0,0,0)
    DrawTriangle(.031,.478,.088,.478,.07,0,1,1)
    #draw yellow triangle
    drawside([(.04, .164), (.045, .155), (.12, .155), (.12, .23), (.11, .24), (.11, .164), (.04, .164)], GL_POLYGON)
    drawside([(-.04, .164), (-.045, .155), (-.12, .155), (-.12, .23), (-.11, .24), (-.11, .164), (-.04, .164)],GL_POLYGON)

    DrawTriangle(.11, .393, -.11, 0.393,.23, 0, 0, 0)

    DrawTriangle(.105, .383, -.105, .383, .21, 1, 1, 0)
    # meduim triangle and circles
    DrawTriangle(.09, .35, -.09, 0.35, .15, 0, 0, 0)
    DrawTriangle(.08, .34, -.08, 0.34, .13, 1, 1, 0)
    DrawCircle(.005, .07, .33, 0, 0, 0)
    DrawCircle(.005, -.07, .33, 0, 0, 0)
    DrawCircle(.005, .07, .22, 0, 0, 0)
    DrawCircle(.005, -.07, .22, 0, 0, 0)

    #draw left side
    DrawTriangle(.07, .155, .105, .155, .03, 0, 0, 0)
    DrawTriangle(.073, .155, .101, .155, .026, .9, .9, .9)
    DrawTriangle(.09, .125, .15, .125, .05, 0, 0, 0)
    DrawTriangle(.093, .123, .147, .123, .045, .9, .9, .9)
    DrawCircle(.02,.0906,.11,0,0,0,pi/2,3*pi/2)
    DrawCircle(.015,.0906,.11,.9,.9,.9,pi/2,3*pi/2)
    DrawCircle(.005,.103,.09,0,0,0)
    DrawTriangle(.15, .2, .25, .2, .25 , 0.1,.1,0)
    Drawline(.15,.13,.23,.13,0,0,0)
    Drawline(.17,.1,.23,.1,0,0,0)
    Drawline(.17,.17,.23,.17,0,0,0)
    Drawline(.17,.07,.23,.07,0,0,0)

    Drawline(.17,0,.23,.0,0,0,0)



#draw right side
    DrawTriangle(-.07, .155, -.105, .155, .03, 0, 0, 0)
    DrawTriangle(-.073, .155, -.101, .155, .026, .9, .9, .9)
    DrawTriangle(-.09, .125, -.15, .125, .05, 0, 0, 0)
    DrawTriangle(-.093, .123, -.147, .123, .045, .9, .9, .9)
    DrawCircle(.02, -.0906, .11, 0, 0, 0, -pi / 2,  pi / 2)
    DrawCircle(.015, -.0906, .11, .9, .9, .9, -pi / 2,  pi / 2)
    DrawCircle(.005, -.103, .09, 0, 0, 0)
    #
    DrawTriangle(-.15, .2, -.25, .2, .25, 0.1, .1, 0)
    Drawline(-.15, .13, -.23, .13, 0, 0, 0)
    Drawline(-.17, .1, -.23, .1, 0, 0, 0)
    Drawline(-.17, .17, -.23, .17, 0, 0, 0)
    Drawline(-.17, .07, -.23, .07, 0, 0, 0)

    Drawline(-.17, 0, -.23, .0, 0, 0, 0)












#draw right shoulder
    DrawCircle(0.03 ,.11,.5,0,0,0 , -pi/2,pi/2)
    DrawCircle(0.025 ,.11,.5,1,1,0 , -pi/2,pi/2)
    DrawCircle(0.03, .1399, .44, 0, 0, 0, -pi / 2, pi / 2)
    DrawCircle(0.026, .1399, .44, 1, 1, 0, -pi / 2, pi / 2)

    DrawTriangle(.14,.5,.11,.5,.109,0,0,0)
    DrawTriangle(.137,.5,.1103,.5,.109,1,1,0)
    #draw left shoulder
    DrawCircle(0.03, -.11, .5, 0, 0, 0, pi / 2, 3 * pi / 2)
    DrawCircle(0.025, -.11, .5, 1, 1, 0, pi / 2, 3 * pi / 2)
    DrawCircle(0.03, -.1399, .44, 0, 0, 0, pi / 2, 3*pi / 2)
    DrawCircle(0.026, -.1399, .44, 1, 1, 0, pi / 2, 3*pi / 2)
    DrawTriangle(-.14, .5, -.11, .5, .109, 0, 0, 0)
    DrawTriangle(-.137, .5, -.1103, .5, .109, 1, 1, 0)
    #left hand
    DrawHand([(.12, .44), (.19, .44), (.19, .35), (.18, .34), (.13, .34), (.12, .35)])
    Drawline(.108, .5 - .109, .117, .5 - .109, 0, 0, 0)
    Drawline(.155, .34, .155, .36, 1, 1, 1, 2)
    Drawline(.12, .37, .19, .37, 0, 0, 0, 2)
    Drawline(.156, .37, .156, .42, 0, 0, 0, 2)
    Drawline(.156, .34, .156, .42, 1, 1, 1, .5)
    DrawHand([(.14,.44),(.17,.44),(.17,.42),(.15,.42),(.145,.42),(.14,.42)])
    #right  hand
    DrawHand([(-.12, .44), (-.19, .44), (-.19, .35), (-.18, .34), (-.13, .34), (-.12, .35)])
    Drawline(-.108, .5 - .109, -.117, .5 - .109, 0, 0, 0)
    Drawline(-.155, .34, -.155, .36, 1, 1, 1, 2)
    Drawline(-.12, .37, -.19, .37, 0, 0, 0, 2)
    Drawline(-.156, .37, -.156, .42, 0, 0, 0, 2)
    Drawline(-.156, .34, -.156, .42, 1, 1, 1, .5)


    DrawHand([(-.14,.44),(-.17,.44),(-.17,.42),(-.15,.42),(-.145,.42),(-.14,.42)])


#draw eyes
    DrawCircle(.07,.1,.75,0,0,0)
    DrawCircle(.06,.1,.75,0,0.7,1)
    DrawCircle(.04,.1,.75,0,0,0)
    DrawCircle(.03,.1,.75,0,0.3,1)
    DrawCircle(.01,.08,.74,1,1,1)
    DrawCircle(.07, -.1, .75, 0, 0, 0)
    DrawCircle(.06, -.1, .75, 0, 0.7, 1)
    DrawCircle(.04, -.1, .75, 0, 0, 0)
    DrawCircle(.03, -.1, .75, 0, 0.3, 1)
    DrawCircle(.01, -.09, .74, 1, 1, 1)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400 ,400)
glutCreateWindow(b"openGL window ")
glutDisplayFunc(Draw)
glutMainLoop()


