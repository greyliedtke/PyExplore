
function encode() {
    const input = document.getElementById("input").value.toUpperCase();
    const output = document.getElementById("output");
    const encodedMessage = enigmaEncoder(input);
    output.value = encodedMessage;
}

function enigmaEncoder(message) {
    const rotor = createRotor();
    let encodedMessage = "";
    for (let i = 0; i < message.length; i++) {
        const letter = message[i];
        const encodedLetter = encodeLetter(letter, rotor);
        encodedMessage += encodedLetter;
    }
    return encodedMessage;
}

function createRotor() {
    const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
    const rotor = alphabet.slice();
    for (let i = 0; i < rotor.length; i++) {
        const randomIndex = Math.floor(Math.random() * rotor.length);
        const temp = rotor[i];
        rotor[i] = rotor[randomIndex];
        rotor[randomIndex] = temp;
    }
    return rotor;
}

function encodeLetter(letter, rotor) {
    const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const index = alphabet.indexOf(letter);
    return rotor[index];
}