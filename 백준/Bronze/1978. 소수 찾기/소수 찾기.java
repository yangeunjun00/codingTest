import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b;
        int sum = 0;
        for(int i = 1; i<=a;i++){
            b = in.nextInt();
            if(asdf(b))sum++;
        }
        System.out.println(sum);
    }
    public static boolean asdf(int a){
        if(a==2)return true;
        if(a%2==0)return false;
        if(a<2)return false;
        for(int i = 3; i*i<=a;i+=2){
            if(a%i==0)return false;
        }
        return true;
    }
}
