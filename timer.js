const start_btn=document.querySelector('#timer_start');
const reset_btn=document.querySelector('#timer_reset');

let input_minute=Number(document.getElementById('m_timer').value);
let input_second=Number(document.getElementById('s_timer').value);

let sum=input_minute*60 + input_second;

let timerFunction=function(){

    sum=sum-1;
    let minute=Math.floor(sum/60);
    let second=sum%60;

    if(minute<10) minute='0'+minute;
    if(second<10) second='0'+second;

    let timenow=minute+':'+second;

    let timeshown=document.querySelector('#w_timer h1');
    timeshown.textContent=timenow;

}

let timer_a;

start_btn.onclick=function(){

    let curState=document.querySelector('#timer_start').textContent;

    if(curState=='start'){
        document.querySelector('#timer_start').textContent='stop';
        timer_a=setInterval(timerFunction,1000);
    }
    else{
        document.querySelector('#timer_start').textContent='start';
        clearInterval(timer_a);
    }

}