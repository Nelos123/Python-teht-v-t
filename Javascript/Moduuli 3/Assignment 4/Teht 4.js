'use strict';

const students = [
  { value: '2345768', name: 'John' },
  { value: '2134657', name: 'Paul' },
  { value: '5423679', name: 'Jones' }
];

const select = document.getElementById('target');

for (let student of students) {
  const option = document.createElement('option');
  option.value = student.value;
  option.textContent = student.name;
  select.appendChild(option);
}
