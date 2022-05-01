const defaultArray = [0, 1, 2, 3, 4, 5]
console.log("arr0: ", defaultArray);

let arr1 = []
for (let i = 0; i < defaultArray.length; i++) {
  arr1.push(defaultArray[i] * 2)
}
console.log("arr1: ", arr1)

const arr2 = defaultArray.map(num => num * 2)
console.log("arr2: ", arr2)

const arr3 = defaultArray.filter(num => ( (num !== 3) && (num !== 1) ) )
console.log("arr3: ", arr3)

const arr4 = [0, 1, 2, 3, 4]
  .map(x => x * 3)
  .filter(x => (x % 2) === 0)
  .map((x, i) => {
    return {
      value: x,
      index: i
    }
  })
  .map(obj => {
    let temp = obj.value
    return (temp + 3) * obj.index
  })
console.log("arr4: ", arr4)

console.log("arr0: ", defaultArray);
