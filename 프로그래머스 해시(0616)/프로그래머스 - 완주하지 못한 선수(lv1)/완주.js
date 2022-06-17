function solution(participant, completion) {
    const hashed = {};
    participant.forEach(e => hashed[e] = hashed[e] ? hashed[e] + 1 : 1);
    completion.forEach(e => hashed[e] -= 1);
    for (let key in hashed) {
        if (hashed[key] >= 1) return key;
    }
}