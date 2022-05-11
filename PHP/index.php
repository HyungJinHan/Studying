<?php
  require_once("lib/print.php");
  // top.php에 겹치는 require을 한번만 실행하게끔 지정
  require("view/top.php");
  // print.php 파일의 코드를 읽어오도록 하는 코드
?>
    <a href="create.php">생성</a>
    <?php if(isset($_GET["id"])) { ?>
      <!-- isset을 통해 id값의 유무에 따른 true, false 확인 후
      id가 없을 시 수정 버튼이 보이지 않도록 지정-->
      <a href="update.php?id=<?=$_GET["id"]?>">수정</a>
      <!-- 수정을 누를 시 원래 있던 제목과 본문이 남아있도록 지정 -->
      <!-- <?=$_GET["id"]?>와 <?php echo $_GET["id"]; ?>은 같음 -->
      <form action="delete_process.php" method="post">
        <input type="hidden" name="id" value="<?=$_GET["id"]?>">
        <!-- 원래의 아이디를 get하기 위해 숨김처리를 해서 id 받기 -->
        <br><input type="submit" value="삭제">
        <!-- <a href="delete_process.php?id=<?=$_GET["id"]?>">삭제</a> -->
        <!-- delete의 경우 거치는 파일이 필요없이 작동하는 php 파일로 바로 이동 -->
        <!-- get 방식의 경우 링크를 누군가에게 보내는 순간 바로 삭제가 되버리기 때문에
        post 형식으로 바꿔줘야 하고, 링크를 통해 삭제가 되기보다는
        submit 버튼을 통해 삭제 -->
      </form>
    <?php } ?>
  <h2>
    <?php
      print_title(); // 위에서 지정한 제목 함수 출력
    ?>
  </h2>
    <?php
      print_description(); // 위에서 지정한 목록 함수 출력
    ?>
<?php
  require("view/bottom.php");
?>
