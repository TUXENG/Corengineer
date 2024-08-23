import gridModule from './modules/gridModule.js'
import menuModule from './modules/menuModule.js'
import headerModule from './modules/headerModule.js'
import typewriterModule from './modules/typewriterModule.js';

document.addEventListener('DOMContentLoaded', function () {
    gridModule.init(4);
    menuModule.init();
    headerModule.init();
    typewriterModule.init();
});
