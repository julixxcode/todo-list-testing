from src.inventario_tareas.task import Task, Priority, Status
import pytest


def test_task_creation_defaults_pending():
    task = Task(id=1, title="Prueba", priority=Priority.HIGH)
    assert task.id == 1
    assert task.title == "Prueba"
    assert task.priority == Priority.HIGH
    assert task.status == Status.PENDING


def test_task_with_status_creates_new_instance_not_mutating():
    original = Task(id=2, title="Original", priority=Priority.LOW)
    updated = original.with_status(Status.DONE)

    assert original.status == Status.PENDING
    assert updated.status == Status.DONE
    assert updated.id == original.id
    assert updated is not original


def test_task_serialize_returns_clean_dict():
    task = Task(id=5, title="Serializar", priority=Priority.MEDIUM, status=Status.IN_PROGRESS)
    data = task.serialize()
    assert data == {
        "id": 5,
        "title": "Serializar",
        "priority": "MEDIUM",
        "status": "IN_PROGRESS",
    }


def test_validate_priority_accepts_str_and_enum():
    assert Task.validate_priority("low") == Priority.LOW
    assert Task.validate_priority(Priority.HIGH) == Priority.HIGH


def test_validate_priority_raises_on_invalid():
    with pytest.raises(ValueError):
        Task.validate_priority("ULTRA")


def test_validate_status_accepts_str_and_enum():
    assert Task.validate_status("done") == Status.DONE
    assert Task.validate_status(Status.PENDING) == Status.PENDING


def test_validate_status_raises_on_invalid():
    with pytest.raises(ValueError):
        Task.validate_status("CANCELADA")
