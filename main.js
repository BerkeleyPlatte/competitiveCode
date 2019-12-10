let n = 9;
let ar = [10, 20, 20, 10, 10, 30, 50, 10, 20];

function sockMerchant(n, ar) {
  console.log(ar);
  let stringAr = ar.map(String);
  console.log(stringAr);
  let uniqueAr = [];
  let obj = {};
  for (let i = 0; i < n; i++) {
    if (uniqueAr.includes(stringAr[i]) === false) {
      uniqueAr.push(stringAr[i]);
    }
  }
  console.log(uniqueAr);
  for (let i = 0; i < uniqueAr.length; i++) {
    obj[uniqueAr[i]] = [];
  }
  // console.log(obj);
  Object.keys(obj).forEach(key => {
    for (let i = 0; i < n; i++) {
      if (key === stringAr[i]) {
        obj[key].push(stringAr[i]);
      }
    }
  });
  // console.log(obj);
  let count = 0;
  Object.values(obj).forEach(value => {
    if (value.length % 2 !== 0) {
      value.pop();
    }
    let num = value.length / 2;
    count += num;
  });
  // console.log(obj);
  console.log(count);
  return count;
}
// Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

// #Example 1: a1 = ["arp", "live", "strong"]

// a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

// returns ["arp", "live", "strong"]

// #Example 2: a1 = ["tarp", "mice", "bull"]

// a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

// returns []

function inArray(array1, array2) {
  let answer = [];
  array2.forEach(str => {
    array1.forEach(substr => {
      if (str.includes(substr)) {
        if (answer.includes(substr) === false) {
          answer.push(substr);
        }
      }
    });
  });
  return answer.sort();
}
