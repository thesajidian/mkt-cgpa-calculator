def calculate_cgpa(grades, credit_hours):
    # Grade to grade points mapping
    grade_points_map = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    
    total_quality_points = 0
    total_credit_hours = 0
    
    for grade, credit_hour in zip(grades, credit_hours):
        grade_point = grade_points_map.get(grade, 0)
        quality_points = grade_point * credit_hour
        total_quality_points += quality_points
        total_credit_hours += credit_hour
    
    if total_credit_hours == 0:
        return 0
    
    cgpa = total_quality_points / total_credit_hours
    return cgpa

# Example usage
if __name__ == "__main__":
    # Example data
    courses = [
        {'course': 'MKT 2101', 'grade': 'A', 'credit_hours': 3},
        {'course': 'MKT 2201', 'grade': 'B', 'credit_hours': 3},
        {'course': 'ALD 2102', 'grade': 'C', 'credit_hours': 3},
        {'course': 'ALD 2103', 'grade': 'B', 'credit_hours': 3},
        {'course': 'ALD 2104', 'grade': 'A', 'credit_hours': 3},
        {'course': 'ALD 2105', 'grade': 'C', 'credit_hours': 3}
    ]

    grades = [course['grade'] for course in courses]
    credit_hours = [course['credit_hours'] for course in courses]

    cgpa = calculate_cgpa(grades, credit_hours)
    print(f"The CGPA is: {cgpa:.2f}")
