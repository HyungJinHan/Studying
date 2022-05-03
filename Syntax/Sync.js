var fs = require('fs');

/*
//readFileSync (비동기적)

console.log('A');
var result = fs. readFileSync('Syntax/sample.txt', 'utf8')
console.log(result);
console.log('C');
*/

//readFile (동기적)

console.log('A');
fs. readFile('Syntax/sample.txt', 'utf8', function(err, result){
    console.log(result);
}); // 위의 값인 B를 불러오기 전에 밑의 C값을 먼저 불러오는 현상이 생김
console.log('C');
