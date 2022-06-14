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
  function day_nightHandler(self){
    var target = document.querySelector('body')
    if (self.value === '야간 모드'){
      Body.setBackgroundColor('#424242');
      Body.setColor('white');
      Link.setColor('white');
      self.value = '주간 모드';
    }
    else {
      target.style.backgroundColor = 'white';
      Body.setBackgroundColor('white');
      Body.setColor('black');
      Link.setColor('black');
      self.value = '야간 모드';
    }
  }
