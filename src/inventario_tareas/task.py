
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class Priority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Status(Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


@dataclass(frozen=True)
class Task:
    """
    Representa una tarea individual.
    Es inmutable (frozen=True) para seguridad y claridad.
    """
    id: int
    title: str
    priority: Priority
    status: Status = Status.PENDING

    def with_status(self, new_status: Status) -> "Task":
        """
        Devuelve una nueva instancia con estado actualizado.
        """
        return Task(
            id=self.id,
            title=self.title,
            priority=self.priority,
            status=new_status,
        )

    def serialize(self) -> dict[str, str | int]:
        """
        Convierte la tarea a un diccionario plano.
        """
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority.value,
            "status": self.status.value,
        }

    @staticmethod
    def validate_priority(value: str | Priority) -> Priority:
        if isinstance(value, Priority):
            return value
        try:
            return Priority(value.upper())
        except Exception as e:
            raise ValueError(f"Prioridad inválida: {value}") from e

    @staticmethod
    def validate_status(value: str | Status) -> Status:
        if isinstance(value, Status):
            return value
        try:
            return Status(value.upper())
        except Exception as e:
            raise ValueError(f"Estado inválido: {value}") from e
