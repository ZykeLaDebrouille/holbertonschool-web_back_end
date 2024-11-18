# ES6 Data Manipulation

This project covers advanced concepts of data manipulation in JavaScript ES6.

## Learning Objectives

By the end of this project, you should be able to explain:

- How to use map, filter and reduce on arrays
- Typed arrays
- The Set, Map, and Weak link data structures

## Requirements

- All files will be executed on Ubuntu 20.04 LTS using NodeJS 20.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the .js extension
- Your code will be tested using Jest and the command npm run test
- Your code will be verified against lint using ESLint
- Your code needs to pass all the tests and lint. You can verify the entire project running npm run full-test
- All of your functions must be exported

## Setup

1. Install NodeJS 20.x
2. Install Jest, Babel, and ESLint in your project directory

## Tasks

### 0. Basic list of objects

Create a function `getListStudents` that returns an array of objects. Each object should have three attributes: `id` (Number), `firstName` (String), and `location` (String).

### 1. More mapping

Create a function `getListStudentIds` that returns an array of ids from a list of object. Use the `map` function on the array.

### 2. Filter

Create a function `getStudentsByLocation` that returns an array of objects who are located in a specific city. Use the `filter` function on the array.

### 3. Reduce

Create a function `getStudentIdsSum` that returns the sum of all the student ids. Use the `reduce` function on the array.

### 4. Combine

Create a function `updateStudentGradeByCity` that returns an array of students for a specific city with their new grade. Use `filter` and `map` combined.

### 5. Typed Arrays

Create a function `createInt8TypedArray` that returns a new `ArrayBuffer` with an `Int8` value at a specific position.

### 6. Set data structure

Create a function `setFromArray` that returns a `Set` from an array.

### 7. More set data structure

Create a function `hasValuesFromArray` that returns a boolean if all the elements in the array exist within the set.

### 8. Clean set

Create a function `cleanSet` that returns a string of all the set values that start with a specific string.

### 9. Map data structure

Create a function `groceriesList` that returns a map of groceries with items and their quantities.

### 10. More map data structure

Create a function `updateUniqueItems` that returns an updated map for all items with initial quantity at 1.

## Running Tests

To run the tests for each task, use the command:
npm run dev <main-file.js>

For example:
npm run dev 0-main.js

Ensure all tests pass before submitting your work.
