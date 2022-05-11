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
      <!-- 수정을 누를 시 원래 있던 제목과 본문이 글 박스에 남아있도록 지정 -->
      <!-- <?=$_GET["id"]?>와 <?php echo $_GET["id"]; ?>은 같음 -->
    <?php } ?>
  <h2>
    <?php
      print_title(); // 위에서 지정한 제목 함수 출력
    ?>
  </h2>
    <?php
      print_description(); // 위에서 지정한 목록 함수 출력
    ?>
    <form action="update_process.php" method="post">
      <!-- 누군가에게 링크를 보낼때 get 방식의 경우 파일이 즉석에서 생성되기 때문에
      방지를 위해 post 방식으로 사용, _process.php에도 post 형식으로 id값을 불러와야 함 -->
      <input type="hidden" name="old_title" value="<?=$_GET["id"]?>">
      <!-- 원래의 파일명을 input 숨김을 통해 서버로 원래의 파일명 전송 -->
      <!-- 숨겨진 input에 <?=$_GET["id"]?>를 통한 원래 파일명을 지정 -->
      <p>
        <input type="text" name="title" placeholder="제목을 입력하세요."
        value="<?php print_title(); ?>">
        <!-- value : 글 박스에 남아있는 글씨 지정
        print_xxx();을 통해 지정한 제목을 value값으로 남겨두기-->
      </p>
      <p>
        <textarea name="description" placeholder="본문을 입력하세요."
        rows="8" cols="30">"<?php print_description(); ?>"</textarea>
        <!-- textarea 태그 사이에 본문에 해당하는 php코드 입력 -->
      </p>
      <p>
        <input type="submit">
      </p>
    </form>
<?php
  require("view/bottom.php");
?>
