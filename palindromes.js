let a = "Racecar";
let b = "yes";
let c = "mom";
let d = "DAD";
let e = "Berkeley";

function palindrome1(x) {
  let xLower = x.toLowerCase();
  let xLowerRev = xLower
    .split("")
    .reverse()
    .join("");
  if (xLower === xLowerRev) {
    console.log(`${x} is a palindrome`);
  } else {
    console.log(`${x} ain't no palindrome`);
  }
}

// palindrome1(a);
// palindrome1(b);
// palindrome1(c);
// palindrome1(d);
// palindrome1(e);

function palindrome2(x) {
  let xReduced = x.toLowerCase().replace(/[^a-z0-9]+/g, "");
  let xReducedRev = xReduced
    .split("")
    .reverse()
    .join("");
  if (xReduced === xReducedRev) {
    console.log(`${x} is a palindrome`);
  } else {
    console.log(`${x} ain't no palindrome`);
  }
}

palindrome2("A man, a plan, a canal: Panama");
palindrome2("This is NOT a palindrome!");
