import json, os

os.makedirs("config", exist_ok=True) # make sure config directory exists

# file to store preferences
prefs_file = "config/user_preferences.json"

# sample user preferences
user_preferences = {
    "user_id": "logistics_manager_01",
    "region_filter": ["North America", "Europe"],
    "alerts": {
        "delivery_delay": True,
        "temp_threshold": 5.0
    },
    "dashboard_layout": {
        "theme": "dark",
        "widgets": ["shipment_map", "latest_orders", "alert_panel"]
    }
}

with open(prefs_file, 'w') as file:
    json.dump(user_preferences, file, indent=4)

print(f"Preferences saved to {prefs_file}")

with open(prefs_file, 'r') as file:
    loaded_preferences = json.load(file) # load preferences from file

print("\nLoaded preferences from file:")
print(loaded_preferences)

json_string = json.dumps(user_preferences, indent=2) # convert dict to JSON string
print("\nPreferences as JSON string:")
print(json_string)

parsed_from_string = json.loads(json_string) # parse JSON string back to dict
print("\nParsed preferences from JSON string:")
print(parsed_from_string)