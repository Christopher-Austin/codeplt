function deafGrandma() {
    let goodbyeCount = 1;
    while (true) {
        let response = prompt("What to say to grandma. ")
        if (!response) {
            console.log("WHAT?!")
        }
        else if (response[0] === response[0].toLowerCase()) {
            console.log("SPEAK UP KID!")
        }
        else if (response === "GOODBYE!" && goodbyeCount < 1) {
            console.log("LEAVING SO SOON?")
            goodbyeCount++;
        }
        else if (response === "GOODBYE!" && goodbyeCount === 1) {
            console.log("LATER, SKATER!")
            break;
        }
        else if (response[0] === response[0].toUpperCase()) {
            console.log("NO, NOT SINCE 1946!")
        }   
    }
}

deafGrandma();
