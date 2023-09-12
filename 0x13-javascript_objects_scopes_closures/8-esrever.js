#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let i;
  for (i = 1; i <= list.length; i++) {
    const val = list.slice(-i)[0];
    newList.push(val);
  }
  return newList;
};
