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
                window.location.replace("http://localhost:5000/players");
            }
            else {
                //adding the eror to le log
                const label = document.createElement("label");
                label.innerText = "Error was not possible to register a new player";
                label.classList.add("error");
                log.append(label);
            }
        });
});
