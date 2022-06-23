function solution(progresses, speeds) {
    // 남은 작업 진도 계산
    const rest = progresses.map(e => 100-e);
    // 배포까지 남은 날짜 계산
    const days = [];
    for (let i = 0; i<rest.length; i++) {
        days.push(Math.ceil(rest[i]/speeds[i]));
    }
    // 결과 넣는 배열
    const result = [];
    // 한번 배포할때 배포되는 기능 개수
    let count = 1;
    // visited 배열
    const visited = Array.from({length: days.length}, () => false);
    // 이중 for 돌리기
    for (let j = 0; j<days.length; j++) {
        for (let k = j+1; k<days.length+1; k++) {
            // 한번 찍어서 계산된곳이면 그냥 다음 루프 돌게함
            if (visited[k] === true || visited[j] === true) {
                continue;
            }
            // 앞 값이 뒷값보다 크거나 같으면 count 증가하고 visited 체크
            if (days[j] >= days[k]) {
                count += 1;
                visited[k] = true;
            // 뒷값이 더 크면 지금까지의 count를 result 배열에 넣고 count 1로 초기화, 시작값 visited 체크
            } else {
                result.push(count);
                count = 1;
                visited[j] = true;
            }
        }

    }
    return result;
}
