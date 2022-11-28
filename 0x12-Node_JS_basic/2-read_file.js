const fs = require('fs');

module.exports = function countStudents(path) {
  let students = [];

  try {
    students = fs.readFileSync(path, { encoding: 'utf8', flag: 'r' });
  } catch (err) {
    throw Error('Cannot load the database');
  }
  students = students.split('\n');
  const headers = students.shift().split(',');

  const groupingStudentsField = {};
  const studentsObjects = [];

  students.forEach((student) => {
    if (student) {
      const studentInfo = student.split(',');
      const studentObject = {};

      headers.forEach((header, index) => {
        studentObject[header] = studentInfo[index];
        if (header === 'field') {
          if (groupingStudentsField[studentInfo[index]]) {
            groupingStudentsField[studentInfo[index]].push(studentObject.firstname);
          } else {
            groupingStudentsField[studentInfo[index]] = [studentObject.firstname];
          }
        }
      });
      studentsObjects.push(studentObject);
    }
  });

  console.log(`Number of students: ${studentsObjects.length}`);

  for (const groupStudent in groupingStudentsField) {
    if (groupingStudentsField[groupStudent]) {
      const listStudents = groupingStudentsField[groupStudent];
      console.log(`Number of students in ${groupStudent}: ${listStudents.length}. List: ${listStudents.join(', ')}`);
    }
  }
};