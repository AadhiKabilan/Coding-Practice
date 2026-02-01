import java.util.*;
class LinearSearch{
    public static void main(String[] args){
        int[] arr = {2,4,1,5,3,8,3,4};
        int target=8;
        for (int i=0;i<arr.length;i++){
            if(arr[i]==target){
                System.out.println(arr[i]+" Found at "+i+" index");
                break;
            }
            System.out.println("Checking "+i+" and "+ arr[i]);
        }
    }
}