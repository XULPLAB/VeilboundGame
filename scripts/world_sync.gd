extends Node3D

# APEX GENESIS: 1:1 World Mapping Constant
const SCALE_FACTOR = 1.0 # 1 meter in real world = 1 unit in Godot

func sync_avatar_to_gps(lat: float, lon: float):
	# Using 5-decimal truncation for battery preservation
	var clean_lat = floor(lat * 100000) / 100000
	var clean_lon = floor(lon * 100000) / 100000
	
	# Mapping GPS to 3D Coordinates
	$Avatar.position.x = clean_lon * SCALE_FACTOR
	$Avatar.position.z = clean_lat * SCALE_FACTOR
	
	print("🛡️ [SYSTEM] Grid Synced. Avatar positioned at: ", $Avatar.position)
