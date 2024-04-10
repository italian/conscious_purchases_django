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

        let result_

        if (await addQuestion('Нужно ли вам это?')) {
            if (await addQuestion('Серьезно?')) {
                if (await addQuestion('Вам было нужно это вчера?')) {
                    if (await addQuestion('Можете ли вы это одолжить или арендовать?')) {
                        alert('Так и сделайте!');
                        result_ = 'Так и сделайте!';
                    } else {
                        if (await addQuestion('Вы хотите это хранить?')) {
                            alert('Покупайте (ищите качественное)');
                            result_ = 'Покупайте (ищите качественное)';
                        } else {
                            alert('Не покупайте');
                            result_ = 'Не покупайте';
                        }
                    }
                } else {
                    alert('Подождите 30 дней (или пока оно вам не понадобится)');
                    result_ = 'Подождите 30 дней (или пока оно вам не понадобится)';
                }
            } else {
                alert('Не покупайте');
                result_ = 'Не покупайте'; 
            }
        } else {
            alert('Не покупайте');
            result_ = 'Не покупайте';
        }

        const result = await fetch('/submit_checklist_result/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            },
            body: JSON.stringify({
                item: itemInput.value,
                result: result_,
            }),
        });
    
        if (result.ok) {
            const response = await result.json();
            if (response.success) {
                alert('Результат чек-листа успешно сохранен!');
            } else {
                alert('Ошибка при сохранении результата.');
            }
        } else {
            alert('Ошибка при отправке результата.');
        }
    });
});


async function addQuestion(questionText) {
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
