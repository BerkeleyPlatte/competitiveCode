s = "UDDDUDUU";

function countingValleys(s) {
  let sm = "a" + s;
  console.log(sm);
  let count = 0;
  let countArr = [];
  let valleyCount = 0;
  for (let i = 0; i < sm.length; i++) {
    if (sm[i] === "U") {
      count += 1;
      countArr.push(count);
    } else if (sm[i] === "D") {
      count -= 1;
      countArr.push(count);
    } else {
      countArr.push(count);
    }
  }
  console.log(countArr);
  for (let i = 0; i < countArr.length; i++) {
    if (countArr[i] === 0) {
      if (countArr[i - 1] === -1) {
        valleyCount += 1;
      }
    }
  }
  console.log(valleyCount);
}

countingValleys(s);
