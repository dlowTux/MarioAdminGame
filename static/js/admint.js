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
const btnstart = document.querySelectorAll('.start');
if (btnstart) {
    const btnArray = Array.from(btnstart);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Are you sure you want to start it?')) {
                e.preventDefault();
            }
        });
    })
}
document
    .getElementById("formclash")
    .addEventListener("submit", function (e) {
        e.preventDefault();
        const log = document.querySelector("#errors");
        log.innerHTML = " ";
        const team1 = document.getElementById("txtteam1").value;
        const score1 = document.getElementById("txtscore1").value;
        const team2 = document.getElementById("txtteam2").value;
        const score2 = document.getElementById("txtscore2").value;
        if (team1 == team2) {
            const label = document.createElement("label");
            label.innerText =
                "Error you can not select the same teams";
            label.classList.add("error");
            log.append(label);
        } else {
            var url = '/RegisterClashTournament'
            if (score1 >= 0 && score2 >= 0) {
                /* Promesa */
                const jcadena = JSON.stringify(
                    {
                        tournament:
                            [id_tounament, id_player]
                    }
                );
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
            } else {
                const label = document.createElement("label");
                label.innerText =
                    "Error you can not put a negative score";
                label.classList.add("error");
                log.append(label);
            }

        }
    });
