#!/usr/bin/node
const dict = require('./101-data').dict;

const totaList = Object.entries(dict);
const values = Object.values(dict);
const valuesUniq = [...new Set(values)];
const newDict = {};
for (const j in valuesUniq) {
  const list = [];
  for (const k in totaList) {
    if (totaList[k][1] === valuesUniq[j]) {
      list.unshift(totaList[k][0]);
    }
  }
  newDict[valuesUniq[j]] = list;
}
console.log(newDict);
