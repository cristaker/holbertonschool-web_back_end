export default function getStudentIdsSum(ListStudents) {
    return ListStudents.reduce((total, student) => total + student.id, 0);
  }