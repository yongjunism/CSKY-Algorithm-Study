function solution(clothes) {
    let answer = 1;
   // [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
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

// forEach 배열의 각 원소마다 내부 함수를 돌리죠 돌리는데 반환값이 없어요 값을 하나만받죠
// 배열.forEach(e = > {});
// map
// 최종리턴값 = [a, b, c].reduce((과거값 = 이전의 반환값, 현재값 = 다음 루프의 배열의 다음값) => {
//     어쩌구저꺼구를
//     return 어떤값 => 다음 루프의 과거값
// }, 초기값 = 가장 처음의 과거값)
