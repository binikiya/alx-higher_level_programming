#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let found = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      found++;
    }
  }
  return found;
};
