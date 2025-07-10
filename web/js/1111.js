let i = 0;
let j = 0;
while(i<10){
    i++;
    if (i % 2 === 0) {
        continue;
    }
    j++;
    console.log("i :"+i+" j :"+j);
}