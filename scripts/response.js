function getBotResponse(input) {
    //rock paper scissors
    if (input == "rock") {
        return "paper";
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else if(input == "Heart clicked!") {
        return "Thank You!";
    } else if(input == "who are you") {
        return "I'm Mohammed, Here to help you with anything.";
    } else if(input == "how old are you") {
        return "I dont have a specific age, I'm just a bot but i was made on 2nd of july by Mohammed";
    } else {
        return "Try asking something else!";
    }
}
