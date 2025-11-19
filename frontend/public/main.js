
// -----------------------------
// API base path
const API_BASE = "/api";

// -----------------------------
// Health check function
async function checkHealth() {
    const resultDiv = document.getElementById("result");
    const statusDiv = document.getElementById("status");

    try {
        const response = await fetch(`${API_BASE}/health`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();

        resultDiv.style.display = "block";
        resultDiv.innerHTML = `
            <h3>Health Check OK</h3>
            <pre>${JSON.stringify(data, null, 2)}</pre>
        `;
        statusDiv.innerHTML = "<strong>Status:</strong> Application runs!";
    } catch (error) {
        resultDiv.style.display = "block";
        resultDiv.innerHTML = `<h3>Error: ${error.message}</h3>`;
        console.error("Health check error:", error);
    }
}

// -----------------------------
// Load users function
async function loadUsers() {
    const usersListDiv = document.getElementById("users-list");
    usersListDiv.innerHTML = '<div class="loading">Loading users...</div>';

    try {
        const response = await fetch(`${API_BASE}/users`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const users = await response.json();

        if (!users.length) {
            usersListDiv.innerHTML = '<div class="loading">No users found</div>';
            return;
        }

        const userCards = users.map(user => `
            <div class="user-card">
                <h3 class="user-name">${user.name}</h3>
                <p class="user-email">${user.email}</p>
                <div class="user-details">
                    <span class="user-age">${user.age} years</span>
                    <span class="user-role role-${user.role}">${user.role}</span>
                </div>
            </div>
        `).join("");

        usersListDiv.innerHTML = userCards;
    } catch (error) {
        usersListDiv.innerHTML = `
            <div class="error">
                Error loading users: ${error.message}
            </div>
        `;
        console.error("Error loading users:", error);
    }
}

// -----------------------------
// Event listeners setup (single block)
document.addEventListener("DOMContentLoaded", () => {
    const healthButton = document.getElementById("health-btn"); // specific button ID
    const loadUsersButton = document.getElementById("load-users-btn");

    if (healthButton) healthButton.addEventListener("click", checkHealth);
    if (loadUsersButton) loadUsersButton.addEventListener("click", loadUsers);
});
