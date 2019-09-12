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

sockMerchant(n, ar);
