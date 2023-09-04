// Validar campos en tiempo real y mostrar tooltips
window.addEventListener('DOMContentLoaded', (event) => {
    var fields = document.querySelectorAll('.form-control');

    fields.forEach(function(field) {
        field.addEventListener('input', function() {
            if (!field.checkValidity()) {
                field.classList.remove('is-valid');
                field.classList.add('is-invalid');
                field.setAttribute('data-toggle', 'tooltip');
                field.setAttribute('data-placement', 'bottom');
                field.setAttribute('title', field.validationMessage);
                $(field).tooltip('show');
            } else {
                field.classList.remove('is-invalid');
                field.classList.add('is-valid');
                field.removeAttribute('data-toggle');
                field.removeAttribute('data-placement');
                field.removeAttribute('title');
                $(field).tooltip('hide');
            }
        });

        field.addEventListener('blur', function() {
            $(field).tooltip('hide');
        });
    });
});


const textarea = document.getElementById('habilidades');
const habilidadesHelp = document.getElementById('habilidades-help');

// Establece las viñetas iniciales en el textarea
const bulletPoints = ['• ', '• ', '• ', '• ', '• '];
textarea.value = bulletPoints.join('\n');

textarea.addEventListener('input', function() {
    const lines = this.value.split('\n');
    const newBulletPoints = [];

    for (let i = 0; i < 5; i++) {
        const line = lines[i] || '';
        newBulletPoints.push('• ' + line.substring(2));
    }

    if (lines.length > 5) {
        habilidadesHelp.innerText = '¡Máximo 5 habilidades permitidas!';
        textarea.setCustomValidity('Excedió el límite de habilidades');
    } else {
        habilidadesHelp.innerText = 'Ingrese hasta 5 habilidades separadas por líneas.';
        textarea.setCustomValidity('');
    }

    this.value = newBulletPoints.join('\n');
});







function validateAndNext(currentStepId, nextStepId) {
    var currentStep = document.getElementById(currentStepId);
    var nextStep = document.getElementById(nextStepId);
    
    var valid = true;

    // Verificar si todos los campos requeridos están validados
    currentStep.querySelectorAll('.form-control').forEach(function(input) {
        if (!input.checkValidity()) {
            valid = false;
            input.classList.add('is-invalid');
        } else {
            input.classList.remove('is-invalid');
        }
    });

    if (valid) {
        currentStep.classList.remove('active');
        nextStep.classList.add('active');
    } else {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Por favor, complete todos los campos requeridos antes de continuar.',
        });
    }
}

function nextStep(currentStepId, nextStepId) {
    document.getElementById(currentStepId).classList.remove('active');
    document.getElementById(nextStepId).classList.add('active');
}

function prevStep(currentStepId, prevStepId) {
    document.getElementById(currentStepId).classList.remove('active');
    document.getElementById(prevStepId).classList.add('active');
}

function mostrarVistaPrevia(input) {
    var vistaPrevia = document.getElementById('vista_previa');
    var defaultPreview = document.getElementById('default_preview');

    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            vistaPrevia.style.display = 'block';
            defaultPreview.style.display = 'none'; // Ocultar la imagen predeterminada
            vistaPrevia.src = e.target.result;
        };
        reader.readAsDataURL(input.files[0]);
    }
}



// Attach onsubmit event handler to the form
document.getElementById('multistep-form').addEventListener('submit', function (event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Perform form validation here
    if (this.checkValidity()) {
        this.submit(); // Submit the form if it's valid
    } else {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Por favor, complete todos los campos requeridos antes de enviar el formulario.',
        });
    }
});





document.addEventListener('DOMContentLoaded', (event) => {
    const fields = document.querySelectorAll('.form-control');

    fields.forEach(function(field) {
        field.addEventListener('input', function() {
            if (!field.checkValidity()) {
                field.classList.remove('is-valid');
                field.classList.add('is-invalid');
                field.setAttribute('data-toggle', 'tooltip');
                field.setAttribute('data-placement', 'bottom');
                field.setAttribute('title', field.validationMessage);
                $(field).tooltip('show');
            } else {
                field.classList.remove('is-invalid');
                field.classList.add('is-valid');
                field.removeAttribute('data-toggle');
                field.removeAttribute('data-placement');
                field.removeAttribute('title');
                $(field).tooltip('hide');
            }
        });

        field.addEventListener('blur', function() {
            $(field).tooltip('hide');
        });
    });
});


