function solution(priorities, location) {
    let max;
    let count = 0;
    
    while (true) {
        max =  Math.max(...priorities);
        let first = priorities.shift();
        
        if (first === max) {
            count += 1;
            if (location === 0) {
                return count;
            }
        } else {
            priorities.push(first);
        }
        location -= 1;
        
        if (location === -1) {
            location = priorities.length-1;
        }
    }
}
