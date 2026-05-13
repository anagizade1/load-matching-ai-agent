def get_available_loads(truck_type=None, origin_state=None):
    loads = [
        {"id": "L001", "origin_city": "Houston", "origin_state": "TX", 
         "destination_city": "Chicago", "truck_type": "dry_van", "rate": 3200},
        {"id": "L002", "origin_city": "Fort Worth", "origin_state": "TX",
         "destination_city": "Los Angeles", "truck_type": "dry_van", "rate": 4100},
        {"id": "L003", "origin_city": "Atlanta", "origin_state": "GA",
         "destination_city": "Miami", "truck_type": "reefer", "rate": 3800},
        {"id": "L004", "origin_city": "Phoenix", "origin_state": "AZ",
         "destination_city": "Denver", "truck_type": "flatbed", "rate": 2600},
    ]
    
    if truck_type:
        loads = [l for l in loads if l["truck_type"] == truck_type]
    
    return loads