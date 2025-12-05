import java.util.Scanner;

public class Main {

    public static void main(String[] args)  {
        Scanner in = new Scanner(System.in);
        int a =  in.nextInt();
        int[] w =  new int[a];
        int[] t = new int[a];
        int[] cnt = new int[a];
        for(int i = 0; i <a;i++){
            w[i] = in.nextInt();
            t[i] = in.nextInt();
        }
        for(int j = 0; j<a;j++){
            for(int k = 0;k<a;k++){
                if(w[j]>w[k]&&t[j]>t[k]){
                    continue;
                }
                else if(w[j]>w[k]||t[j]>t[k]){
                    continue;
                }
                else if(w[j]<w[k]&&t[j]<t[k]){
                    cnt[j]+=1;

                }
            }
        }
        for(int j = 0; j<a;j++){
            System.out.print(cnt[j]+1+" ");
        }

    }
}

