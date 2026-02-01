import java.util.Scanner;

class Sample {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Array Size: ");
        int size=sc.nextInt();
        int[] num= new int[size];
        System.out.println("Enter Array Elements(upto "+size+"): ");
        for(int i=0; i<size;i++){
        num[i]=sc.nextInt();
        }
        for (int n:num){
            System.out.print(n+" "); 
        }
    }
}