document.addEventListener("DOMContentLoaded", function () {
    // === Sécurité : Protection si certains éléments n'existent pas ===
    const kpiPatients = document.getElementById("kpi-patients");
    const kpiCas = document.getElementById("kpi-cas");
    const kpiSource = document.getElementById("kpi-source");
    const kpiDate = document.getElementById("kpi-date");

    if (kpiPatients) kpiPatients.textContent = Math.floor(Math.random() * 100) + 100;
    if (kpiCas) kpiCas.textContent = Math.floor(Math.random() * 50) + 20;
    if (kpiSource) kpiSource.textContent = "Air contaminé";
    if (kpiDate) kpiDate.textContent = new Date().toISOString().split('T')[0];

    // === Graphique 1 : Nombre de consultations par mois ===
    const ctx1 = document.getElementById("chart-consultations");
    if (ctx1) {
        new Chart(ctx1, {
            type: 'bar',
            data: {
                labels: ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin'],
                datasets: [{
                    label: 'Consultations',
                    data: [12, 19, 3, 5, 20, 30],
                    backgroundColor: '#4e79a7',
                    borderRadius: 10,
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false } },
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    }

    // === Graphique 2 : Source d'infection ===
    const ctx2 = document.getElementById("chart-source");
    if (ctx2) {
        new Chart(ctx2, {
            type: 'pie',
            data: {
                labels: ['Air', 'Contact Humain', 'Surface', 'Autres'],
                datasets: [{
                    data: [45, 25, 15, 15],
                    backgroundColor: ['#f28e2b', '#e15759', '#76b7b2', '#59a14f'],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { position: 'bottom' } }
            }
        });
    }

    // === Graphique 3 : Précision du modèle IA ===
    const ctx3 = document.getElementById("chart-modele");
    if (ctx3) {
        new Chart(ctx3, {
            type: 'doughnut',
            data: {
                labels: ['Précision', 'Erreur'],
                datasets: [{
                    data: [94, 6],
                    backgroundColor: ['#edc948', '#bab0ab'],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { position: 'bottom' } }
            }
        });
    }

    // === Graphique 4 : Taux de détection sur 6 mois ===
    const ctx4 = document.getElementById("chart-profit");
    if (ctx4) {
        new Chart(ctx4, {
            type: 'line',
            data: {
                labels: ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin'],
                datasets: [{
                    label: 'Taux de détection (%)',
                    data: [60, 70, 80, 75, 85, 90],
                    fill: true,
                    borderColor: '#59a14f',
                    backgroundColor: 'rgba(89, 161, 79, 0.2)',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { position: 'top' } },
                scales: {
                    y: { min: 0, max: 100 }
                }
            }
        });
    }
});
