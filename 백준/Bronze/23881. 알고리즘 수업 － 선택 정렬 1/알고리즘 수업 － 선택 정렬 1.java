import java.util.Scanner;//TIP 코드를 <b>실행</b>하려면 <shortcut actionId="Run"/>을(를) 누르거나
// 에디터 여백에 있는 <icon src="AllIcons.Actions.Execute"/> 아이콘을 클릭하세요.
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int count = 0; //교환 횟수 세는 용 변수
        int[] arr = new int[a];
        for (int i = 0; i < a; i++) {
            arr[i] = sc.nextInt();
        }
        for(int i = arr.length-1;i>=0;i--){
            int temp = 0;
            for(int j = 1;j<=i;j++){
                if(arr[temp]<arr[j]){
                    temp = j;
                }
            }
            if(temp==i){
                continue;
            }
            ++count;
            int change = arr[temp];
            arr[temp] = arr[i];
            arr[i] = change;
            if(b==count){
                System.out.printf("%d %d",arr[temp],arr[i]);
            }
        }

        if(b>count){
            System.out.println(-1);
        }

    }

}
