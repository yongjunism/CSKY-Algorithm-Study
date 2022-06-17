function solution(clothes) {
    let answer = 1;
    
    let table = clothes.reduce((acc, cur) => {
        acc[cur[1]] = acc[cur[1]] ? acc[cur[1]] + 1 : 1;
        return acc;
    }, {});
    console.log(table);
    for (let key in table) {
        answer *= table[key] + 1;
    }
    
    return answer-1;
}