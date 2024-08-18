import gridModule from './modules/gridModule.js'
import menuModule from './modules/menuModule.js'

document.addEventListener('DOMContentLoaded', function () {
    gridModule.init(4);
    menuModule.init();
});
