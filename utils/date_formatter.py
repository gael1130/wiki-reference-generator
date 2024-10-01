from datetime import datetime
from typing import Optional

MONTHS_FR = [
    "janvier", "février", "mars", "avril", "mai", "juin",
    "juillet", "août", "septembre", "octobre", "novembre", "décembre"
]

def format_date_french(date_obj: Optional[datetime]) -> str:
    if not date_obj:
        date_obj = datetime.now()
    return f"{date_obj.day} {MONTHS_FR[date_obj.month - 1]} {date_obj.year}"