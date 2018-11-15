/*
    Pseudo:
    for j = 2 to A.length
        key = A[j]
        //Insert A[j] into the sorted sequence A[1..j - 1].
        i = j - 1
        while i > 0 and A[i] > key
            A[i + 1] = A[i]
            i = i -1
        A[i + 1] = key

*//


public class MyClass {
    
    public static void main(String args[]) {
        int[] A = {5,2,4,6,1,3};
        
        InsertionSort(A);
        
    }
    
    public static void InsertionSort(int A[]){
        
        int n = A.length;
        for (int i = 1; i < n; ++i)
        {
            int key = A[i];
            int j = i - 1;
                
            while(j >= 0 && A[j] > key)
            {
                A[j+1] = A[j];
                j = j - 1;
            }
            A[j + 1] = key;
  
        }
        
          //Result of A
          for(int i = 0; i < A.length; i++)
          {
              System.out.println(A[i]);
          }
   
    }
}
