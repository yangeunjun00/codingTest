import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int[] arr = new int[a];
        double max = 0;
        double dir= 0;
        for(int i = 0; i < a; i++){
            arr[i] = in.nextInt();
            if(arr[i]>max || i==0){
                max = arr[i];
            }
        }
        double sum = 0;
        for(int i = 0; i< a; i++){
            sum += (double) arr[i]/max*100;
        }
        System.out.printf("%f",sum/a);
    }
}



