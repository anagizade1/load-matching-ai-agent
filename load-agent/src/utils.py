def format_phone(phone):
  if phone.startswith("+"):
    return phone
  else: 
    return "+1" + phone


def km_to_miles(km):
    return km * 0.621371