function solution(slice, n) {
  var answer = 0;
  for (let i = 1; i <= n; i++) {
    answer = slice * i;
    if (answer >= n) {
      return i;
    }
  }
}
