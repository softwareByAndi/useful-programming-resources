const arr = [0, 1, 2, 3, 4, 5]

// array destructuring
const x = [...arr]
console.log("arr: ", arr)
console.log("x:   ", x)
console.log("\n----------------------\n")

// array destructure in variable declaration
let [
  var0,
  var1,
  var2,
  ...rest
] = arr

console.log("var0: ", var0)
console.log("var1: ", var1)
console.log("var2: ", var2)
console.log("rest: ", rest)
console.log("\n----------------------\n")

let v0 = arr[0],
  v1 = arr[1],
  v2 = arr[2],
  r = arr.slice(3)
console.log("v0: ", v0)
console.log("v1: ", v1)
console.log("v2: ", v2)
console.log("r: ", r)
