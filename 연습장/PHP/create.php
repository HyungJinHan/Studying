<?php
  require_once("lib/print.php");
  // top.php에 겹치는 require을 한번만 실행하게끔 지정
  require("view/top.php");
  // print.php 파일의 코드를 읽어오도록 하는 코드
?>
    <a href="create.php">생성</a>
    <form action="create_process.php" method="post">
      <!-- 누군가에게 링크를 보낼때 get 방식의 경우 파일이 즉석에서 생성되기 때문에
      방지를 위해 post 방식으로 사용, _process.php에도 post 형식으로 id값을 불러와야 함 -->
      <p>
        <input type="text" name="title" placeholder="제목을 입력하세요.">
      </p>
      <p>
        <textarea name="description" placeholder="본문을 입력하세요." rows="8" cols="30"></textarea>
      </p>
      <p>
        <input type="submit">
      </p>
    </form>
<?php
  require("view/bottom.php");
?>
