
// DOM Events
document
    .getElementById("form")
    .addEventListener("submit", function (e) {
        // Override the default Form behaviour
        e.preventDefault();
        const user = document.getElementById('txtuser').value,
            password = document.getElementById('txtpass').value;
        const cadena = {'data': [user, password]}
        const jcadena = JSON.stringify(cadena)
        var url = '/login';
        fetch(url, {
            method: 'POST',
            body: jcadena,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json()).then(data => {
            console.log(data)
        })
    });
