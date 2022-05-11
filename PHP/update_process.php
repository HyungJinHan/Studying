<?php
  rename("Data/".$_POST["old_title"], "Data/".$_POST["title"]);
  // 이전 파일명으로 update.php에서 설정한 old_title을 입력
  file_put_contents("Data/".$_POST["title"], $_POST["description"]);
  // Data라는 폴더에 POST 방식으로 파일을 불러옴 (제목과 본문 전부)
  header("Location: index.php?id=".$_POST["title"]);
  // Redirection : Location을 원하는 파일로 설정하면 자동으로 이동시켜주는 문법
  // index.php?id="생성된 페이지의 타이틀"로 이동한다는 의미
?>
