$(document).ready(function () {
    $('.stats').hide()
});


// CREATE A NEW GAME
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

            // add an eventlistener on every tile
            let tegels = document.getElementsByClassName("playcart");
            Array.from(tegels).forEach(function (tegel) {
                tegel.addEventListener('click', clickontile);
            });



            // update the stats text
            document.getElementById("curplayer").innerHTML = "Current Player: " + data['current_color'].toUpperCase();
            document.getElementById("gamecode").innerHTML = "Share this code: " + data['gamecode']

        });
}


// when you click on the button "CREATE NEW GAME", create a new game
$(function () {
    $('.createGame').click(function () {
        $(this).fadeOut();
        $('.stats').show();
        $('#startuptext').hide();
        createGame();
    })
})











// CONNECT TO AN EXISTING GAME
function connectToGame() {

    // get the gamecode from the input field
    let gamecode = document.getElementById("inputgamecode").value
    console.log(gamecode)

    let data = {
        actie: 'connectgame',
        gameID: gamecode
    };
    fetch('cgi-bin/connectgame.cgi?data=' + JSON.stringify(data))
        .then(response => response.json())
        .then(data => {
            console.log(data);

            // print error message if the gamecode can not be
            if (data['gameinfo'] === 'Invalid Gamecode!') {
                alert("This gamekey does not exists!")
            } else {

                for (let i = 0; i < 25; i++) {
                    let woord = data["gameinfo"][i][0]
                    let kleur = data["gameinfo"][i][1]

                    // change colors to a nicer color
                    if (kleur === 'red') {
                        kleur = '#ff7675'
                    } else if (kleur === 'blue') {
                        kleur = '#74b9ff'
                    }

                    document.getElementById('playboard').innerHTML += '<div class="playcart omgedraaid" style="background-color:' + kleur + '"><p class="playcartword">' + woord + '</p></div>'

                }

                // add an eventlistener on every tile
                let tegels = document.getElementsByClassName("playcart");
                Array.from(tegels).forEach(function (tegel) {
                    tegel.addEventListener('click', clickontile);
                });
            }


            // update the stats text
            document.getElementById("gamecode").innerHTML = "Share this code: " + data['gamecode']
        })
}

$(function () {
    $('#connectbutton').click(function () {
        console.log("Ik connecteer nu met een bestaand spel")
        $('.stats').show();
        $('#startuptext').hide();
        connectToGame()
    })
})





// CLICK ON A TILE
function clickontile() {


    if (!(spymasterEnabled())) {
        console.log("De tegel wordt omgedraaid!")
        clickedword = $(this).text()
        gamecode = $("#gamecode").text();

        let data = {
            actie: 'fliptile',
            gameID: gamecode,
            woord: clickedword
        }

        fetch('cgi-bin/fliptile.cgi?data=' + JSON.stringify(data))
            .then(response => response.json())
            .then(data => console.log(data));


        console.log($(this).removeClass("omgedraaid"))

        // The spymaster can not flip a tile!
    } else {
        alert("Stop cheating spymaster! A spymaster can not flip tiles!")
    }


}







// UPDATE GAME TILES
setInterval(updategametiles, 1000);


function updategametiles() {

    let gamecode = $("#gamecode").text()

    let data = {
        actie: 'refresh',
        gameID: gamecode
    };

    fetch('cgi-bin/updategame.cgi?data=' + JSON.stringify(data))
        .then(response => response.json())
        .then(data => {
            console.log(data);


            let tiles = document.getElementsByClassName('playcart')

            // print error message if the gamecode can not be
            for (let i = 0; i < 25; i++) {

                let woord = data["updateddata"]['board'][i][0]
                let kleur = data["updateddata"]['board'][i][1]
                let omgedraaid = data["updateddata"]['board'][i][2]

                // change colors to a nicer color
                if (kleur === 'red') {
                    kleur = '#ff7675'
                } else if (kleur === 'blue') {
                    kleur = '#74b9ff'
                }

                if (omgedraaid === true) {
                    $(tiles[i]).removeClass("omgedraaid")
                }

            }

            document.getElementById("curplayer").innerHTML = "Current Player: " + data['updateddata']['current_color'].toUpperCase();
            document.getElementById("remainingred").innerHTML = data['updateddata']["resterende_tegels_red"]
            document.getElementById("remainingblue").innerHTML = data['updateddata']["resterende_tegels_blue"]

            // CHECK WINNING CONDITIONS
            if (data['updateddata']["resterende_tegels_blue"] == 0) {
                alert("Team BLUE wins!")
                location.reload()
            } else if (data['updateddata']["resterende_tegels_red"] == 0) {
                alert("Team RED wins!")
                location.reload()
            }

            if (data['updateddata']["winner"] !== null) {
                alert("Team " + data['updateddata']["winner"] + " wins!");
                location.reload()
            }
        })
}





