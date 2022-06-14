var Link = {
  setColor:function (color){
    // var alist = document.querySelectorAll('a');
    // var i = 0;
    // while(i < alist.length){
    //   alist[i].style.color = color;
    //   i = i + 1;
    // }
    $('a').css('color', color);
  }
}
  var Body = {
    setColor:function (color){
      //document.querySelector('body').style.color = color;
      $('body').css('color', color);
    },
    setBackgroundColor:function (color){
      //document.querySelector('body').style.backgroundColor = color;
      $('body').css('backgroundColor', color);
    }
  }
  function tabSetColor(color){
    // var alist = document.querySelectorAll('.tab');
    // var i = 0;
    // while(i < alist.length){
    //  alist[i].style.color = color;
    //  i = i + 1;
    // }
    $('.tab').css('color', color);
  }
  function day_nightHandler(self){
  //var target = document.querySelector('body'); body에 대한 target
    if (self.value === '🌜 야간 모드 🌜'){
      Body.setBackgroundColor('#424242');
      Body.setColor('white');
      Link.setColor('white');
      self.value = '🌞 주간 모드 🌞';
      document.querySelector('#disqus_thread').style.backgroundColor = '#BDBDBD';
    //target.style.backgroundColor = '#424242'; body에 대한 값
      tabSetColor('#585858');
    }
    else {
  //var target = document.querySelector('body'); body에 대한 target
    //target.style.backgroundColor = 'white'; body에 대한 값
      Body.setBackgroundColor('white');
      Body.setColor('black');
      Link.setColor('black');
      self.value = '🌜 야간 모드 🌜';
      document.querySelector('#disqus_thread').style.backgroundColor = 'white';
      tabSetColor('#A4A4A4');
    }
  }
