const typewriterModule = (function () {
    const textArray = [
        { text: "WEB", textColor: "#757575", bgColor: "#ff5722" },
        { text: "MOBILE", textColor: "#757575", bgColor: "#f00000" },
        { text: "ELECTRONIC", textColor: "#ffffff", bgColor: "#00838f" },
        { text: "ROBOTIC", textColor: "#ffffff", bgColor: "#e91e63" },
        { text: "INNOVATION", textColor: "#75757500", bgColor: "#9fef00" }
    ];
    const typingSpeed = 120;
    const erasingSpeed = 100;
    const newTextDelay = 2000;
    let typingElement = null;
    let textArrayIndex = 0;
    let charIndex = 0;

    function applyStyles() {
        typingElement.style.color = textArray[textArrayIndex].bgColor;
        typingElement.style.backgroundColor = textArray[textArrayIndex].textColor;
    }

    function type() {
        if (charIndex < textArray[textArrayIndex].text.length) {
            typingElement.textContent += textArray[textArrayIndex].text.charAt(charIndex);
            charIndex++;
            setTimeout(type, typingSpeed);
        } else {
            if (textArrayIndex < textArray.length - 1) {
                setTimeout(erase, newTextDelay);
            }
        }
    }

    function erase() {
        if (charIndex > 0) {
            typingElement.textContent = textArray[textArrayIndex].text.substring(0, charIndex - 1);
            charIndex--;
            setTimeout(erase, erasingSpeed);
        } else {
            textArrayIndex++;
            applyStyles();
            setTimeout(type, typingSpeed + 1100);
        }
    }

    function init() {
        typingElement = document.querySelector(".welcome__slogan-spam-typing");
        if (typingElement) {
            applyStyles(); // Aplica los estilos al iniciar
            setTimeout(type, newTextDelay);
        }
    }

    return {
        init: init
    };
})();

export default typewriterModule;
