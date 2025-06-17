document.addEventListener('DOMContentLoaded', () => {
    const imageUpload = document.getElementById('imageUpload');
    const uploadButton = document.getElementById('uploadButton');
    const fileNameDisplay = document.getElementById('fileNameDisplay');
    const imagePreview = document.getElementById('imagePreview');
    const uploadedImage = document.getElementById('uploadedImage');
    const previewPlaceholder = document.getElementById('previewPlaceholder');
    const predictButton = document.getElementById('predictButton');
    const detectionStatus = document.getElementById('detectionStatus');
    const confidenceScore = document.getElementById('confidenceScore');

    let selectedFile = null;

    // Trigger file input click when "Choose Image" button is clicked
    uploadButton.addEventListener('click', () => {
        imageUpload.click();
    });

    imageUpload.addEventListener('change', (event) => {
        selectedFile = event.target.files[0];
        if (selectedFile) {
            fileNameDisplay.textContent = selectedFile.name;
            predictButton.disabled = false; // Enable predict button

            // Display image preview
            const reader = new FileReader();
            reader.onload = (e) => {
                uploadedImage.src = e.target.result;
                uploadedImage.style.display = 'block';
                previewPlaceholder.style.display = 'none';
            };
            reader.readAsDataURL(selectedFile);

            // Reset results
            detectionStatus.textContent = 'Awaiting Prediction';
            detectionStatus.className = 'result-value initial-state';
            confidenceScore.textContent = 'N/A';
            confidenceScore.className = 'result-value initial-state';

        } else {
            fileNameDisplay.textContent = '';
            predictButton.disabled = true; // Disable predict button
            uploadedImage.style.display = 'none';
            previewPlaceholder.style.display = 'block';
        }
    });

    predictButton.addEventListener('click', async () => {
        if (!selectedFile) {
            alert('Please select an image first.');
            return;
        }

        // --- Simulate API call to your ML model ---
        // In a real application, you would send `selectedFile` to your backend
        // where your ML model is hosted (e.g., using Flask, FastAPI, Node.js).
        // The backend would then process the image and return the prediction.

        detectionStatus.textContent = 'Predicting...';
        detectionStatus.className = 'result-value initial-state';
        confidenceScore.textContent = 'Loading...';
        confidenceScore.className = 'result-value initial-state';
        predictButton.disabled = true; // Disable button during prediction

        try {
            // Simulate a network delay (replace with actual fetch to your API)
            await new Promise(resolve => setTimeout(resolve, 2000)); // 2-second delay

            // --- Simulate ML Model Response ---
            // Replace this with the actual response from your backend
            const simulatedPrediction = Math.random(); // A random number between 0 and 1
            const threshold = 0.5; // Example threshold for TB detection

            let statusText = '';
            let confidenceText = '';
            let statusClass = '';

            if (simulatedPrediction > threshold) {
                statusText = 'Tuberculosis Detected';
                statusClass = 'result-value positive';
                confidenceText = `${(simulatedPrediction * 100).toFixed(2)}%`;
            } else {
                statusText = 'No Tuberculosis Detected';
                statusClass = 'result-value negative';
                confidenceText = `${((1 - simulatedPrediction) * 100).toFixed(2)}%`; // Confidence in being negative
            }

            detectionStatus.textContent = statusText;
            detectionStatus.className = statusClass; // Apply dynamic class for color
            confidenceScore.textContent = confidenceText;
            confidenceScore.className = statusClass; // Apply dynamic class for color

        } catch (error) {
            console.error('Error during prediction:', error);
            detectionStatus.textContent = 'Error during prediction';
            detectionStatus.className = 'result-value initial-state';
            confidenceScore.textContent = 'N/A';
            confidenceScore.className = 'result-value initial-state';
            alert('An error occurred during prediction. Please try again.');
        } finally {
            predictButton.disabled = false; // Re-enable button
        }
    });
});