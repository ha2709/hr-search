import models


def apply_filters(query, status=None, location=None, department=None, position=None):
    # print(79, status)
    if status:
        query = query.filter(models.Employee.status.has(name=status[0]))
    if location:
        query = query.filter(models.Employee.location.has(name=location))
    if department:
        query = query.filter(models.Employee.department.has(name=department))
    if position:
        query = query.filter(models.Employee.position.has(title=position))
    results = query.all()
    return results
