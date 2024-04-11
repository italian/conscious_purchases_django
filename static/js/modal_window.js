var modal = document.getElementById("errorModal");
// var span = document.getElementsByClassName("close")[0];

// При открытии модального окна
function openModal() {
    modal.style.display = "block";
}

// При закрытии модального окна
function closeModal() {
    modal.style.display = "none";
}

// При нажатии на <span> (x), закрываем модальное окно
// span.onclick = function() {
//     closeModal();
// }

// При нажатии в любом месте за пределами модального окна, закрываем его
window.onclick = function(event) {
 if (event.target == modal) {
        closeModal();
    }
}