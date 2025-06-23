document.addEventListener('DOMContentLoaded', () => {
    const imageUpload = document.getElementById('imageUpload');
    const uploadButton = document.getElementById('uploadButton');
    const fileNameDisplay = document.getElementById('fileNameDisplay');
    const uploadedImage = document.getElementById('uploadedImage');
    const previewPlaceholder = document.getElementById('previewPlaceholder');
    const predictButton = document.getElementById('predictButton');
    const detectionStatus = document.getElementById('detectionStatus');
    const confidenceScore = document.getElementById('confidenceScore');

    let selectedFile = null;

    uploadButton.addEventListener('click', () => {
        imageUpload.click();
    });

    imageUpload.addEventListener('change', (event) => {
        selectedFile = event.target.files[0];
        if (selectedFile) {
            fileNameDisplay.textContent = selectedFile.name;
            predictButton.disabled = false;

            const reader = new FileReader();
            reader.onload = (e) => {
                uploadedImage.src = e.target.result;
                uploadedImage.style.display = 'block';
                previewPlaceholder.style.display = 'none';
            };
            reader.readAsDataURL(selectedFile);

            detectionStatus.textContent = 'En attente de la prediction';
            detectionStatus.className = 'result-value initial-state';
            confidenceScore.textContent = 'N/A';
            confidenceScore.className = 'result-value initial-state';

        } else {
            fileNameDisplay.textContent = '';
            predictButton.disabled = true;
            uploadedImage.style.display = 'none';
            previewPlaceholder.style.display = 'block';
        }
    });

    predictButton.addEventListener('click', async () => {
        if (!selectedFile) {
            alert('Veuillez d\'abord sélectionner une image.');
            return;
        }

        

        // Ici tu pourrais envoyer les données au backend via un formulaire caché ou AJAX
        // Mais pour ce projet on simule la prédiction

        detectionStatus.textContent = 'Prédiction en cours...';
        detectionStatus.className = 'result-value initial-state';
        confidenceScore.textContent = 'Chargement...';
        confidenceScore.className = 'result-value initial-state';
        predictButton.disabled = true;

        await new Promise(resolve => setTimeout(resolve, 2000)); // Simule un délai

        const simulatedPrediction = Math.random();
        const threshold = 0.5;

        let statusText = '';
        let confidenceText = '';
        let statusClass = '';

        if (simulatedPrediction > threshold) {
            statusText = 'Tuberculose détectée';
            statusClass = 'result-value positive';
            confidenceText = `${(simulatedPrediction * 100).toFixed(2)}%`;
        } else {
            statusText = 'Aucune tuberculose détectée';
            statusClass = 'result-value negative';
            confidenceText = `${((1 - simulatedPrediction) * 100).toFixed(2)}%`;
        }

        detectionStatus.textContent = statusText;
        detectionStatus.className = statusClass;
        confidenceScore.textContent = confidenceText;
        confidenceScore.className = statusClass;

        // Tu pourrais stocker les infos du patient dans sessionStorage/localStorage si nécessaire
        console.log("Patient:", { nom, age, genre, fichier: selectedFile.name });

        predictButton.disabled = false;
    });
});
