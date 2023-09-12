#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  const val = Number(x);
  let i;
  for (i = 0; i < val; i++) {
    theFunction();
  }
};
