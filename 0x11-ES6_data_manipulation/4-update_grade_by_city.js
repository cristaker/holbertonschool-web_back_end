export default function updateStudentGradeByCity(listStudents, city, newGrades) {
    return listStudents.filter(
      (student) => student.location === city,
    ).map((student) => Object.assign(
      student,
      { grade: newGrades.filter((grade) => student.id === grade.studentId)[0] ? newGrades.filter((grade) => student.id === grade.studentId)[0].grade : 'N/A' },
    ));
  }