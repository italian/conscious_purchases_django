var modal = document.getElementById("errorModal");

// При открытии модального окна
function openModal() {
    modal.style.display = "block";
}

// При закрытии модального окна
function closeModal() {
    modal.style.display = "none";
}

// При нажатии в любом месте за пределами модального окна, закрываем его
window.onclick = function(event) {
    if (event.target == modal) {
        closeModal();
    }
}

// Добавляем обработчик событий click к модальному окну
modal.onclick = function() {
    closeModal();
}