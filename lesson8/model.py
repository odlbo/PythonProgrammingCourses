from dataclasses import dataclass, field


@dataclass
class Person:
    id: int = field(default_factory=int)
    phone_number: str = field(default_factory=str)
    first_name: str = field(default_factory=str)
    last_name: str = field(default_factory=str)
    surname: str = field(default_factory=str)
