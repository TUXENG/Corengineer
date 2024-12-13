const menuModule = (function () {
    const checkbox = document.getElementById('menu-bars');
    const menuIcon = document.getElementById('menu-icon');

    function updateMenuIcon() {
        if (checkbox.checked) {
            menuIcon.classList.remove('fa-bars');
            menuIcon.classList.add('fa-xmark');
        } else {
            menuIcon.classList.remove('fa-xmark');
            menuIcon.classList.add('fa-bars');
        }
    }
    
    function init() {
        updateMenuIcon();
        checkbox.addEventListener('change', updateMenuIcon);
    }

    return {
        init: init
    };
})();

export default menuModule;