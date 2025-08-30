function solution(array) {
  var answer = 0;
  for (let j = 0; j < array.length - 1; j++) {
    for (let i = 0; i < array.length - 1 - j; i++) {
      if (array[i] > array[i + 1]) {
        answer = array[i];
        array[i] = array[i + 1];
        array[i + 1] = answer;
      }
    }
  }
  return array[(array.length + 1) / 2 - 1];
}
