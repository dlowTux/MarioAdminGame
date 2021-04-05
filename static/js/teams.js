const btnDelete = document.querySelectorAll(".btn-delete");
if (btnDelete) {
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener("click", (e) => {
            if (!confirm("Are you sure you want to delete it?")) {
                e.preventDefault();
            }
        });
    });
}
document.getElementById("formteams").addEventListener("submit", function (e) {
    e.preventDefault();
    const log = document.querySelector("#errors");
    log.innerHTML = " ";
    const text = document.getElementById("txtteams").value;
    const text1 = document.getElementById("txtuser").value;

    const jcadena = JSON.stringify({username: [text, text1]});
    console.log(jcadena)
    var url = "/AddTeam";
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
                window.location.replace("http://localhost:5000/teams");
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
