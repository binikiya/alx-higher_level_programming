#!/usr/bin/node

exports.esrever = function(list) {
    const reversed = [];
    let j = 0;
    for (let i = list.length - 1; i >= 0; i--) {
	reversed[j] = list[i];
	j++;
    }
    return reversed;
}
