function createGame() {


    let data = {
        actie: 'toevoegen'
    };

    fetch('cgi-bin/createGame.cgi?data=' + JSON.stringify(data))
        .then(response => response.json())
        .then(data => {
            console.log(data);

            for (let i = 0; i < 25; i++) {
                let woord = data["board"][i][0]
                let kleur = data["board"][i][1]

                // change colors to a nicer color
                if (kleur === 'red') {
                    kleur = '#ff7675'
                } else if (kleur === 'blue') {
                    kleur = '#74b9ff'
                }

                document.getElementById('playboard').innerHTML += '<div class="playcart omgedraaid" style="background-color:' + kleur + '"><p class="playcartword">' + woord + '</p></div>'

            }

            // update the stats text
            document.getElementById("curplayer").innerHTML = "Current Player: " + data['current_color'].toUpperCase();
            document.getElementById("gamecode").innerHTML = "Share this code: " + data['gamecode']

        });
}



// when you click on the button "CREATE NEW GAME", create a new game
$(function () {
    $('#createGame').click(function () {
        createGame();
    })
})



$(function(){
    $('#connectbutton').click(function(){
        console.log("Ik connecteerd nu met een bestaand spel")
    })
})

function connectToGame(gamecode){
    let data = {
        actie: 'connectgame'
    }
    fetch('cgi-bin/connectgame.cgi?data=' + JSON.stringify(data))
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
}



//Toggle spymaster when the user clicks to checkbox (we need to remove every "omgedraaid" class from all the playcarts)
function toggleSpyMaster() {
    const checkbox = document.getElementById("togglespy")
    const tiles = document.getElementsByClassName('playcart')
    if (checkbox.checked) {
        $(tiles).removeClass("omgedraaid")
    } else {
        $(tiles).addClass("omgedraaid")
    }
}

