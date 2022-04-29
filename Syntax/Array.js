var arr = ['a','b','c','d'];
console.log(arr[1]);
console.log(arr[2]);
// ↑ 선택값
arr[2] = 3;
console.log(arr);
// ↑ 수정사항
console.log(arr.length);
// ↑ 총 개수
arr.push('e');
console.log(arr);
// ↑ 끝에 값 추가
