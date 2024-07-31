document.addEventListener('DOMContentLoaded', function () {
    const searchIcon = document.querySelector('.header__search-ico');
    const searchField = document.querySelector('.header__search-textfield');

    searchIcon.addEventListener('click', function () {
        // Toggle visibility of the search field
        if (searchField.style.display === 'block') {
            searchField.style.display = 'none';
            searchField.style.opacity = '0';
        } else {
            searchField.style.display = 'block';
            searchField.style.opacity = '1';
            searchField.focus();
        }
    });
});
