document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('tbChart').getContext('2d');
    const tbChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Tuberculose', 'Non Ateints'],
            datasets: [{
                data: [parseInt(document.querySelector('.card:nth-child(2)').textContent.split(":")[1]), 
                       parseInt(document.querySelector('.card:nth-child(3)').textContent.split(":")[1])],
                backgroundColor: ['#ff6b6b', '#6bff6b'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        color: '#e0e0e0'
                    }
                }
            }
        }
    });
});
