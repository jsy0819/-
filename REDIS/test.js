console.log("---------");
function add(a,b){
    return a+b;
}
function minus(a,b){
    return a-b;
}
const multi = function(a,b){
return a*b;
}
const divide = function(a,b){
    if(b===0){
        return '0으로 나눌 수 없습니다.';
    }else if(b==0){
        return '문자로 나눌 수 없습니다.';
    }else{
        return a/b;
    }

}
console.log(divide(3,"0"));
console.log(divide(3,0));
console.log(divide(10,3));
console.log(multi(4,6));
console.log(typeof multi);
console.log(typeof minus);
let x=54;
console.log(x);
x=1;
console.log(x);
let y=2;
x=10;

x= add(x,y);
console.log(x);
x= minus(x,y);
console.log(x);

name="bjsong";
console.log(name);

function nameOpen(nameValue){
return '우리집 이름은 '+nameValue+'입니다.';
}
let nameValue='ai';
console.log('우리집 이름은 '+nameValue+'입니다.');

console.log("4"+"4");
console.log('4'+'4');
console.log('우리집 '+nameValue+"입니다.");

let sName = 'I\'m a Boy';
console.log(sName);