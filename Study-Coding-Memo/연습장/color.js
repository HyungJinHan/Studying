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
  //var target = document.querySelector('body'); bodyμ λν target
    if (self.value === 'π μΌκ° λͺ¨λ π'){
      Body.setBackgroundColor('#424242');
      Body.setColor('white');
      Link.setColor('white');
      self.value = 'π μ£Όκ° λͺ¨λ π';
      document.querySelector('#disqus_thread').style.backgroundColor = '#BDBDBD';
    //target.style.backgroundColor = '#424242'; bodyμ λν κ°
      tabSetColor('#585858');
    }
    else {
  //var target = document.querySelector('body'); bodyμ λν target
    //target.style.backgroundColor = 'white'; bodyμ λν κ°
      Body.setBackgroundColor('white');
      Body.setColor('black');
      Link.setColor('black');
      self.value = 'π μΌκ° λͺ¨λ π';
      document.querySelector('#disqus_thread').style.backgroundColor = 'white';
      tabSetColor('#A4A4A4');
    }
  }
