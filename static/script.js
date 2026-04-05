/**
 * FreshEye Frontend Logic
 *
 * TODO: Implement the functions below.
 * Use Copilot to help! Write comments describing what you want to do.
 */

let selectedFile = null;

// Handle file selection
document.getElementById('fileInput').addEventListener('change', function(e) {
    selectedFile = e.target.files[0];
    if (selectedFile) {
        // TODO: Show preview of the selected image
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('previewImage').src = e.target.result;
            document.getElementById('preview').style.display = 'block';
            document.getElementById('classifyBtn').style.display = 'inline-block';
        };
        reader.readAsDataURL(selectedFile);
    }
});

async function classifyImage() {
    if (!selectedFile) return;

    // TODO: Send the image to the /api/classify endpoint
    // and display the results

    const formData = new FormData();
    formData.append('file', selectedFile);

    document.getElementById('classifyBtn').textContent = 'Scanning...';

    try {
        const response = await fetch('/api/classify', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();

        // TODO: Display the results nicely
        document.getElementById('resultContent').innerHTML = `
            <p><strong>Item:</strong> ${data.item}</p>
            <p><strong>Freshness:</strong> ${data.freshness}</p>
            <p><strong>Confidence:</strong> ${(data.confidence * 100).toFixed(1)}%</p>
            <p><strong>Tips:</strong> ${data.tips}</p>
        `;
        document.getElementById('result').style.display = 'block';
    } catch (error) {
        document.getElementById('resultContent').innerHTML = `
            <p style="color: red;">Error: ${error.message}</p>
        `;
        document.getElementById('result').style.display = 'block';
    }

    document.getElementById('classifyBtn').textContent = 'Scan for Freshness';
}
