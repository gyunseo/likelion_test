const start_btn=document.querySelector('#timer_start');
const reset_btn=document.querySelector('#timer_reset');

let input_minute;
let input_second;

let sum;

let timer_a;

let timerFunction=function(){

    if(sum==1) clearInterval(timer_a);

    sum=sum-1;
    let minute=Math.floor(sum/60);
    let second=sum%60;

    if(minute<10) minute='0'+minute;
    if(second<10) second='0'+second;

    let timenow=minute+':'+second;

    let timeshown=document.querySelector('#w_timer h1');
    timeshown.textContent=timenow;

}


start_btn.onclick=function(){

    input_minute=Number(document.getElementById('m_timer').value);
    input_second=Number(document.getElementById('s_timer').value);
    sum=input_minute*60+input_second;

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

reset_btn.onclick=function(){

    document.querySelector('#m_timer').value='0';
    document.querySelector('#s_timer').value='0';
    document.querySelector('#w_timer h1').textContent='00:00';
    clearInterval(timer_a);

}