#!/bin/bash

# Créer le répertoire du projet
mkdir -p ES6_data_manipulation

# Créer les fichiers de tâches
touch ES6_data_manipulation/0-get_list_students.js
touch ES6_data_manipulation/1-get_list_student_ids.js
touch ES6_data_manipulation/2-get_students_by_loc.js
touch ES6_data_manipulation/3-get_ids_sum.js
touch ES6_data_manipulation/4-update_grade_by_city.js
touch ES6_data_manipulation/5-typed_arrays.js
touch ES6_data_manipulation/6-set.js
touch ES6_data_manipulation/7-has_array_values.js
touch ES6_data_manipulation/8-clean_set.js
touch ES6_data_manipulation/9-groceries_list.js
touch ES6_data_manipulation/10-update_uniq_items.js

# Créer les fichiers main correspondants
cat << EOF > ES6_data_manipulation/0-main.js
import getListStudents from "./0-get_list_students.js";

console.log(getListStudents());
EOF

cat << EOF > ES6_data_manipulation/1-main.js
import getListStudentIds from "./1-get_list_student_ids.js";
import getListStudents from "./0-get_list_students.js";

console.log(getListStudentIds("hello"));
console.log(getListStudentIds(getListStudents()));
EOF

cat << EOF > ES6_data_manipulation/2-main.js
import getListStudents from "./0-get_list_students.js";
import getStudentsByLocation from "./2-get_students_by_loc.js";

const students = getListStudents();

console.log(getStudentsByLocation(students, 'San Francisco'));
EOF

cat << EOF > ES6_data_manipulation/3-main.js
import getListStudents from "./0-get_list_students.js";
import getStudentIdsSum from "./3-get_ids_sum.js";

const students = getListStudents();
const value = getStudentIdsSum(students);

console.log(value);
EOF

cat << EOF > ES6_data_manipulation/4-main.js
import getListStudents from "./0-get_list_students.js";
import updateStudentGradeByCity from "./4-update_grade_by_city.js";

console.log(updateStudentGradeByCity(getListStudents(), "San Francisco", [{ studentId: 5, grade: 97 }, { studentId: 1, grade: 86 }]));

console.log(updateStudentGradeByCity(getListStudents(), "San Francisco", [{ studentId: 5, grade: 97 }]));
EOF

cat << EOF > ES6_data_manipulation/5-main.js
import createInt8TypedArray from "./5-typed_arrays.js";

console.log(createInt8TypedArray(10, 2, 89));
EOF

cat << EOF > ES6_data_manipulation/6-main.js
import setFromArray from "./6-set.js";

console.log(setFromArray([12, 32, 15, 78, 98, 15]));
EOF

cat << EOF > ES6_data_manipulation/7-main.js
import hasValuesFromArray from "./7-has_array_values.js";

console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1]));
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [10]));
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1, 10]));
EOF

cat << EOF > ES6_data_manipulation/8-main.js
import cleanSet from "./8-clean_set.js";

console.log(cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), 'bon'));
console.log(cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), ''));
EOF

cat << EOF > ES6_data_manipulation/9-main.js
import groceriesList from "./9-groceries_list.js";

console.log(groceriesList());
EOF

cat << EOF > ES6_data_manipulation/10-main.js
import updateUniqueItems from "./10-update_uniq_items.js";
import groceriesList from "./9-groceries_list.js";

const map = groceriesList();
console.log(map);

updateUniqueItems(map)
console.log(map);
EOF

echo "Fichiers créés avec succès!"