// END TURN BUTTON
$(function () {
    $('#endturnbutton').click(function () {
        console.log("Switching teams")
        endTurn();
    })
})


function endTurn() {

    let gamecode = $("#gamecode").text()

    let data = {
        actie: 'endturn',
        gameID: gamecode
    }

    fetch('cgi-bin/switchteam.cgi?data=' + JSON.stringify(data))
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })



}


function spymasterEnabled() {
    const checkbox = document.getElementById("togglespy")
    return checkbox.checked;
}








$(function(){
    $('#refreshbutton').click(function(){
        refreshTiles()
    })
})

//REFRESH THE GAME TILES
function refreshTiles(){
    gamecode = $("#gamecode").text();
    console.log("De tegels worden geupdate!")


    let data = {
        actie: 'refresh',
        gameID: gamecode
    };

    fetch('cgi-bin/refreshgame.cgi?data=' + JSON.stringify(data))
        .then(response => response.json())
        .then(data => console.log(data));

        for (let i = 0; i < 25; i++) {
            let woord = data["gameinfo"][i][0]
            let kleur = data["gameinfo"][i][1]

            // change colors to a nicer color
            if (kleur === 'red') {
                kleur = '#ff7675'
            } else if (kleur === 'blue') {
                kleur = '#74b9ff'
            }

            document.getElementById('playboard').innerHTML += '<div class="playcart omgedraaid" style="background-color:' + kleur + '"><p class="playcartword">' + woord + '</p></div>'

            
        }

        // add an eventlistener on every tile
        let tegels = document.getElementsByClassName("playcart");
        Array.from(tegels).forEach(function(tegel){
            tegel.addEventListener('click', clickontile);
        });
        
        

        // update the stats text
        // document.getElementById("curplayer").innerHTML = "Current Player: " + data['current_color'].toUpperCase();
        // document.getElementById("gamecode").innerHTML = "Share this code: " + data['gamecode']
            // console.log(data["gamedata"][i])
            // let woord = data["gamedata"][i]
            // console.log(woord);
            
            // if(data["gamedata"][i][2] === True){
            //     document.getElementById('playboard').innerHTML += '<div class="playcart" style="background-color:' + kleur + '"><p class="playcartword">' + woord + '</p></div>'
            // }else{
            //     document.getElementById('playboard').innerHTML += '<div class="playcart omgedraaid" style="background-color:' + kleur + '"><p class="playcartword">' + woord + '</p></div>'
            // }

    


    // $(tegels).each(function(){
    //     if($(this).hasClass("omgedraaid")){
    //         console.log($(this).text())
    //         $(this).removeClass("omgedraaid")
    //     }
    // })

}



//Toggle spymaster when the user clicks to checkbox (we need to remove every "omgedraaid" class from all the playcarts)
function toggleSpyMaster() {
    const checkbox = document.getElementById("togglespy");
    const tiles = document.getElementsByClassName('playcart');

    if (checkbox.checked) {
        $(tiles).removeClass("omgedraaid");
        var refreshcolors = setInterval(updateSpymasterColors, 1000)
    } else {
        console.log("CLEAR INTERVAL")
        clearInterval(refreshcolors);
        $(tiles).addClass("omgedraaid")
        $(tiles).fadeTo("slow", 1);
    }


}

function updateSpymasterColors() {

    const checkbox = document.getElementById("togglespy")
    const tiles = document.getElementsByClassName('playcart')

    let gamecode = $("#gamecode").text()

    let data = {
        actie: 'getselectedcolors',
        gameID: gamecode
    }


    fetch('cgi-bin/spymastercolors.cgi?data=' + JSON.stringify(data))
        .then(response => response.json())
        .then(data => {
            console.log(data)

            if (checkbox.checked){
                $(tiles).removeClass("omgedraaid")

                console.log(data['selectedColors'])
                for (let i = 0; i < data['selectedColors'].length; i++) {
                    if (data['selectedColors'][i] === false) {
                        $(tiles[i]).fadeTo("slow", 0.25);
                    } else {
                        $(tiles[i]).fadeTo("slow", 1);
                    }
                }
            }
        })
}
