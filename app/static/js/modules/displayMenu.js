const displayMenu = (function () {

    const buttonMenu = document.querySelector('.header__nav-checkbox-menu');
    const navList = document.querySelector('.header__nav-list'); // Corregido selector

    function showMenu() {
        navList.style.display = 'flex'; // Cambia display a block
        navList.classList.add('show'); // Asegúrate de añadir la clase 'show' para cualquier estilo adicional
    }

    function hideMenu() {
        navList.classList.remove('show'); // Elimina la clase 'show'
        setTimeout(() => {
            navList.style.display = 'none'; // Cambia display a none después de un tiempo
        }, 300);
    }

    function toggleDisplayMenu() {
        if (navList.classList.contains('show')) {
            hideMenu();
        } else {
            showMenu();
        }
    }

    function init() {
        buttonMenu.addEventListener('change', () => {
            if (buttonMenu.checked) {
                showMenu();
            } else {
                hideMenu();
            }
        });
    }

    return {
        init: init
    };

})();

export default displayMenu;