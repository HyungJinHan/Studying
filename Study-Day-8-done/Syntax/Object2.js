var q = {
  v1:'h',
  v2:'h',
  v3:'j',
  f1:function (){
    console.log(this.v1);
  },
  f2:function (){
    console.log(this.v2);
  },
  f3:function (){
    console.log(this.v3);
  }
}

q.f1();
q.f2();
q.f3();
