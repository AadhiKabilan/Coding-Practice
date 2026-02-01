import java.util.*;
class Fibonacci{
    public static void main(String[] args){
        //0 1 1 2 3 5 8 13 21 
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter N value: ");
        int n= sc.nextInt();
        sc.close();
        int num1=0;
        int num2=1;
        System.out.print(num1+" "+num2+" ");
        for(int i=2;i<=n;i++){
            int num3=num1+num2;
            System.out.print(num3+" ");
            num1=num2;
            num2=num3;
        }
    }
}