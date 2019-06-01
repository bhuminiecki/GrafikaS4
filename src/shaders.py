vertex = """
#version 330

uniform mat4 P;
uniform mat4 V;
uniform mat4 M;

in vec4 vertex;
in vec4 color;
in vec4 normal;

out vec4 gColor;

void main(void) {
    gColor=color;
    gl_Position=P*V*M*vertex;
}
"""

fragment = """
#version 330

out vec4 pixelColor;
in vec4 iColor;

void main(void) {
    pixelColor=iColor;
}
"""
