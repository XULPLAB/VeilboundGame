extends Control

# APEX GENESIS: UI Constrains
@onready var joystick_knob = $Knob
@onready var energy_status = 1.0 # 100%

func _process(_delta):
	# 15% Amber Low-Energy Warning Logic
	if energy_status <= 0.15:
		joystick_knob.modulate = Color(1.0, 0.75, 0.0) # Amber
	else:
		joystick_knob.modulate = Color(0.0, 1.0, 1.0, 0.5) # Cyan Semi-Transparent

func _input(event):
	# Logic for movement within the bottom-right quarter of the screen
	if event is InputEventScreenTouch or event is InputEventScreenDrag:
		update_joystick_position(event.position)
