document.addEventListener('DOMContentLoaded', function () {
    const searchIcon = document.querySelector('.header__search-ico');
    const searchField = document.querySelector('.header__search-textfield');
    
    
    searchIcon.addEventListener('click', function () {
        // Toggle visibility of the search field
        if (searchField.classList.contains('show')) {
                searchField.classList.remove('show');
                searchIcon.style.opacity = '1';
            } else {
                searchField.classList.add('show');
                searchIcon.style.opacity = '0.7';
                searchField.focus();
            }
    });
});

