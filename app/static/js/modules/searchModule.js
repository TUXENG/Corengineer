const searchModule = (function() {

    const searchIcon = document.querySelector('.header__search-ico');
    const searchField = document.querySelector('.header__search-textfield');

    function showSearchField() {
        searchField.style.display = 'inline-block'; 
        setTimeout(() => {
            searchField.classList.add('show');
        }, 0); 
        searchField.focus();
        searchIcon.style.opacity = '1';
    }


    function hideSearchField() {
        searchField.classList.remove('show');
        setTimeout(() => {
            searchField.style.display = 'none';
        }, 300);
        searchIcon.style.opacity = '0.6';
    }

    
    function toggleSearchField() {
        if (searchField.classList.contains('show')) {
            hideSearchField();
        } else {
            showSearchField();
        }
    }


    function init() {
        searchIcon.addEventListener('click', toggleSearchField);
    }


    return {
        init: init
    };
})();


export default searchModule;
