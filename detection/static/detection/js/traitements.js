document.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('treatmentChart').getContext('2d');

    const totalPatients = parseInt(document.getElementById('totalPatients').textContent);
    const tbDetected = parseInt(document.getElementById('tbDetected').textContent);
    const nonTb = parseInt(document.getElementById('nonTb').textContent);

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Tuberculose détectée', 'Non atteints'],
            datasets: [{
                data: [tbDetected, nonTb],
                backgroundColor: ['#ff6b6b', '#6bff6b'],
                borderColor: '#24243e',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: {
                        color: '#e0e0e0'
                    }
                }
            }
        }
    });
});
