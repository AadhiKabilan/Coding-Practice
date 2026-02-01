import java.util.*;
class MergeArrays {
    public static void main(String[] args){
        // Scanner sc = new Scanner(System.in);
        // System.out.println("Enter Array size: ");
        // int n=sc.nextInt();
        // int[] arr1 = new int[n];
        // System.out.println("Enter Array Elements: ");
        // for(int i=0;i<n;i++){
        //     arr1[i] = sc.nextInt();
        // }
        // System.out.println("Enter Array-2 size: ");
        // int m=sc.nextInt();
        // int[] arr2 = new int[m];
        // System.out.println("Enter Array Elements: ");
        // for(int i=0;i<m;i++){
        //     arr2[i] = sc.nextInt();
        // }
        int[] arr1={2,3,4,5,6};
        int[] arr2={1,4,5,6,6,7,8,9};
        // Arrays.sort(arr1);
        // Arrays.sort(arr2);
        System.out.println(Arrays.toString(arr1));
        System.out.println("Array 1: ");
        for(int i:arr1){
            System.out.print(i+" ");
        }
        System.out.println();
        System.out.println("Array 2: ");
        for(int i:arr2){
            System.out.print(i+ " ");
        }

        System.out.println("Union: "+ findUnion(arr1,arr2));
    }
    public static ArrayList<Integer> findUnion(int[] a, int[] b){
        ArrayList<Integer> result = new ArrayList<>();
        int i = 0, j=0;

        while(i<a.length && j<b.length){
            int current;
            if(a[i]<b[j]){
                current = a[i++];
            }
            else if(b[j]<a[i]){
                current=b[j++];
            }
            else {
                current=a[i];
                i++; j++;
            }

            addifNotduplicate(result,current);

            
        }
        int current;
        while(i<a.length){
                
                current=a[i];
                addifNotduplicate(result,current);
                i++;
            }
            while(j<b.length){
                current=b[j];
                addifNotduplicate(result,current);
                j++;
            }

        System.out.println(result);
        return(result);
    
    }
    static void addifNotduplicate(ArrayList<Integer> result, int value){
        if(result.size()==0 || result.get(result.size()-1)!=value){
            result.add(value);
        }
    }
}