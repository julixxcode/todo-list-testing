from src.inventario_tareas.task_manager import TaskManager, TaskNotFoundError
from src.inventario_tareas.task import Priority, Status
import pytest


def test_add_task_creates_pending_task():
    tm = TaskManager()
    t = tm.add_task(task_id=1, title="Hacer tests", priority=Priority.HIGH)

    assert t.id == 1
    assert t.title == "Hacer tests"
    assert t.priority == Priority.HIGH
    assert t.status == Status.PENDING
    assert tm.get_task(1).title == "Hacer tests"


def test_add_task_rejects_duplicate_id():
    tm = TaskManager()
    tm.add_task(1, "primera", Priority.LOW)

    with pytest.raises(ValueError):
        tm.add_task(1, "repetida", Priority.HIGH)


def test_get_task_raises_if_not_found():
    tm = TaskManager()
    with pytest.raises(TaskNotFoundError):
        tm.get_task(99)


def test_update_status_changes_status_and_persists():
    tm = TaskManager()
    tm.add_task(10, "Actualizar estado", Priority.MEDIUM)
    updated = tm.update_status(10, Status.DONE)

    assert updated.status == Status.DONE
    assert tm.get_task(10).status == Status.DONE


def test_update_status_accepts_string():
    tm = TaskManager()
    tm.add_task(2, "migrar", Priority.LOW)
    updated = tm.update_status(2, "in_progress")

    assert updated.status == Status.IN_PROGRESS


def test_list_tasks_filters_by_status():
    tm = TaskManager()
    tm.add_task(1, "a", Priority.LOW)
    tm.add_task(2, "b", Priority.LOW)
    tm.update_status(2, Status.DONE)

    done_tasks = tm.list_tasks(Status.DONE)
    assert len(done_tasks) == 1
    assert done_tasks[0].id == 2

    pending_tasks = tm.list_tasks("pending")
    assert len(pending_tasks) == 1
    assert pending_tasks[0].id == 1


def test_as_dict_returns_serializable_structure():
    tm = TaskManager()
    tm.add_task(1, "Doc", Priority.HIGH)
    tm.add_task(2, "Test", Priority.MEDIUM)
    tm.update_status(2, "done")

    data = tm.as_dict()

    assert data[1]["title"] == "Doc"
    assert data[2]["status"] == "DONE"
    assert "priority" in data[1]
