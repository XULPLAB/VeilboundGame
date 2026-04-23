extends Sprite2D
var reaction_tween: Tween
func _ready():
    if material: material = material.duplicate()
func trigger_tap_reaction():
    if reaction_tween: reaction_tween.kill()
    reaction_tween = create_tween()
    material.set_shader_parameter("reaction_power", 1.0)
    reaction_tween.tween_property(material, "shader_parameter/reaction_power", 0.0, 0.8).set_trans(Tween.TRANS_ELASTIC).set_ease(Tween.EASE_OUT)
    var ot = scale
    var p = create_tween()
    p.tween_property(self, "scale", ot * 1.1, 0.1)
    p.tween_property(self, "scale", ot, 0.3)
