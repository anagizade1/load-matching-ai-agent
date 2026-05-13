import os
from dotenv import load_dotenv
from src.sheets_client import get_drivers
from src.load_provider import get_available_loads

load_dotenv()

# ── Alətlər 
tools = [
    {
        "name": "get_drivers",
        "description": "Google Sheets-dən aktiv sürücüləri gətirir",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "get_loads",
        "description": "Mövcud yükləri gətirir",
        "input_schema": {
            "type": "object",
            "properties": {
                "truck_type": {
                    "type": "string",
                    "description": "Truck tipi: dry_van, reefer, flatbed"
                }
            },
            "required": []
        }
    },
    {
        "name": "send_sms",
        "description": "Sürücüyə SMS göndərir",
        "input_schema": {
            "type": "object",
            "properties": {
                "driver_name": {"type": "string"},
                "phone": {"type": "string"},
                "message": {"type": "string"}
            },
            "required": ["driver_name", "phone", "message"]
        }
    }
]

# ── Mock Claude cavabları ─────────────────
# Claude addım-addım belə düşünür:

# Addım 1 — əvvəl driverları gətir
step1 = {"stop_reason": "tool_use", "tool_name": "get_drivers", "tool_input": {}}

# Addım 2 — loadları gətir
step2 = {"stop_reason": "tool_use", "tool_name": "get_loads", "tool_input": {"truck_type": "dry_van"}}

# Addım 3 — SMS göndər
step3 = {"stop_reason": "tool_use", "tool_name": "send_sms", "tool_input": {
    "driver_name": "John Smith",
    "phone": "+15551234567",
    "message": "Sənə yaxın load var: Dallas → Chicago, $3200"
}}

# Addım 4 — bitdi
step4 = {"stop_reason": "end_turn", "text": "3 driverdən 2-sinə SMS göndərildi."}

# ── Loop 
steps = [step1, step2, step3, step4]

for step in steps:
    if step["stop_reason"] == "tool_use":
        print(f"🔧 Claude aləti çağırdı: {step['tool_name']}")

        if step["tool_name"] == "get_drivers":
            result = get_drivers()
            print(f"   {len(result)} driver tapıldı:")
            for d in result:
                print(f"   → {d['name']} | {d['city']} | {d['truck_type']}")

        elif step["tool_name"] == "get_loads":
            result = get_available_loads(
                truck_type=step["tool_input"].get("truck_type")
            )
            print(f"   {len(result)} load tapıldı:")
            for l in result:
                print(f"   → {l['id']} | {l['origin_city']} → {l['destination_city']} | ${l['rate']}")

        elif step["tool_name"] == "send_sms":
            inp = step["tool_input"]
            print(f"   📱 SMS göndərildi: {inp['driver_name']}")
            print(f"   Mesaj: {inp['message']}")

        print()

    elif step["stop_reason"] == "end_turn":
        print(f"✅ Agent bitdi: {step['text']}")