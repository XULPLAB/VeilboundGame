extends CanvasItem

# APEX GENESIS: 0.6s Bezier Pulse (Gold to Cyan)
func trigger_pulse():
	var tween = create_tween()
	tween.set_trans(Tween.TRANS_BEZIER)
	tween.set_ease(Tween.EASE_IN_OUT)
	
	# Transition from Gold (Qwen/Power) to Cyan (System/Success)
	modulate = Color(1.0, 0.84, 0.0) # Gold
	tween.tween_property(self, "modulate", Color(0.0, 1.0, 1.0), 0.6)

# APEX GENESIS: iPhone Taptic Sequence (Medium -> Flow -> Success)
func play_haptic_sequence():
	# In Godot for Mobile, we trigger via Input.vibrate()
	# Representing the Three-Stage Command:
	Input.vibrate_handheld(20) # Medium Impact (Grab)
	await get_tree().create_timer(0.1).timeout
	Input.vibrate_handheld(10) # Flow (Connection)
	await get_tree().create_timer(0.1).timeout
	Input.vibrate_handheld(40) # Success (Lock)
