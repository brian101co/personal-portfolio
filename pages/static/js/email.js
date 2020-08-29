const sayHelloModal = document.querySelector('.contact-modal');

sayHelloModal.addEventListener('click', function(event) {
    if ( event.target.classList.contains('btn') ) {
        event.preventDefault()
        const email = sayHelloModal.querySelector('[name="email"]').value;

        if ( email ) {
            fetch(location.origin + "/api/verifyemail/" + email)
                .then(response => response.json())
                .then(data => {
                    parsed_data = JSON.parse(JSON.parse(data))
                    if ( parsed_data.format_valid && parsed_data.smtp_check ) {
                        sayHelloModal.submit();
                    } else {
                        let container = sayHelloModal.querySelector('[name="email"]').parentElement;
                        container.innerHTML += `<div class="alert alert-danger mt-2">
                                                    Please provide a valid email address.
                                                </div>`
                    }
                })
                .catch(err => console.log(err));
        } else {

        }
    }
});