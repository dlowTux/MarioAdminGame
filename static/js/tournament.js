document
    .getElementById("formulariotournament")
    .addEventListener("submit", function (e) {
        e.preventDefault();
        const log = document.querySelector("#errors");
        log.innerHTML = " ";
        const name = document.getElementById("txtname").value;
        const type = document.getElementById("txttype").value;
        const jcadena = JSON.stringify({tournament: [name, type]});
        console.log(jcadena);
        var url = "/AddTournament";
        fetch(url, {
            method: "POST",
            body: jcadena,
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((resp) => resp.json())
            .then((data) => {
                //reload the page
                if (data["response"] == true) {
                    window.location.replace("http://localhost:5000/tournament");
                } else {
                    //adding the eror to le log
                    const label = document.createElement("label");
                    label.innerText =
                        "Error that tournament has the same name that other tournament";
                    label.classList.add("error");
                    log.append(label);
                }
            });
    });
document.getElementById("formsingler").addEventListener("submit", function (e) {
    e.preventDefault();
    const log = document.querySelector("#errors");
    log.innerHTML = " ";
    const id_tounament = document.getElementById("id_tournament").value;
    const id_player = document.getElementById("id_player").value;
    const jcadena = JSON.stringify({tournament: [id_tounament, id_player]});
    console.log(jcadena);
    var url = "/AddPlayerTournament";
    fetch(url, {
        method: "POST",
        body: jcadena,
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((resp) => resp.json())
        .then((data) => {
            //reload the page
            if (data["response"] == true) {

                window.location.replace("http://localhost:5000/tournament");
                console.log(data['response'][1])
            } else {
                //adding the eror to le log
                const label = document.createElement("label");
                label.innerText =
                    "Error the player was not added to the tournament try again";
                label.classList.add("error");
                log.append(label);
            }
        });
});
document.getElementById("formclans").addEventListener("submit", function (e) {
    e.preventDefault();
    const log = document.querySelector("#errors");
    log.innerHTML = " ";
    const id_tounament = document.getElementById("id_tournament_e").value;
    const id_player = document.getElementById("id_team").value;
    const jcadena = JSON.stringify({tournament: [id_tounament, id_player]});
    console.log(jcadena);
    var url = "/AddTeamTournament";
    fetch(url, {
        method: "POST",
        body: jcadena,
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((resp) => resp.json())
        .then((data) => {
            //reload the page
            if (data["response"] == true) {
                window.location.replace("http://localhost:5000/tournament");
            } else {
                //adding the eror to le log
                const label = document.createElement("label");
                label.innerText =
                    "Error the clan was not added to the tournament try again";
                label.classList.add("error");
                log.append(label);
            }
        });
});
/*document.getElementById("formspoints").addEventListener("submit", function (e) {
    e.preventDefault();
    const log = document.querySelector("#errors");
    log.innerHTML = " ";
    const id_tounament = document.getElementById("id_t").value;
    const id_player = document.getElementById("id_p").value;
    const jcadena = JSON.stringify({tournament: [id_tounament, id_player]});
    console.log(jcadena);
    var url = "/AddPonitsSeries";
    fetch(url, {
        method: "POST",
        body: jcadena,
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((resp) => resp.json())
        .then((data) => {
            //reload the page
            if (data["response"] == true) {
                window.location.replace("http://localhost:5000/tournament");
            } else {
                //adding the eror to le log
                const label = document.createElement("label");
                label.innerText =
                    "Error the was not added to the tournament try again";
                label.classList.add("error");
                log.append(label);
            }
        });
});*/
const btnDelete = document.querySelectorAll('.btn-delete');
if (btnDelete) {
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Are you sure you want to delete it?')) {
                e.preventDefault();
            }
        });
    })
}
