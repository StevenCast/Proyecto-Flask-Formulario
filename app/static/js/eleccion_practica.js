document.addEventListener('DOMContentLoaded', function() {
    const servicioComunitarioRadio = document.getElementById('Sevicio_comunitario');
    const laboralesRadio = document.getElementById('Laborales');

    // Agregar evento 'change' a los radios
    servicioComunitarioRadio.addEventListener('change', function() {
        if (servicioComunitarioRadio.checked) {
            agregarElementosServicioComunitario();
        }
    });

    laboralesRadio.addEventListener('change', function() {
        if (laboralesRadio.checked) {
            agregarElementosLaborales();
        }
    });

    function agregarElementosServicioComunitario() {
        // Limpiar opciones anteriores si existen
        limpiarOpciones();

        // Crear elementos y agregarlos al formulario
        const select = document.createElement('select');
        select.name = 'comunitarias';
        const opciones = ['Escoja una opcion', 'Actividades solidarias y de cooperación', 'Participación en juntas receptoras del voto'];
        opciones.forEach(opcion => {
            const option = document.createElement('option');
            option.textContent = opcion;
            select.appendChild(option);
        });
        const label = document.createElement('label');
        label.classList.add('datos_formulario');
        label.textContent = 'Servicio Comunitario';
        label.appendChild(select);
        const fieldset = document.querySelector('fieldset:nth-of-type(1)');
        fieldset.appendChild(label);
    }

    function agregarElementosLaborales() {
        // Limpiar opciones anteriores si existen
        limpiarOpciones();

        // Crear elementos y agregarlos al formulario
        const select = document.createElement('select');
        select.name = 'laborales';
        const opciones = ['Escoja una opcion', 'Participacion Estudiantil en Actividades Académicas, de Gestión, de Investigación y de Colaboración en Eventos Académicos', 'Representacion Estudiantil', 'Estudiantes mentores', 'Actividades Deportivas planificadas por la Institución', 'Experiencia Laboral', 'Dirección de ramas de organizaciones estudiantiles académicas', 'Representación de la Institución en competencias académicas', 'Clubes, Coro y Grupo de Cámara', 'Representación de la Institución en competencias deportivas', 'Participación en la dirección de asociaciones de estudiantes'];
        opciones.forEach(opcion => {
            const option = document.createElement('option');
            option.textContent = opcion;
            select.appendChild(option);
        });
        const label = document.createElement('label');
        label.classList.add('datos_formulario');
        label.textContent = 'Laborales';
        label.appendChild(select);
        const fieldset = document.querySelector('fieldset:nth-of-type(1)');
        fieldset.appendChild(label);
    }

    function limpiarOpciones() {
        const fieldset = document.querySelector('fieldset:nth-of-type(1)');
        const labels = fieldset.querySelectorAll('.datos_formulario');
        labels.forEach(label => {
            if (label.querySelector('select')) {
                fieldset.removeChild(label);
            }
        });
    }
});


