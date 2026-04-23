shader_type canvas_item;
uniform bool is_flyer = false;
uniform float speed = 2.0;
uniform float amplitude = 0.05;
uniform float reaction_power = 0.0;
void vertex() {
    float time = TIME * speed;
    if (is_flyer) {
        VERTEX.y += sin(time) * 15.0; 
        VERTEX.y += sin(time * 2.0) * (abs(VERTEX.x) * 0.2);
        VERTEX.x += cos(time * 0.5) * 5.0;
    } else {
        float breath = sin(time) * amplitude;
        VERTEX.y *= (1.0 - breath);
        VERTEX.x *= (1.0 + breath * 0.5);
    }
    VERTEX.y -= reaction_power * 40.0 * abs(sin(TIME * 20.0));
}
void fragment() {
    vec4 col = texture(TEXTURE, UV);
    float glow_mask = reaction_power * 0.5;
    vec3 glow_color = vec3(0.0, 0.8, 1.0); 
    COLOR = vec4(col.rgb + (glow_color * glow_mask * col.a), col.a);
}
