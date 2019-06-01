import glfw
import glm
from OpenGL.GL import shaders
from OpenGL.GL import *
from OpenGL.GLU import *
from src import shaders
from src import cube

aspect_ratio = 1
sp = None


def key_callback(window, key, scancode, action, mods):
    return


def window_resize_callback(window, width, height):
    if height == 0:
        return
    global aspect_ratio
    aspect_ratio = width / height
    glViewport(0, 0, width, height)


def init_opengl_program(window):
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)
    glfw.set_window_size_callback(window, window_resize_callback)
    glfw.set_key_callback(window, key_callback)


def free_opengl_program(window):
    global sp
    del sp


def draw_scene(window):
    global sp
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    V = glm.lookAt(
        glm.vec3(0.0, 0.0, -5.0),
        glm.vec3(0.0, 0.0, 0.0),
        glm.vec3(0.0, 1.0, 0.0)
    )

    P = glm.perspective(50.0*glm.pi()/180.0, aspect_ratio, 1.0, 50.0)

    M = glm.mat4(1.0)

    glUseProgram(sp)
    glUniformMatrix4fv(glGetUniformLocation(sp, "V"), 1, False, glm.value_ptr(V))
    glUniformMatrix4fv(glGetUniformLocation(sp, "P"), 1, False, glm.value_ptr(P))
    glUniformMatrix4fv(glGetUniformLocation(sp, "M"), 1, False, glm.value_ptr(M))

    glEnableVertexAttribArray(glGetAttribLocation(sp, "vertex"))
    glVertexAttribPointer(glGetAttribLocation(sp, "vertex"), 4, GL_FLOAT, False, 0, cube.vertices)

    glEnableVertexAttribArray(glGetAttribLocation(sp, "normal"))
    glVertexAttribPointer(glGetAttribLocation(sp, "normal"), 4, GL_FLOAT, False, 0, cube.normals)

    glEnableVertexAttribArray(glGetAttribLocation(sp, "color"))
    glVertexAttribPointer(glGetAttribLocation(sp, "color"), 4, GL_FLOAT, False, 0, cube.colors)

    glDrawArrays(GL_TRIANGLES, 0, cube.vertexcount)

    glDisableVertexAttribArray(glGetAttribLocation(sp, "vertex"))
    glDisableVertexAttribArray(glGetAttribLocation(sp, "normal"))
    glDisableVertexAttribArray(glGetAttribLocation(sp, "color"))

    glfw.swap_buffers(window)


def main():
    global sp
    glfw.init()
    if not glfw:
        return

    window = glfw.create_window(800, 600, "IK-demo", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.swap_interval(1)

    sp = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(shaders.vertex, GL_VERTEX_SHADER),
                                          OpenGL.GL.shaders.compileShader(shaders.fragment, GL_FRAGMENT_SHADER))

    init_opengl_program(window)

    glfw.set_time(0)

    while not glfw.window_should_close(window):
        glfw.set_time(0)
        draw_scene(window)
        glfw.poll_events()

    free_opengl_program(window)

    glfw.destroy_window(window)
    glfw.terminate()


if __name__ == "__main__":
    main()
