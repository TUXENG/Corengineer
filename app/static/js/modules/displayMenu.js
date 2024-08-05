const displayMenu = (function () {

    const buttonMenu = document.querySelector('.header__nav-checkbox-menu');
    const nav = document.querySelector('.header__nav'); 
    const navList = document.querySelector('.header__nav-list');

    function showMenu() {
        setTimeout(() => {
            nav.style.display = 'flex';
            nav.style.opacity = '1';
            nav.style.width = '100%'
            nav.classList.add('show');
            navList.style.display = 'flex';
            navList.style.opacity = '1';
        }, 100);
    }

    function hideMenu() {
        nav.classList.remove('show'); 
        setTimeout(() => {
            nav.style.display = 'none'; 
            nav.style.opacity = '0';
            nav.style.width = '0%'
            navList.style.display = 'none';
            navList.style.opacity = '0';
        }, 180);
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