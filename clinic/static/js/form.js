document.addEventListener('DOMContentLoaded', function() {

    // Get references to the insurance radio buttons and the details section
    const insuranceYesRadio = document.getElementById('insuranceYes');
    const insuranceNoRadio = document.getElementById('insuranceNo');
    const insuranceDetailsDiv = document.getElementById('insuranceDetails');

    // Function to show/hide insurance details based on radio button selection
    function toggleInsuranceDetails() {
        if (insuranceYesRadio.checked) {
            insuranceDetailsDiv.classList.remove('hidden');
            // Optional: Make insurance fields required if 'Yes' is checked
            insuranceDetailsDiv.querySelectorAll('input').forEach(input => input.required = true);
        } else {
            insuranceDetailsDiv.classList.add('hidden');
            // Optional: Remove 'required' attribute if 'No' is checked
             insuranceDetailsDiv.querySelectorAll('input').forEach(input => {
                 input.required = false;
                 input.value = ''; // Clear values if hidden
             });
        }
    }

    // Add event listeners to the radio buttons
    if (insuranceYesRadio && insuranceNoRadio && insuranceDetailsDiv) {
        insuranceYesRadio.addEventListener('change', toggleInsuranceDetails);
        insuranceNoRadio.addEventListener('change', toggleInsuranceDetails);

        // Initial check in case the form is pre-filled or user navigates back
        toggleInsuranceDetails();
    }

    // Basic Form Validation Example (Client-side)
    const form = document.getElementById('appointmentForm');
    if (form) {
        form.addEventListener('submit', function(event) {
            // The browser's built-in 'required' attribute handling is usually sufficient
            // for basic checks. You can add more complex validation here if needed.
            if (!form.checkValidity()) {
                event.preventDefault(); // Stop submission if invalid
                // Optionally, you could add custom error messages or styles here
                alert('Please fill out all required fields correctly.');
            } else {
                // Optional: Show a 'submitting' state on the button
                const submitButton = form.querySelector('button[type="submit"]');
                if(submitButton) {
                    submitButton.disabled = true;
                    submitButton.textContent = 'Submitting...';
                }
                 // Form is valid and will proceed with submission (to the 'action' URL)
                 console.log('Form is valid, submitting...');
            }
        });
    }

});