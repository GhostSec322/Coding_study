//Variavle
var a=10;
let b=10;
const c=10;
console.log(a,b,c)
//Function 
function f(x){
    let return_value= 2*x +3;
    return return_value;
}
function fly(){
    while(true){
        alert("State: fly")
        break;
    }
}
add=(x,y)=>{
    let c= x+y;
    return c;
}
// Condition 
let have_money = 5000;
if(have_money> 5000){
    alert("Ride Texi");
}else if(have_money > 2000){
    alert("Ride Bus")
}
else{
    alert("Walk");
}
// For ,While
for(let i=0; i<10; i++)
{
    console.log((i+1)+"번째 나무찍기");
}
myarray = [1,2,3,4,5]
myarray.forEach(element => {
    let i=1;
    console.log(i+"번째 나무")
    i++;
});