import java.util.*;
class MaxMinArray {
    public static void main(String[] args){
        int[] arr={2,1,5,3,7,4,6};
        int n=arr.length;
        Arrays.sort(arr);

        int[] temp = new int[n];
        int min=0;
        int max=n - 1;
        // System.out.println(min+" "+max);
        for(int j=0; j<n;j++){
            if(j%2==0){
                temp[j]=arr[max];
                max--;
            }else{
                temp[j]=arr[min];
                min++;
            }
        }
        
        for(int i:temp){
            System.out.print(i+" ");
        }
    }
}