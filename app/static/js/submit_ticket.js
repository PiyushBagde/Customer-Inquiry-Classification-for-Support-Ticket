document.getElementById('ticketForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/api/tickets', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.success) {
            showAlert('success', 'Ticket submitted successfully!');
            e.target.reset();
        } else {
            showAlert('error', result.error || 'Error submitting ticket.');
        }
    } catch (error) {
        showAlert('error', 'Error submitting ticket. Please try again.');
    }
});

function showAlert(type, message) {
    const successAlert = document.getElementById('successAlert');
    const errorAlert = document.getElementById('errorAlert');
    const successMessage = document.getElementById('successMessage');
    const errorMessage = document.getElementById('errorMessage');
    const alertContainer = document.getElementById('alert');

    alertContainer.classList.remove('hidden');

    if (type === 'success') {
        successAlert.classList.remove('hidden');
        errorAlert.classList.add('hidden');
        successMessage.textContent = message;
    } else {
        errorAlert.classList.remove('hidden');
        successAlert.classList.add('hidden');
        errorMessage.textContent = message;
    }

    setTimeout(() => {
        alertContainer.classList.add('hidden');
    }, 5000);
}
