import java.util.*;
class BinarySearch{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);

        System.out.println("Enter Array size: ");
        int m=sc.nextInt();
        int[] arr = new int[m];

        System.out.println("Enter Array Elements: ");
        for(int i=0;i<m;i++){
            arr[i] = sc.nextInt();
        }
        System.out.println("Enter target value: ");
        int target= sc.nextInt();
        sc.close();
        for (int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println(" ");
        System.out.println("Sorted Array: ");
        int[] arr2=bubblesort(arr,m);
        for (int i=0;i<arr2.length;i++){
            System.out.print(arr2[i]+" ");
        }

        binarySearch(arr2,target);

    }
    public static int[] bubblesort(int[] arr,int m){
        
        for (int i=0;i<m;i++){
            for(int j=0;j<m-i-1;j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }
        return arr;
    }
    public static void binarySearch(int[] arr, int target){
        // 1 2 2 4 4 6
        int n = arr.length;
        int l=0;
        int h=n-1;
        

        while(l<=h){
            int mid=(l+h)/2;
            if(arr[mid]==target){
                System.out.println("Target found at "+mid);
                break;
            }
            else if(arr[mid]<target){
                l=mid+1;
            }
            else{
                h=mid-1;
            }

        }

    }
}