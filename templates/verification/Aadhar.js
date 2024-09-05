// Validate Aadhaar Card Form
function validateAadhaarForm() {
    const aadhaarNumber = document.getElementById("aadhaarNumber").value;
    const aadhaarPattern = /^[0-9]{12}$/;
    const pincodePattern = /^[0-9]{6}$/;
    const mobilePattern = /^[0-9]{10}$/;
    const cardPhotoFile = document.getElementById("aadhaarCardPhoto").files[0];

    if (!aadhaarPattern.test(aadhaarNumber)) {
        alert("Please enter a valid 12-digit Aadhaar number.");
        return false;
    }

    if (!pincodePattern.test(document.getElementById("aadhaarPincode").value)) {
        alert("Please enter a valid 6-digit pincode.");
        return false;
    }

    if (!mobilePattern.test(document.getElementById("aadhaarMobile").value)) {
        alert("Please enter a valid 10-digit mobile number.");
        return false;
    }

    if (!cardPhotoFile) {
        alert("Please upload a photo of your Aadhaar card.");
        return false;
    }

    alert("Aadhaar Card details submitted successfully!");
    return true;
}