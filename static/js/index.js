// DOM Events
document.getElementById("form").addEventListener("submit", function (e) {
    // Override the default Form behaviour
    e.preventDefault();
    const log = document.querySelector("#errors");
    log.innerHTML = " ";

    const user = document.getElementById("txtuser").value,
        password = document.getElementById("txtpass").value;
    const cadena = {data: [user, password]};
    const jcadena = JSON.stringify(cadena);
    var url = "/login";
    fetch(url, {
        method: "POST",
        body: jcadena,
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((resp) => resp.json())
        .then((data) => {
            if (data["response"] == true) {
                //redirect to the home page
                window.location.replace("http://localhost:5000/home");
            } else {
                //add an span in the html to indicate that the password or user
                //was not correct

                const label = document.createElement("label");
                label.innerText = "Username or password was not correct";
                label.classList.add("error");
                log.append(label);
            }
        });
});
