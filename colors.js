var links={

    SetColor:function(color){
    //   var alist=document.querySelectorAll('a');
    //   var i=0;

    //   while(i<alist.length){

    //     alist[i].style.color=color;
    //     i=i+1;
    //   }

    // }
    $('a').css('color',color)
    }

}
  
var Body={

    SetColor:function(color){
        //   var target=document.querySelector('body');
        //   target.style.color=color;
        $('body').css('color',color);
    
    }
    ,
    SetBGColor:function(color){
        //   var target=document.querySelector('body');
        //   target.style.backgroundColor=color;
        $('body').css('backgroundColor',color);
    }
    

}

    




function nightdayhandler(self){


    if(self.value=='night'){

      Body.SetBGColor('black');

      Body.SetColor('white');

      self.value='day';

      links.SetColor('powderblue');

      
      
    }

    else{
      
      Body.SetBGColor('white');
      Body.SetColor('black');
      self.value='night';

      links.SetColor('blue');

      
    }

  }
