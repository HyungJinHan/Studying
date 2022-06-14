var family = [1,10,100,1000,10000,100000,1000000,10000000];
// var family = ['hyun','sung','jin','ju','sik','kyung','hun','hye'];
var i = 0;
var total = 0;
while(i < family.length){
  total = total + family[i]
  i = i + 1;
}
// console.log(family[i]);
console.log(`total : ${total}`);
