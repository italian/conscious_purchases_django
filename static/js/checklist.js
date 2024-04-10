document.addEventListener('DOMContentLoaded', async function() {
    const buttonChecklistForm = document.getElementById('button_checklistForm');
    const itemInput = document.getElementById('item');

    buttonChecklistForm.addEventListener('click', async function(event) {
        event.preventDefault();

        if (itemInput.value.trim() === '') {
            alert('Пожалуйста, введите название покупки.');
            return;
        }

        buttonChecklistForm.style.display = 'none';

        if (await addQuestion('Нужно ли вам это?')) {
            if (await addQuestion('Серьезно?')) {
                if (await addQuestion('Вам было нужно это вчера?')) {
                    if (await addQuestion('Можете ли вы это одолжить или арендовать?')) {
                        alert('Так и сделайте!');
                    } else {
                        if (await addQuestion('Вы хотите это хранить?')) {
                            alert('Покупайте (ищите качественное)');
                        } else {
                            alert('Не покупайте');
                        }
                    }
                } else {
                    alert('Подождите 30 дней (или пока оно вам не понадобится)');
                }
            } else {
                alert('Не покупайте');
            }
        } else {
            alert('Не покупайте');
        }
    });
});


function addQuestion(questionText) {
    return new Promise((resolve, reject) => {
        const questionsDiv = document.getElementById('questions');
        const questionDiv = document.createElement('div');
        questionDiv.innerHTML = `
            <p>${questionText}</p>
            <button class="yesButton">Да</button>
            <button class="noButton">Нет</button>
        `;
        questionsDiv.appendChild(questionDiv);

        const yesButton = questionDiv.querySelector('.yesButton');
        yesButton.addEventListener('click', function(event) {
            event.preventDefault();
            yesButton.disabled = true;
            noButton.disabled = true;
            resolve(true);
        });

        const noButton = questionDiv.querySelector('.noButton');
        noButton.addEventListener('click', function(event) {
            event.preventDefault();
            yesButton.disabled = true;
            noButton.disabled = true;
            resolve(false);
        });
    });
}
