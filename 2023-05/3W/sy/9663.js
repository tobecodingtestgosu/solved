// const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().trim();

function main(n) {
  let answer = 0;
  const matrix = [];
  for (let i = 0; i < n; i++) {
    const cells = [];
    for (let j = 0; j < n; j++) {
      cells.push(0);
    }
    matrix.push(cells);
  }

  //let matrix = Array(n).fill(Array(n).fill(0));

  function checkQueen(y, x) {
    for (let i = 0; i < y + 1; i++) {
      if (matrix[i][x] == 1) return false;
      if (x >= i && matrix[y - i][x - i] == 1) return false;
      if (x < n - i && matrix[y - i][x + i] == 1) return false;
    }
    return true;
  }

  function backtracking(y) {
    if (y == n) {
      answer += 1;
      return;
    }
    for (let k = 0; k < n; k++) {
      if (!checkQueen(y, k)) continue;

      matrix[y][k] = 1;

      backtracking(y + 1);
      matrix[y][k] = 0;
    }
  }
  backtracking(0);
  return answer;
}

console.log(main(8));
