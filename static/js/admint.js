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
