
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class EvaRecord:
    country: str
    date: Optional[datetime]
    duration_hours: float
