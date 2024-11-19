```markdown
# Promises and Async/Await in JavaScript

## Author
**Enes**
[GitHub Profile](https://github.com/ZykeLaDebrouille)

## Learning Objectives

- Understand how to create and use Promises.
- Learn the methods: `then`, `catch`, and `finally`.
- Understand the use of `async` and `await`.
- Learn how to handle errors with `try/catch`.

## Requirements

- Node.js version 20.x.x
- npm version 9.x.x
- All files should end with a new line.
- A README.md file at the root of the project.
- Code must be tested using Jest.

## Examples

### Creating a Promise

```javascript
function myPromise() {
  return new Promise((resolve, reject) => {
    // Logic here
  });
}
```

### Using async/await

```javascript
async function asyncFunction() {
  try {
    const result = await myPromise();
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}
```

## Tasks

### 0. Keep every promise you make and only make promises you can keep

Create a function `getResponseFromAPI()` that returns a Promise.

**Example Output:**
```javascript
const response = getResponseFromAPI();
console.log(response instanceof Promise); // true
```

### 1. Don't make a promise...if you know you can't keep it

Create a function `getFullResponseFromAPI(success)` that returns a promise based on a boolean parameter.

**Example Output:**
```javascript
console.log(getFullResponseFromAPI(true)); // Promise { { status: 200, body: 'Success' } }
console.log(getFullResponseFromAPI(false)); // Promise { <rejected> Error: The fake API is not working currently }
```

### 2. Catch me if you can!

Create a function `handleResponseFromAPI(promise)` that appends three handlers to the given promise.

**Example Output:**
```javascript
const promise = Promise.resolve();
handleResponseFromAPI(promise); // Logs: Got a response from the API
```

### 3. Handle multiple successful promises

Create a function `handleProfileSignup()` that uses `uploadPhoto` and `createUser` from utils.js to log profile information.

**Example Output:**
```javascript
handleProfileSignup(); // Logs: photo-profile-1 Guillaume Salva
```

### 4. Simple promise

Create a function `signUpUser(firstName, lastName)` that returns a resolved promise with user information.

**Example Output:**
```javascript
console.log(signUpUser("Bob", "Dylan")); // Promise { { firstName: 'Bob', lastName: 'Dylan' } }
```

### 5. Reject the promises

Create a function `uploadPhoto(filename)` that returns a Promise rejecting with an Error.

**Example Output:**
```javascript
console.log(uploadPhoto('guillaume.jpg')); // Promise { <rejected> Error: guillaume.jpg cannot be processed }
```

### 6. Handle multiple promises

Create a function `handleProfileSignup(firstName, lastName, fileName)` that returns an array of settled promises.

**Example Output:**
```javascript
console.log(handleProfileSignup("Bob", "Dylan", "bob_dylan.jpg"));
// Logs an array of results from both promises.
```

### 7. Load balancer

Create a function `loadBalancer(chinaDownload, USDownload)` that returns the value of the promise that resolves first.

**Example Output:**
```javascript
const test = async () => {
    console.log(await loadBalancer(promiseUK, promiseFR)); // Logs whichever download completes first.
}

test();
```

### 8. Throw an error

Create a function `divideFunction(numerator, denominator)` that throws an error when dividing by zero.

**Example Output:**
```javascript
console.log(divideFunction(10, 2)); // 5
console.log(divideFunction(10, 0)); // Throws Error: cannot divide by 0
```

### 9. Throw error / try catch

Create a function `guardrail(mathFunction)` that executes a function and returns an array with the result and a guard message.

**Example Output:**
```javascript
console.log(guardrail(() => { return divideFunction(10, 2)}));
// Logs: [5, 'Guardrail was processed']
console.log(guardrail(() => { return divideFunction(10, 0)}));
// Logs: ['Error: cannot divide by 0', 'Guardrail was processed']
```
```
