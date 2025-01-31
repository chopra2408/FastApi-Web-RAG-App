function validateURL() {
    const urlInput = document.getElementById('url-input');
    const warning = document.getElementById('url-warning');

    if (!urlInput.value.trim()) {
        warning.textContent = "⚠️ URL cannot be empty!";
    } else {
        warning.textContent = "";
    }
}

function validateQuery() {
    const queryInput = document.getElementById('query-input');
    const warning = document.getElementById('query-warning');

    if (!queryInput.value.trim()) {
        warning.textContent = "⚠️ Please enter a question.";
    } else {
        warning.textContent = "";
    }
}

async function processURL() {
    const url = document.getElementById('url-input').value.trim();
    const warning = document.getElementById('url-warning');
    const button = document.getElementById('process-btn');
    const spinner = document.getElementById('loading');

    if (!url) {
        warning.textContent = "⚠️ URL cannot be empty!";
        return;
    }

    warning.textContent = "";
    button.disabled = true;
    spinner.classList.remove('hidden');

    try {
        const response = await fetch('http://localhost:8000/process_url', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url, prompt: "" })
        });

        const data = await response.json();
        if (response.ok) {
            warning.style.color = "#00ff00";
            warning.textContent = "✅ URL processed successfully!";
        } else {
            warning.textContent = "❌ " + data.detail;
        }
    } catch (error) {
        warning.textContent = "⚠️ Error: " + error.message;
    }

    button.disabled = false;
    spinner.classList.add('hidden');
}

async function askQuestion() {
    const query = document.getElementById('query-input').value.trim();
    const url = document.getElementById('url-input').value.trim();
    const warning = document.getElementById('query-warning');
    const button = document.getElementById('query-btn');
    const responseContainer = document.getElementById('response-container');

    if (!query || !url) {
        warning.textContent = "⚠️ Please enter a URL and ask a question.";
        return;
    }

    warning.textContent = "";
    button.disabled = true;
    responseContainer.innerHTML = "⏳ Processing your request...";

    try {
        const response = await fetch('http://localhost:8000/query', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url, prompt: query })
        });

        const data = await response.json();
        responseContainer.innerHTML = `<p><strong>Answer:</strong> ${data.answer}</p>`;
    } catch (error) {
        responseContainer.innerHTML = "⚠️ Error: " + error.message;
    }

    button.disabled = false;
}
