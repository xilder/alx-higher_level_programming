#!/usr/bin/node

const fs = require('fs');
const [fileA, fileB, fileC] = process.argv.slice(2, 5);

if (
  fs.existsSync(fileA)
  && fs.statSync(fileA).isFile
  && fs.existsSync(fileB)
  && fs.statSync(fileB).isFile
  && fileC !== undefined
) {
  const fileAContent = fs.readFileSync(fileA);
  const fileBContent = fs.readFileSync(fileB);
  const stream = fs.createWriteStream(fileC);

  stream.write(fileAContent);
  stream.write(fileBContent);
  stream.end();
}
