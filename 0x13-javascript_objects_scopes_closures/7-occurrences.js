#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const secList = list.map(
    (x) => {
      if (x === searchElement) {
        return 1;
      } else {
        return 0;
      }
    }
  );

  for (let temp = 0; temp < secList.length; temp++) {
    if (secList[temp] === 1) {
      count += 1;
    }
  }
  return count;
};
