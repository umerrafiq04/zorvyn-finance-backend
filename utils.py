def calculate_summary(records):
    total_income = 0
    total_expense = 0
    category_summary = {}

    for r in records:
        if r.type == "income":
            total_income += r.amount
        elif r.type == "expense":
            total_expense += r.amount

        # category-wise
        if r.category not in category_summary:
            category_summary[r.category] = 0

        category_summary[r.category] += r.amount

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense,
        "category_summary": category_summary
    }