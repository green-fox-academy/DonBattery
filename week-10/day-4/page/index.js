'use strict';

/* eslint linebreak-style: ["error", "windows"] */

const dropDownMenu = document.getElementById('dropDown');

const inputTextField = document.getElementById('textInput');

const radioB1 = document.getElementById('radioButton1');

const radioB2 = document.getElementById('radioButton2');

const check1 = document.getElementById('checkBox1');

const submit = document.getElementById('submitButton');

// -------------------------------------------------------------------------------------------------

dropDownMenu.addEventListener('change', () => { console.log('Drop down menu:', dropDownMenu.options.selectedIndex); });

inputTextField.addEventListener('input', () => { console.log('Input Text', inputTextField.value); });

radioB1.addEventListener('change', () => { console.log('Radio1', radioB1.checked); });

radioB2.addEventListener('change', () => { console.log('Radio2', radioB2.checked); });

check1.addEventListener('change', () => { console.log('Checkbox', check1.checked); });

submit.addEventListener('click', (event) => {
  event.preventDefault();
  console.log('Submit Button clicked!');
});

function displayMessage (message, error = false) {
  const messageBox = document.querySelector('.messageBox');
  messageBox.innerHTML = message;
  messageBox.classList = error
    ? 'box messageBox error'
    : 'box messageBox normal';
}

displayMessage('Please set up your query', true);
