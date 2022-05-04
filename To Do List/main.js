// list와 관련된 선택자를 먼저 설정
const containerBox = document.querySelector("#containerBox"),
    contents = containerBox.querySelector("#contents"),
    list = contents.querySelector("#list"),
    inputList = document.querySelector(".inputlist"),
    listForm = inputList.querySelector("#listForm"),
    input = listForm.querySelector("input");
const list_LS = "toDos";
// 웹에 정보 저장을 위한 빈 오브젝트
let toDos = [];
// localStorage를 이용하여 웹 자체에 정보를 저장, 객체를 JSON 문자열로 변환
function saveList(){
    localStorage.setItem(list_LS, JSON.stringify(toDos));
}

// 웹에 입력한 리스트를 보여주기 위함
// document.createElement() : 괄호 안에 있는 요소 생성
// span : 문장 단위로 영역 지정 (줄 바꿈이 일어나지 않음), div : 문단 단위로 영역을 지정 (줄 바꿈이 일어남)
function showingList(text){
    const li = document.createElement("li");
    const delbtn = document.createElement("button");
    const span = document.createElement("span");
    const listNum = toDos.length+1;
  // 리스트를 지울 수 있는 삭제 버튼 생성
  delbtn.innerText = "Done👍";
  delbtn.addEventListener("click", deleteList);
  span.innerText = text;
  // appendChild : 선택한 요소 안에 자식 요소를 추가
  list.appendChild(li);
  li.appendChild(span);
  li.appendChild(delbtn);
  li.id = listNum;
  const toDoObj = {
      text: text,
      id: listNum
  };
  toDos.push(toDoObj);
  // 입력된 리스트를 저장
  saveList();
}

//function addList(){
//  var contents = document.querySelector("input");
//  if(!contents.value){
//    alert("내용을 입력해주세요.");
//    contents.focus();
//    return false;
//  }
//}

// 삭제버튼을 누르면 해당되는 리스트를 지우는 함수
function deleteList(event){
    const btn = event.target;
    const li = btn.parentNode;
    list.removeChild(li);
  // filter() : 주어진 함수를 통과하는 모든 요소를 모아 재배열
  const cleanList = toDos.filter(function(toDo){
    // parseInt() : 문자열 인자의 구문을 분석해 특정 진수의 정수를 반환
    return toDo.id !== parseInt(li.id);
  });
  toDos = cleanList;
  saveList();
}

// input에 입력한 값을 다루는 함수
function handleSubmit(event){
  // event.preventDefault() : 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지않고 그 이벤트를 취소하는 기능
  event.preventDefault();
  const currentValue = input.value;
  showingList(currentValue);
  input.value = "";
}

// localStorage에 저장된 리스트를 불러오는 함수
function loadList(){
    const loadedList = localStorage.getItem(list_LS);
    if(loadedList !== null){
    // JSON.parse(): JSON 문자열의 구문을 분석하고 자바스크립트 값이나 객체를 생성
    const parsedData = JSON.parse(loadedList);
    parsedData.forEach(function(toDo){
      // 불러온 리스트를 보여주는 함수
      showingList(toDo.text);
    });
  }
}

function init(){
    loadList();
    listForm.addEventListener("submit", handleSubmit);
}

init();
