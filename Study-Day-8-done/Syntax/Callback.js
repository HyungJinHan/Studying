/*
function a(){
  console.log('A');
}
*/

var a = function a(){
  console.log('A');
} // 익명함수

function slowfunc(callback){
  callback();
}

slowfunc(a);
