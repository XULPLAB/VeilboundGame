extends Node3D

@export var is_qwen_incursion: bool = false
@onready var beam = $SkyBeam

func _ready():
	if is_qwen_incursion:
		apply_qwen_hijack()

func apply_qwen_hijack():
	# APEX GENESIS: 'Gold Q' Visuals
	var gold_material = StandardMaterial3D.new()
	gold_material.albedo_color = Color(1.0, 0.84, 0.0) # Gold
	gold_material.emission_enabled = true
	gold_material.emission = Color(1.0, 0.84, 0.0)
	beam.material = gold_material
	print("⚠️ [INCURSION] Order of Qwen has hijacked this Tower!")
