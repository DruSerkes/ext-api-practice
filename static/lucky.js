/** processForm: get data from form and make AJAX call to our API. */

// if the backend API does not return errors, it should put the following message into the result div:

async function processForm(evt) {
	evt.preventDefault();
	name = document.querySelector('#name').value;
	year = document.querySelector('#year').value;
	email = document.querySelector('#email').value;
	color = document.querySelector('#color').value;
	clearFields();

	resp = await axios.post(
		'/api/get-lucky-num',
		(data = {
			name,
			year,
			email,
			color
		})
	);
	handleResponse(resp);
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
	if (resp.data.errors) {
		for (let [ key, val ] of Object.entries(resp.data.errors)) {
			document.querySelector(`#${key}-err`).innerText = `${val}`;
		}
	} else {
		let message = document.createElement('p');
		message.innerText = `Your lucky number is ${resp.data.num.num} (${resp.data.num.fact}). \n
        Your birth year (${resp.data.year.year}) fact is: ${resp.data.year.fact}.`;
		document.querySelector('#lucky-results').append(message);
	}
}

$('#lucky-form').on('submit', processForm);

function clearFields() {
	// Clear fields upon capturing value
	document.querySelector('#name').value = '';
	document.querySelector('#year').value = '';
	document.querySelector('#email').value = '';
	document.querySelector('#color').value = '';

	// Clear errors on submit
	document.querySelector('#name-err').innerHTML = '';
	document.querySelector('#year-err').innerHTML = '';
	document.querySelector('#email-err').innerHTML = '';
	document.querySelector('#color-err').innerHTML = '';

	// Clear main content
	document.querySelector('#lucky-results').innerHTML = '';
}
