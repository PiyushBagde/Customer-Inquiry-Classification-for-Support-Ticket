async function fetchDashboardData() {
            try {
                const response = await fetch('/api/dashboard-data');
                const data = await response.json();

                const insightsResponse = await fetch('/api/dashboard-insights');
                const insightsData = await insightsResponse.json();

                if (data.success) {
                    updateSummaryCards(data.summary);
                    initializeCharts(data.charts);
                    initializeTopKeywordsChart(data.topKeywords);
                    updateInsights(data.insights);
                }
            } catch (error) {
                console.error('Error fetching dashboard data:', error);
            }

             try {
                const insightsResponse = await fetch('/api/dashboard-insights');
                const insightsData = await insightsResponse.json();

                if (insightsData.success) {
                    updateInsights(insightsData.insights);
                } else {
                    console.error("Error fetching insights:", insightsData.error);
                }
            } catch (error) {
                console.error('Error fetching insights data:', error);
            }
        }

function initializeTopKeywordsChart(topKeywords) {
    new Chart(document.getElementById('topKeywordsChart'), {
        type: 'bar',
        data: {
            labels: topKeywords.labels,
            datasets: [{
                label: 'Frequency',
                data: topKeywords.data,
                backgroundColor: '#4F46E5'
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Top Keywords and Phrases'
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function updateInsights(insights) {
    // Update Inquiry Types List
    const inquiryTypesList = document.getElementById('inquiryTypesList');
    inquiryTypesList.innerHTML = insights.commonTypes.map(type => `
        <div class="bg-gray-50 p-4 rounded-lg">
            <div class="flex justify-between items-center mb-2">
                <h4 class="font-medium text-gray-900">${type.name}</h4>
                <span class="text-sm text-indigo-600 font-medium">${type.percentage}%</span>
            </div>
            <div class="w-full bg-gray-200 rounded-full h-2">
                <div class="bg-indigo-600 h-2 rounded-full" style="width: ${type.percentage}%"></div>
            </div>
            <p class="text-sm text-gray-600 mt-2">${type.description}</p>
        </div>
    `).join('');

    // Update Keyword Analysis
    const keywordAnalysis = document.getElementById('keywordAnalysis');
    keywordAnalysis.innerHTML = insights.keywordsByType.map(type => `
        <div class="border-b border-gray-200 pb-4 last:border-b-0">
            <h4 class="font-medium text-gray-900 mb-2">${type.inquiryType}</h4>
            <div class="flex flex-wrap gap-2">
                ${type.keywords.map(keyword => `
                    <span class="px-3 py-1 bg-indigo-100 text-indigo-800 rounded-full text-sm">
                        ${keyword.word} (${keyword.count})
                    </span>
                `).join('')}
            </div>
        </div>
    `).join('');
}

function updateSummaryCards(summary) {
    document.getElementById('totalTickets').textContent = summary.total_tickets;
    document.getElementById('openTickets').textContent = summary.open_tickets;
    document.getElementById('resolvedTickets').textContent = summary.resolved_tickets;
    document.getElementById('resolutionRate').textContent =
        `${((summary.resolved_tickets / summary.total_tickets) * 100).toFixed(1)}%`;
}

function initializeCharts(chartData) {
    // Ticket Type Distribution Chart
    new Chart(document.getElementById('ticketTypeChart'), {
        type: 'pie',
        data: {
            labels: chartData.ticket_types.labels,
            datasets: [{
                data: chartData.ticket_types.data,
                backgroundColor: [
                    '#4F46E5', '#7C3AED', '#EC4899', '#F59E0B', '#10B981'
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });

    // Products Chart
    const productData = chartData.products.labels.map((label, index) => ({
        label: label,
        count: chartData.products.data[index]
    }));

    // Sort the array by count in descending order
    productData.sort((a, b) => b.count - a.count);

    // Create new arrays for sorted labels and data
    const sortedLabels = productData.map(item => item.label);
    const sortedData = productData.map(item => item.count);

    new Chart(document.getElementById('productChart'), {
        type: 'bar',
        data: {
            labels: sortedLabels,
            datasets: [{
                label: 'Tickets',
                data: sortedData,
                backgroundColor: '#4F46E5',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            indexAxis: 'y',  // Make it a horizontal bar chart
            plugins: {
                legend: {
                    display: false  // Hide legend since we only have one dataset
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    grid: {
                        drawBorder: false
                    },
                    ticks: {
                        precision: 0  // Show whole numbers only
                    }
                },
                y: {
                    grid: {
                        display: false  // Hide y-axis grid lines
                    }
                }
            }
        }
    });

}

// Initialize dashboard
fetchDashboardData();

// Refresh dashboard data every 30 seconds
setInterval(fetchDashboardData, 30000);