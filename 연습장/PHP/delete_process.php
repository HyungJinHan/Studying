<?php
  unlink("Data/".basename($_POST["id"]));
  // 해당 id 값의 파일을 삭제, submit 형식으로 수정했기에 post 방식으로
  // 파일 삭제 시 나오는 파일의 경로와 그 외의 method와 같은 경로를
  // 제외시키도록 $_POST["id"]에 basename 지정
  header("Location: index.php");
  // 삭제 후 홈으로 이동하도록 지정
?>
