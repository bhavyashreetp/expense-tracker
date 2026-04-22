const API_URL = "http://127.0.0.1:8000";

let currentSort = "";

const form = document.getElementById("expenseForm");

form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const data = {
        amount: document.getElementById("amount").value,
        category: document.getElementById("category").value,
        description: document.getElementById("description").value,
        date: document.getElementById("date").value,

        // Prevent duplicate submits
        request_id: crypto.randomUUID()
    };

    try {
        const response = await fetch(`${API_URL}/expenses`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            alert("Failed to add expense");
            return;
        }

        form.reset();

        // Reload data after adding
        loadExpenses(currentSort);

    } catch (error) {
        console.error(error);
        alert("Server error while adding expense");
    }
});

async function loadExpenses(sort = currentSort) {
    currentSort = sort;

    const category = document.getElementById("filterCategory").value.trim();

    let url = `${API_URL}/expenses?`;

    // Filter by category
    if (category) {
        url += `category=${encodeURIComponent(category)}&`;
    }

    // Sort by newest date
    if (sort) {
        url += `sort=${sort}`;
    }

    try {
        const response = await fetch(url);
        const expenses = await response.json();

        const table = document.getElementById("expenseTable");
        table.innerHTML = "";

        let total = 0;

        expenses.forEach(exp => {
            total += parseFloat(exp.amount);

            table.innerHTML += `
                <tr>
                    <td>₹${exp.amount}</td>
                    <td>${exp.category}</td>
                    <td>${exp.description}</td>
                    <td>${exp.date}</td>
                </tr>
            `;
        });

        document.getElementById("total").innerText =
            `Total: ₹${total.toFixed(2)}`;

    } catch (error) {
        console.error(error);
        alert("Unable to load expenses");
    }
}

// Apply category filter
function applyFilter() {
    loadExpenses(currentSort);
}

// Sort by newest date
function sortByDate() {
    loadExpenses("date_desc");
}

// Initial load
loadExpenses();