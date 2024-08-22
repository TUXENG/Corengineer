const typewriterModule = (function () {
    const text = "INNOVATION";
    const speed = 100;
    let index = 0;

    function typeWriter() {
        const typeWriterElement = document.querySelector('welcome__slogan-span');
        if (index < text.length) {
            typeWriterElement.textContent += text.charAt(index);
            index++;
            setTimeout(typeWriter, speed);
        }
    }

    function init() {
        typeWriter();
    }

    return {
        init: init
    }; 
})();

export default typewriterModule;