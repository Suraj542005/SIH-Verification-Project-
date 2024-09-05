function validateMarksheetForm(type) {
    // Correctly use backticks for template literals and variable interpolation
    const name = document.getElementById(`${type}Name`).value;
    const fatherName = document.getElementById(`${type}FatherName`).value;
    const motherName = document.getElementById(`${type}MotherName`).value;
    const dob = document.getElementById(`${type}Dob`).value;
    const schoolName = document.getElementById(`${type}SchoolName`).value;
    const rollNumber = document.getElementById(`${type}RollNumber`).value;
    const phoneNumber = document.getElementById(`${type}PhoneNumber`).value;
    const marksheetPhoto = document.getElementById(`${type}MarksheetPhoto`).files[0];

    // Check if any of the required fields are missing or not filled
    if (!name || !fatherName || !motherName || !dob || !schoolName || !rollNumber || !phoneNumber || !marksheetPhoto) {
        alert("Please fill all the fields and upload the photo of your marksheet.");
        return false;
    }

    // Display a success message upon successful submission
    alert(`${type.charAt(0).toUpperCase() + type.slice(1)} Marksheet details submitted successfully!`);
    return true;
}