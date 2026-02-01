import java.util.*;
class Factorial{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter N value: ");
        int n= sc.nextInt();
        sc.close();
        System.out.println("Factorial of "+n+" is "+fact(n));
    }
    public static int fact(int n){
        //4
        //1 x 2 x 3 x 4
        if(n==1){
            return 1;
        }
            
        return n * fact(n-1);
    }
}