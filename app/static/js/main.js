import searchModule from './modules/searchModule.js';
import gridModule from './modules/gridModule.js'

document.addEventListener('DOMContentLoaded', function () {
    searchModule.init();
    gridModule.init(4);
});
