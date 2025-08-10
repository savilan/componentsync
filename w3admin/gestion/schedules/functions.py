def format_schedule_data(schedule):
    return {
        "id": schedule.id,
        "title": schedule.title,
        "start_day": schedule.start_day.strftime("%Y-%m-%d"),
        "start_datetime": str(schedule.start_datetime),
        "end_day": schedule.end_day.strftime("%Y-%m-%d"),
        "end_datetime": str(schedule.end_datetime),
        "status_id": schedule.status_id,
        "condition_id": schedule.condition_id,
        "frecuency_id": schedule.frecuency_id,
        "count": schedule.count,
        "created_at": schedule.created_at.strftime("%Y-%m-%d %H:%M:%S"),
    }