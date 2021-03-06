
function GenerateTd(data) {
    return `<td>${data[1]}</td>
            <td>
                <a href="/DeletePlayer/${data[0]}" class="btn btn-delete" >
                    <img src="static/img/delete2.png" />
                </a>
            </td>
            <td>
                <a
                   href='/UpdatePlayer/${data[0]}' 
                >
                    <img src="static/img/updated.png" />
                </a>
            </td>
                     `;
}
function GenerateTable() {
    const table = document.getElementById("table-players");
    table.innerHTML = "";
    /* Peticion Get to get all the player*/
    var url = "/GetAllPlayers";
    fetch(url, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((resp) => resp.json())
        .then((data) => {
            if (data["response"] != false) {
                //creando los elementos

                for (var i in data["response"]) {
                    var tr = document.createElement("tr");
                    tr.innerHTML = GenerateTd(data['response'][i]);
                    table.append(tr);
                }
            } else {
                //adding the eror to le log
                const label = document.createElement("label");
                label.innerText = "Error was not possible to get the players";
                label.classList.add("error");
                log.append(label);
            }
        });
}
document.getElementById("form-search").addEventListener("submit", function (e) {
    e.preventDefault();
    const log = document.querySelector("#errors");
    log.innerHTML = " ";
    const text = document.getElementById("textbuscar").value;
    var url = "/Player/" + text;
    fetch(url, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((resp) => resp.json())
        .then((data) => {
            //reload the page
            const table = document.getElementById("table-players");
            table.innerHTML = "";
            for (var i in data["response"]) {
                var tr = document.createElement("tr");
                tr.innerHTML = GenerateTd(data["response"][i]);
                table.append(tr);
            }

        });
});

document.getElementById("formplayer").addEventListener("submit", function (e) {
    e.preventDefault();
    const log = document.querySelector("#errors");
    log.innerHTML = " ";
    const text = document.getElementById("txtusername").value;
    const jcadena = JSON.stringify({username: [text]});
    var url = "/RegisterUser";
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
                // try to just add the last element insert
                var la = document.createElement("label");
                la.innerText = "Player was added successfully";
                la.classList.add("notices");
                log.append(la);
                GenerateTable();
                document.getElementById("formplayer").reset();
            } else {
                //adding the eror to le log
                const label = document.createElement("label");
                label.innerText =
                    "Error was not possible to register a new player";
                label.classList.add("error");
                log.append(label);
            }
        });
});



