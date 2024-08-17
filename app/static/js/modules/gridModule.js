const gridModule = (function () {
    
    const items = document.querySelectorAll('.card');

    function showItems(maxItems) {
        items.forEach((item, index) => {
            if (index < maxItems) { 
                item.classList.add('visible');
            }
        });
        
    }

    function init(maxItems = 4) {
        showItems(maxItems);
        console.log('Hay ${items.length} para mostrar');
    }

    return {
        init: init
    };
})();

export default gridModule;


