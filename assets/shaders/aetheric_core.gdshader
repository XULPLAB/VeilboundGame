shader_type spatial;
uniform vec3 energy_color : source_color = vec3(0.0, 0.5, 1.0);
uniform float core_intensity : hint_range(0.0, 5.0) = 2.0;
uniform float rotation_speed : hint_range(0.0, 10.0) = 2.0;
uniform float pulse_speed : hint_range(0.0, 5.0) = 1.5;
void vertex() {
    float pulse = sin(TIME * pulse_speed) * 0.05;
    VERTEX += NORMAL * pulse;
    float angle = TIME * rotation_speed;
    mat2 rot = mat2(vec2(cos(angle), -sin(angle)), vec2(sin(angle), cos(angle)));
    VERTEX.xz = rot * VERTEX.xz;
}
void fragment() {
    float fresnel = pow(1.0 - dot(NORMAL, VIEW), 3.0);
    float pulse = (sin(TIME * pulse_speed) * 0.5) + 0.5;
    ALBEDO = energy_color * 0.2;
    EMISSION = energy_color * (fresnel + (pulse * 0.5)) * core_intensity;
    ALPHA = clamp(fresnel + 0.3, 0.0, 1.0);
    ROUGHNESS = 0.1;
    METALLIC = 0.5;
}