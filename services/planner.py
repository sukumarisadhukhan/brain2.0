from services.priority_engine import rank_tasks


def build_plan(tasks, available_minutes):
    """
    Build a realistic plan based on
    priority and available time.
    """

    ranked = rank_tasks(tasks)

    selected = []
    total_minutes = 0

    for task, score in ranked:

        duration = task.estimated_minutes or 30

        if total_minutes + duration <= available_minutes:

            selected.append({
                "task": task,
                "score": score,
                "minutes": duration
            })

            total_minutes += duration

    return {
        "tasks": selected,
        "planned_minutes": total_minutes,
        "available_minutes": available_minutes,
        "remaining_minutes":
            available_minutes - total_minutes
    }