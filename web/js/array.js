/*
배열(array)
*/

const arraySum1 = function(num){
    let z=0;
    num.forEach(function(num){
        z += num;
    });
    return z;
};

const arraySum2 = (num) => {
    let z=0;
    num.forEach(num =>{
        z += num;
    });
    return z;
}
const arraySum = function(num){
    let z=0;
    
    
    for(i=0;i<num.length;i++){
        //console.log(i + '배열의 크기' + num.length);
         //z = z+num[i];
         z += num[i];
    }
         
    /*
    z = num[0]+num[1];
    z = z+num[2];
    z = z+num[3];
    z = z+num[4];
    */
    return z;
}

let myNum = [1,2,3,4,5];
myNum.forEach
console.log(myNum.length);
console.log(myNum[0]);
console.log(arraySum(myNum));
console.log(arraySum1(myNum));
console.log(arraySum2(myNum));
console.log(typeof myNum);


for (i = 0; i < 10; i++) {
    if(i>=1){
        console.log(i);
        for(j=1;j<10;j++){
            console.log(i+'*'+j+' = '+i*j);
        }
    }
   
}