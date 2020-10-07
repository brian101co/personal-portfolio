const conversations = document.querySelectorAll('.conversation');
const inbox = document.querySelector('.inbox');
const submitForm = document.querySelector('.message-form');

// Dashboard State
let id;

function getData(url) {
    return fetch(url)
        .then(function (response) {
            return response.json();
        });
}

function sendMessage(url, obj, token) {
    return fetch(url, {
        method: 'POST',
        body: JSON.stringify(obj),
        headers: {
            "Content-Type": "application/json; charset=UTF-8",
            "X-CSRFToken": token,
        }
    }).then(function (response) {
        return response.json();
    })
}

conversations.forEach(function (conversation) {
    conversation.addEventListener('click', function (event) {
        const convoElement = event.target.parentElement;
        id = convoElement.querySelector('input').value;
        const url = window.location + 'api/messages/' + id + '/';
        getData(url)
            .then(function (data) {
                inbox.innerHTML = '';
                const parsed_data = JSON.parse(data);
                for (const message of parsed_data) {
                    let split_date = message.fields.sent_at.split('T');
                    let date = new Date(split_date[0]);
                    let time = split_date[1].slice(0, 8);

                    if (message.fields.sender == id) {
                        inbox.innerHTML += `<p class="card-text p-3 reciever">
                                                ${message.fields.content}
                                                <small class="d-block mt-2">${date.toDateString()}</small>
                                            </p>`;
                    } else {
                        inbox.innerHTML += `<p class=" message p-3">
                                                ${message.fields.content}
                                                <small class="d-block mt-2">${date.toDateString()}</small>
                                            </p>`;
                    }
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    });
});

submitForm.addEventListener('click', function (event) {
    event.preventDefault();

    if (event.target.classList.contains('btn')) {
        const url = window.location + 'api/messages/';
        const message = {
            recipient: submitForm.querySelector('select[name="recipient"]').value,
            content: submitForm.querySelector('textarea[name="content"]').value,
        };
        csrfmiddlewaretoken = submitForm.querySelector('input[name="csrfmiddlewaretoken"]').value;
        sendMessage(url, message, csrfmiddlewaretoken)
            .then(function (data) {
                const parsed_data = JSON.parse(data);
                inbox.innerHTML = '';
                submitForm.querySelector('textarea[name="content"]').value = '';
                for (const message of parsed_data) {
                    let split_date = message.fields.sent_at.split('T');
                    let date = new Date(split_date[0]);
                    let time = split_date[1].slice(0, 8);
                    if (message.fields.sender == id) {
                        inbox.innerHTML += `<p class="message p-3 reciever">
                                                ${message.fields.content}
                                                <small class="d-block mt-2">${date.toDateString()}</small>
                                            </p>`;
                    } else {
                        inbox.innerHTML += `<p class="message p-3">
                                                ${message.fields.content}
                                                <small class="d-block mt-2">${date.toDateString()}</small>
                                            </p>`;
                    }
                }
            })
            .catch(function (error) {
                console.log(error);
            })
    }
});