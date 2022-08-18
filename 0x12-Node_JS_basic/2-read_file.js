const fs = require('fs');

function countStudents(path) {
  let students = [];
  const StudentGroup = {};
  const studentObj = [];

  try {
    students = fs.readFileSync(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  students = students.split('\n');
  const header = students.shift().split(',');

  students.forEach((element) => {
    if (element) {
      const studentInfo = element.split(',');

      header.forEach((header, i) => {
        studentObj[header] = studentInfo[i];
        if (header === 'field') {
          if (StudentGroup[studentInfo[i]]) {
            StudentGroup[studentInfo[i]].push(studentObj.firstname);
          } else {
            StudentGroup[studentInfo[i]] = [studentObj.firstname];
          }
        }
      });
      studentObj.push(studentObj);
    }
  });
  console.log(`Number of students: ${studentObj.length}`);

  for (const info in StudentGroup) {
    if (StudentGroup[info]) {
      const listStudents = StudentGroup[info];
      console.log(`Number of students in ${info}: ${listStudents.length}. List: ${listStudents.join(', ')}`);
    }
  }
}

module.exports = countStudents;
