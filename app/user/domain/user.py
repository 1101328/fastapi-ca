from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    name: str
    email: str
    password: str
    memo: str | None
    created_at: datetime
    updated_at: datetime