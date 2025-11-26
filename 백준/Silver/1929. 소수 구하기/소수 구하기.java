import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        for(int i=a;i<=b;i++){
            if(prime(i)) {
                System.out.println(i);
            }
        }
    }

    public static boolean prime(int n) {
        if(n==2)return true;
        if(n%2==0)return false;
        if(n<2)return false;
        for(int i=3;i*i<=n;i+=2){
            if(n%i==0)return false;
        }
        return true;
    }

}



