extends Node

# APEX GENESIS: 3-Battle Creature Rescue Logic
var battle_count = 0
var max_battles = 3

func start_rescue_mission():
	battle_count = 0
	print("⚔️ [BATTLE] Rescue Mission Started at Castlewood Grid.")
	next_battle_phase()

func next_battle_phase():
	if battle_count < max_battles:
		battle_count += 1
		# Trigger Aetheric Injection Haptics here
		print("🔥 [BATTLE] Phase ", battle_count, " Engaging...")
	else:
		complete_rescue()

func complete_rescue():
	print("🏆 [SUCCESS] Creature Rescued. Minting to Treasury.")
