# Expense Tracker

## Project Overview

This project is a simple full-stack Expense Tracker application developed as part of an assignment.

The main purpose of this application is to help users record and manage their daily expenses in an organized and reliable way.

The application allows users to:

* Add new expenses
* View all saved expenses
* Filter expenses by category (for example: Food, Travel, Shopping)
* Sort expenses by date (newest expenses first)
* View the total amount of the displayed expenses

The project was developed with a strong focus on clean backend logic, maintainable code structure, and real-world usability rather than only UI design.

It also handles practical scenarios such as:

* Preventing duplicate entries if users click submit multiple times
* Supporting browser refresh after submission
* Handling retry requests during network interruptions

This makes the application more reliable and closer to production-level behavior.

---

## Technology Stack

### Backend

The backend is developed using:

* Python
* FastAPI
* SQLAlchemy
* SQLite

### Frontend

The frontend is developed using:

* HTML
* JavaScript
* Bootstrap

---

## Features Implemented

### 1. Add Expense

Users can enter:

* Amount
* Category
* Description
* Date

and save the expense using the **Add Expense** button.

Each expense is stored permanently in the SQLite database.

---

### 2. View Expense List

All saved expenses are displayed in a table format showing:

* Amount
* Category
* Description
* Date

This helps users easily track and review their expenses.

---

### 3. Filter by Category

Users can filter expenses by entering a category name such as:

```text id="d4y7qf"
Food
```

and clicking **Apply Filter**.

Only matching category records will be displayed.

This improves usability when handling multiple expense entries.

---

### 4. Sort by Date (Newest First)

Users can click **Sort by Date** to display the latest expenses first.

Example:

```text id="t7l6z2"
2026-04-25
2026-04-24
2026-04-23
2026-04-21
```

Sorting is based on the expense date entered by the user, not the system creation timestamp.

This is more meaningful because users usually want to track when the expense actually happened.

---

### 5. Dynamic Total Calculation

The total expense amount is calculated automatically based on the currently displayed records.

This updates dynamically after filtering and sorting.

Example:

```text id="hl9sy1"
Food → ₹500
Travel → ₹3000
Shopping → ₹1600
```

Total:

```text id="lhr7jv"
₹5100
```

---

## Backend API Endpoints

### POST /expenses

This API is used to create a new expense.

Required fields:

* amount
* category
* description
* date
* request_id

The `request_id` helps prevent duplicate expense creation.

---

### GET /expenses

This API is used to fetch the expense list.

It supports:

* category-based filtering
* sorting by newest date first

Examples:

```text id="ee9fzk"
GET /expenses?category=Food
```

```text id="shbqj1"
GET /expenses?sort=date_desc
```

---

## Important Design Decisions

### SQLite for Data Storage

SQLite was selected because it is:

* lightweight
* easy to configure
* does not require a separate database server
* suitable for assignment-level and small production-like projects

---

### Idempotency (Duplicate Prevention)

A unique `request_id` is generated for every expense submission.

This prevents duplicate records when users:

* click submit multiple times
* refresh the browser after submission
* retry requests during network interruptions

This improves correctness and data reliability.

---

### Accurate Money Handling

Instead of using float values, `Decimal` and SQLAlchemy `Numeric(10,2)` were used.

This avoids precision issues in financial calculations.

Example:

```text id="rnnwqf"
0.1 + 0.2 ≠ 0.3
```

Using Decimal ensures accurate money handling.

---

## How to Run the Project Locally

## Backend

Open terminal:

```bash id="uy6b9u"
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Backend runs at:

```text id="pxdfw4"
http://127.0.0.1:8000
```

Swagger API documentation:

```text id="9trtx2"
http://127.0.0.1:8000/docs
```

---

## Frontend

Open another terminal:

```bash id="3wmggr"
cd frontend
python -m http.server 5500
```

Frontend runs at:

```text id="z4j45f"
http://127.0.0.1:5500
```

---

## Sample Test Data

| Amount | Category | Description       | Date       |
| ------ | -------- | ----------------- | ---------- |
| 500    | Food     | Lunch             | 2026-04-21 |
| 3000   | Travel   | Bus Charge        | 2026-04-23 |
| 1600   | Shopping | Clothes Purchased | 2026-04-15 |

---

## Trade-offs and Limitations

Due to assignment time constraints, the following features were not included:

* User authentication
* Advanced reporting dashboard
* Charts and analytics
* Export to Excel/PDF
* Multi-user support

Priority was given to:

* correctness
* clean architecture
* backend reliability
* duplicate prevention
* maintainable code structure

---

## Future Improvements

If more time is available, the following enhancements can be added:

* User authentication and authorization
* Monthly expense reports
* Excel and PDF export
* Category-wise summary dashboard
* Graphs and analytics
* Multi-user support
* Improved UI/UX experience

---

## Deployment

### Backend

Backend deployment can be done using Render.

### Frontend

Frontend deployment can be done using Netlify.

This provides a live deployed application link as requested in the assignment.

---



## Final Note

This project was built with a focus on simplicity, correctness, reliability, and maintainability.

Instead of adding unnecessary features, priority was given to creating a stable and production-minded application that demonstrates strong backend fundamentals and practical full-stack development skills.

Thank you.
