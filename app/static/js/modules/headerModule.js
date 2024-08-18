const headerModule = (function () {
    const header = document.querySelector('.header');
    let lastScrollY = 0;
    let ticking = false;

    function updateHeader() {
        const scrollY = window.scrollY;

        if (scrollY > lastScrollY) {
            // Hacia abajo
            header.classList.add('hidden');
        } else {
            // Hacia arriba
            header.classList.remove('hidden');
        }

        lastScrollY = scrollY <= 0 ? 0 : scrollY;
        ticking = false;
    }

    function onScroll() {
        if (!ticking) {
            window.requestAnimationFrame(updateHeader);
            ticking = true;
        }
    }

    function init() {
        window.addEventListener('scroll', onScroll);
    }

    return {
        init: init
    };
})();

export default headerModule;
