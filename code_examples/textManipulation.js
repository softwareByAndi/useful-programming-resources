import { createRequire } from "module";
const require = createRequire(import.meta.url);
const fs = require('fs');

const eragon_txt = (fs.readFileSync('./eragon_en.txt', 'utf8'))
  .split('\n')

let newArray = []
for (let i = 0; i < eragon_txt.length; i++) {
  const sentence = eragon_txt[i].split('.')
  // const trim = sentence.trim()
  // const filtered = trim.length? trim : null
  newArray.push(sentence)
}

function splitSentencesByDelimiters(text, delimiters= ['.']) {
  if (delimiters.length === 0)
    return text

  return text
    .split(delimiters[0])
    .map(sentence => sentence.trim())
    .filter(sentence => sentence?.length)
    .map(sentence => splitSentencesByDelimiters(sentence, delimiters.slice(1)))
    .flat()
}

let mappedArray = eragon_txt
  .map(paragraph => paragraph.replace(/[“”]/g, '"'))
  .map(paragraph => splitSentencesByDelimiters(paragraph, ['.', '?', '!', ':', ';', '"']))
  .map(paragraph => {
    if (paragraph.length)
      return paragraph
    else
      return ['']
  })
  .flat()
console.log(mappedArray)
