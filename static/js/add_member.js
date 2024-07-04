document.addEventListener('DOMContentLoaded', function() {
    const nextButtons = document.querySelectorAll('.next');
    const prevButtons = document.querySelectorAll('.prev');
    const fieldsets = document.querySelectorAll('fieldset');
    const progressBar = document.querySelector('.progress-bar');
    const trainerRequired = document.getElementById('trainer_required');
    const trainerDurationGroup = document.getElementById('trainer_duration_group');
    const trainerFeeGroup = document.getElementById('trainer_fee_group');
    let currentStep = 0;

    function updateProgressBar() {
        const percentage = ((currentStep + 1) / fieldsets.length) * 100;
        progressBar.style.width = percentage + '%';
    }

    function showStep(step) {
        fieldsets.forEach((fieldset, index) => {
            if (index === step) {
                fieldset.classList.add('active');
                fieldset.classList.remove('d-none');
            } else {
                fieldset.classList.remove('active');
                fieldset.classList.add('d-none');
            }
        });
        updateProgressBar();
    }

    nextButtons.forEach(button => {
        button.addEventListener('click', () => {
            if (currentStep < fieldsets.length - 1) {
                currentStep++;
                showStep(currentStep);
            }
        });
    });

    prevButtons.forEach(button => {
        button.addEventListener('click', () => {
            if (currentStep > 0) {
                currentStep--;
                showStep(currentStep);
            }
        });
    });

    trainerRequired.addEventListener('change', function() {
        if (trainerRequired.value === 'yes') {
            trainerDurationGroup.style.display = 'block';
            trainerFeeGroup.style.display = 'block';
        } else {
            trainerDurationGroup.style.display = 'none';
            trainerFeeGroup.style.display = 'none';
        }
    });

    showStep(currentStep);
});