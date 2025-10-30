from __future__ import annotations
from typing import Dict, List, Optional
from .task import Task, Status, Priority


class TaskNotFoundError(Exception):
    """Error cuando no se encuentra una tarea."""


class TaskManager:
    """
    Administra tareas en memoria.
    """
    def __init__(self) -> None:
        self._tasks: Dict[int, Task] = {}

    def add_task(self, task_id: int, title: str, priority: Priority | str) -> Task:
        """
        Crea y guarda una nueva tarea.
        """
        if task_id in self._tasks:
            raise ValueError(f"La tarea con id {task_id} ya existe")

        validated_priority = Task.validate_priority(priority)
        task = Task(id=task_id, title=title.strip(), priority=validated_priority)
        self._tasks[task_id] = task
        return task

    def get_task(self, task_id: int) -> Task:
        """
        Retorna la tarea con ese id.
        """
        try:
            return self._tasks[task_id]
        except KeyError as e:
            raise TaskNotFoundError(f"No existe tarea con id {task_id}") from e

    def update_status(self, task_id: int, new_status: Status | str) -> Task:
        """
        Cambia el estado de la tarea.
        """
        task = self.get_task(task_id)
        validated_status = Task.validate_status(new_status)
        updated_task = task.with_status(validated_status)
        self._tasks[task_id] = updated_task
        return updated_task

    def list_tasks(self, status: Optional[Status | str] = None) -> List[Task]:
        """
        Lista todas las tareas o filtra por estado.
        """
        if status is None:
            return list(self._tasks.values())

        validated_status = Task.validate_status(status)
        return [t for t in self._tasks.values() if t.status == validated_status]

    def as_dict(self) -> Dict[int, dict]:
        """
        Exporta todas las tareas como dict serializable.
        """
        return {tid: task.serialize() for tid, task in self._tasks.items()}
