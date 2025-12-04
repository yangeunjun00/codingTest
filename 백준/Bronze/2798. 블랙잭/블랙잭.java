import java.util.Scanner;

public class Main {

    public static void main(String[] args)  {
        Scanner in = new Scanner(System.in);
        int a =  in.nextInt();
        int b = in.nextInt();
        int temp = 0;
        int[] arr =  new int[a];
        for(int i = 0; i < arr.length; i++){
            arr[i] = in.nextInt();
        }
       int adj = 0;
        for(int i1 = 0;i1<arr.length;i1++){
            for(int i2 = i1+1;i2<arr.length;i2++){
                for(int i3 = i2+1;i3<arr.length;i3++){
                    temp = arr[i1]+arr[i2]+arr[i3];
                    if(b-temp<0){
                        continue;
                    }
                    if(b-adj>b-temp){
                        adj = temp;
                    }
                }
            }
        }
        System.out.println(adj);

    }
}

