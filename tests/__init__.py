from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Literal


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
    Inmutable (frozen=True) para que el TaskManager controle los cambios.
    Cumple SRP: esta clase solo modela una tarea, no la administra.
    """
    id: int
    title: str
    priority: Priority
    status: Status = Status.PENDING

    def with_status(self, new_status: Status) -> "Task":
        """
        Devuelve una NUEVA tarea con el estado actualizado.
        No muta la instancia original -> más seguro para testing.
        """
        return Task(
            id=self.id,
            title=self.title,
            priority=self.priority,
            status=new_status,
        )

    def serialize(self) -> dict[str, str | int]:
        """
        Convierte la tarea a dict simple.
        Útil para persistencia futura / API.
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
