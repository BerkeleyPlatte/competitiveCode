function r(n) {
  return Number(
    String(n)
      .split("")
      .reverse()
      .join("")
  );
}

console.log(r(35231));

function r2(n) {
  let nS = n.toString();
  let nSm = nS.split("").reverse();
  let finArr = [];
  nSm.forEach(num => {
    finArr.push(parseInt(num));
  });
  return finArr;
}

console.log(r2(1234));
