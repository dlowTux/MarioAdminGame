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
            console.log('Diferentes')
        }
    });
