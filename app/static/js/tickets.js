
function filterTickets(category, status) {
    const tickets = document.querySelectorAll('.ticket-item');
    tickets.forEach(ticket => {
        if (category === 'all' || ticket.dataset.type === category) {
            if (status === 'all' || ticket.dataset.status === status) {
                ticket.style.display = 'block';
            } else {
                ticket.style.display = 'none';
            }
        } else {
            ticket.style.display = 'none';
        }
    });
}

function filterStatus(status) {
    const tickets = document.querySelectorAll('.ticket-item');
    tickets.forEach(ticket => {
        if (status === 'all' || ticket.dataset.status === status) {
            ticket.style.display = 'block';
        } else {
            ticket.style.display = 'none';
        }
    });
}

function updateTicketStatus(ticketId, newStatus) {
    fetch(`/api/tickets/${ticketId}/status`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ status: newStatus })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.reload();
        } else {
            alert('Error updating ticket status');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error updating ticket status');
    });
}