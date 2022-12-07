#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((prevVal, currentVal) => currentVal === searchElement ? prevVal + 1 : prevVal, 0);
};
