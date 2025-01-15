// Funcionalidades personalizadas para la documentación

document.addEventListener('DOMContentLoaded', function() {
    // Mejora en los enlaces externos
    document.querySelectorAll('a[href^="http"]').forEach(function(link) {
        if (!link.hasAttribute('target')) {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }
    });

    // Mejora en las tablas
    document.querySelectorAll('table.docutils').forEach(function(table) {
        table.classList.add('responsive');
        if (!table.hasAttribute('border')) {
            table.setAttribute('border', '1');
        }
    });

    // Mejora en la navegación
    var currentPath = window.location.pathname;
    document.querySelectorAll('.wy-menu-vertical li a').forEach(function(link) {
        if (link.getAttribute('href') && currentPath.includes(link.getAttribute('href'))) {
            link.parentElement.classList.add('current');
        }
    });

    // Función para copiar bloques de código
    document.querySelectorAll('.highlight').forEach(function(block) {
        var button = document.createElement('button');
        button.className = 'copy-button';
        button.textContent = 'Copiar';
        
        button.addEventListener('click', function() {
            var code = block.querySelector('pre').textContent;
            navigator.clipboard.writeText(code).then(function() {
                button.textContent = '¡Copiado!';
                setTimeout(function() {
                    button.textContent = 'Copiar';
                }, 2000);
            });
        });

        block.insertBefore(button, block.firstChild);
    });
}); 