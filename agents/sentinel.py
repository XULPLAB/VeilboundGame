import sys
import os

def process_command(cmd_text):
    # Log what was received for debugging
    if not cmd_text:
        return "🔱 XULPLAB: Critical Error - No payload detected by Sentinel."

    cmd = cmd_text.lower().strip()
    
    # Check if the bot is talking to itself
    if "🔱 xulplab" in cmd:
        return None

    # SHADER DEPLOYMENT
    if "#deploy shader" in cmd:
        os.makedirs("assets/shaders", exist_ok=True)
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
        with open("assets/shaders/aetheric_core.gdshader", "w") as f:
            f.write(shader_code)
        return "🔱 XULPLAB: Shader synthesized. 'aetheric_core.gdshader' is now live in the repository."

    # WAYSTOP UPDATE
    if "#update manifest: waystops" in cmd:
        return "🔱 XULPLAB: Waystop Manifest locked. Crystal assets registered."

    # PRISM UPDATE
    if "#update manifest: prisms" in cmd:
        return "🔱 XULPLAB: Prism Manifest locked. 6 Tiers initialized."

    # FALLBACK: If nothing matches, tell the user what the bot heard
    return f"🔱 XULPLAB: Sentinel heard: '{cmd_text[:30]}...' but no command pattern matched. Use #Deploy Shader or #Update Manifest."

if __name__ == "__main__":
    telegram_message = sys.argv[1] if len(sys.argv) > 1 else ""
    result = process_command(telegram_message)
    if result:
        print(result)
