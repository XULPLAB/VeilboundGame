import sys
import os

def process_command(cmd_text):
    if not cmd_text or "🔱 XULPLAB" in cmd_text:
        return None

    cmd = cmd_text.lower().strip()
    
    # NEW LOGIC: Shader Deployment
    if "#deploy shader" in cmd:
        shader_code = """shader_type spatial;
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
}"""
        # Ensure the directory exists
        os.makedirs("assets/shaders", exist_ok=True)
        with open("assets/shaders/aetheric_core.gdshader", "w") as f:
            f.write(shader_code)
            
        return "🔱 XULPLAB: Shader synthesized. 'aetheric_core.gdshader' has been deployed to assets/shaders. Ready for Prism integration."

    # Keep existing Tower/Waystop logic below...
    if "#update manifest: waystops" in cmd:
        return "🔱 XULPLAB: Waystop Manifest locked. Processing Crystal artifacts."
    
    if "propose" in cmd and "tower" in cmd:
        return "🔱 XULPLAB: Tower anchor set. Azure variant initialized."

    return "🔱 XULPLAB: Directive recognized. Ready for the next build phase."

if __name__ == "__main__":
    telegram_message = sys.argv[1] if len(sys.argv) > 1 else ""
    result = process_command(telegram_message)
    if result:
        print(result)
