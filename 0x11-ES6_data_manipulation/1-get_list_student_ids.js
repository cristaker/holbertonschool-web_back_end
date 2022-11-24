export default function getListStudentIds(ListStudents) {
    if (!Array.isArray(ListStudents)) return [];
    return ListStudents.map((element) => element.id);
  }