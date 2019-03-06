import pyglet
from pyglet.gl import *
win = pyglet.window.Window()
@win.event
def on_draw():
        # Clear buffers
        glClear(GL_COLOR_BUFFER_BIT)
        # Set polygonmode
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        # Draw some stuff
        glBegin(GL_TRIANGLE_FAN)
        glVertex3i(250, 250, 1)
        glVertex3i(50, 400, 1)
        glVertex3i(350, 250, 1)
        glVertex3i(400, 300, 1)
        glVertex3i(400, 100, 1)
        glEnd()
pyglet.app.run()
