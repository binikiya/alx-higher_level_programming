#!/usr/bin/node

const Square2 = require('./5-square.js');
module.exports = class Square extends Square2 {
    charPrint(c) {
	if (c === undefined) {
	    this.print();
	}
	else {
	    for (let i = 0; i < this.height; i++) {
		console.log('C'.repeat(this.width));
	    }
	}
    }
}
