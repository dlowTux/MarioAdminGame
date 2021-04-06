document.getElementById("formulariotournament").addEventListener("submit", function (e) {
    e.preventDefault();
    const log = document.querySelector("#errors");
    log.innerHTML = " ";
    const name = document.getElementById("txtname").value;
    const type = document.getElementById("txttype").value;
    const jcadena = JSON.stringify({tournament: [name, type]});
    console.log(jcadena)
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
                    "Error that user is already in into a clan";
                label.classList.add("error");
                log.append(label);
            }
        });
});
