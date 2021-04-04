document.getElementById("formUpdate").addEventListener("submit", function (e) {
    e.preventDefault();
    const log = document.querySelector("#errors");
    log.innerHTML = " ";
    const text = document.getElementById("txtUser").value;
    const jcadena = JSON.stringify({username: [text]});
    var url = "/UpdatePlayer/" + document.getElementById('txtid').value;
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
