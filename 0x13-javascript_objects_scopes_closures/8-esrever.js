#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    reverse[j] = list[i];
    j++;
  }
  return (reverse);
};
