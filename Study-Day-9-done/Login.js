document.querySelector("#login_btn").addEventListener("click", () => {
  const id = "hhj";
  const password = "hhj";

  if(id == document.querySelector("#ID").value) {
    if(password == document.querySelector("#PW").value) {
      alert("연습장으로 이동합니다.");
      location.href = "연습장/index.html";
    }
    else {
      alert("비밀번호가 맞지 않습니다.");
    }
  }
  else {
    alert("아이디 혹은 비밀번호가 맞지 않습니다.");
  }
});

document.querySelector("#ToDoList").addEventListener("click", () => {
  const id = "hhj";
  const password = "hhj";

  if(id == document.querySelector("#ID").value) {
    if(password == document.querySelector("#PW").value) {
      alert("To Do List로 이동합니다.");
      window.open("연습장/To Do List/ToDoList.html");
    }
    else {
      alert("비밀번호가 맞지 않습니다.");
    }
  }
  else {
    alert("아이디 혹은 비밀번호가 맞지 않습니다.");
  }
});
