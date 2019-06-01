vertex = """
#version 330
in vec3 position;
in vec3 color;

uniform mat4 transform;

out vec3 newColor;
void main()
{
    gl_Position = transform * vec4(position, 1.0f);
    newColor = color;
}
"""

fragment = """
#version 330
in vec3 newColor;

out vec4 outColor;

void main()
{
    outColor = vec4(newColor, 1.0f);
}
"""