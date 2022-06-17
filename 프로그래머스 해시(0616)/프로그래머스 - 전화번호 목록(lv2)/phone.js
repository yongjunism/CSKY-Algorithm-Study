const phone_books = [["119", "97674223", "1195524421"], ["123","456","789"], ["12","123","1235","567","88"]];

function solution(phone_book) {
    const hash = {};
    phone_book.map(e => hash[e] = e);
    for (let key in hash) {
        let temp = "";
        for (let alphabet of key) {
            temp += alphabet;
            if (hash[temp] && temp !== key) {
                return false;
            }
        }
    }
    return true;
}

console.log(phone_books.map(solution));

