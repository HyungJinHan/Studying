// click 이벤트 걸기
document.getElementById("btnAdd").addEventListener("click", addList); // 추가
document.getElementById("DeleteSel").addEventListener("click", delSelected); // 선택 항목 삭제
document.getElementById("btnDelAll").addEventListener("click", delAllEle); // 전체 항목 삭제

// click 이벤트에 대한 함수

// 추가 : addList() 함수
function addList(){
  var contents = document.querySelector(".text-basic");
    if(!contents.value){
      alert("내용을 입력해주세요.");
      contents.focus();
      return false;
    }  // 내용을 비우고 추가를 할시 alert

  // tr, td, input을 새로 생성 / input에 type="checkbox", class="btn-chk" 속성 부여
  var tr = document.createElement("tr");
  // var label = document.createElement("label");
  var input = document.createElement("input");
  input.setAttribute("type", "checkbox");
  input.setAttribute("id", "btn-chk");
  // label.setAttribute("for", "btn-chk");
  // label.htmlFor = "btn-chk";

  var td01 = document.createElement("td");
  td01.appendChild(input);
  // td01.appendChild(label);
  tr.appendChild(td01);

  var td02 = document.createElement("td");
  td02.innerHTML = contents.value;
  tr.appendChild(td02);

  document.getElementById("list-body").appendChild(tr);
  contents.value="";
  contents.focus();
}

// 선택 항목 삭제
function delSelected(){
  var body = document.getElementById('list-body');
  var chkbox = document.querySelectorAll('#btn-chk');
  for(var i in chkbox){
    if(chkbox[i].nodeType == 1 && chkbox[i].checked == true){
      body.removeChild(chkbox[i].parentNode.parentNode);
    }
  }
}

// 전체 항목 삭제
function delAllEle(){
  var list = document.getElementById("list-body")
  while(list.firstChild){
    list.removeChild(list.firstChild);
  }
}
