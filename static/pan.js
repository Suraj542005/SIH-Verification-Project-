function validatePanForm() {
    const panNumber = document.getElementById('panNumber').value;
    const name = document.getElementById('panName').value;
    const fatherName = document.getElementById('panFatherName').value;
    const dob = document.getElementById('panDob').value;
    const panPhoto = document.getElementById('panPhoto').files[0];

    if (!panNumber || !name || !fatherName || !dob || !panPhoto) {
        alert("Please fill all the fields and upload the photo of your PAN card.");
        return false;
    }

    // Validate PAN number format
    const panPattern = /^[A-Z]{5}[0-9]{4}[A-Z]{1}$/;
    if (!panPattern.test(panNumber)) {
        alert("Invalid PAN number format. Please enter a valid PAN number.");
        return false;
    }

    alert("PAN card details submitted successfully!");
    return true;
}