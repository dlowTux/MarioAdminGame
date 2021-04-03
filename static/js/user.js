document.getElementById("formplayer").addEventListener("submit", function (e) {
    e.preventDefault();
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

            }
        });
});
