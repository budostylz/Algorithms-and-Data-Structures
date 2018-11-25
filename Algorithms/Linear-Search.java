// Java code for linearly search in x in arr[].
//If x is present then return it's location, overwise return -1

public class LinearSearch
{
    // This function returns index of element x in arr[]
    static int search(int arr[], int n, int x)
    {
        for (int i = 0; i < n; i++)
        {
            // Return the index of the element if the element is found
            if (arr[i] == x) 
                return i;
        }

        // return -1 if the element is not found
        return -1;
    }

    // Driver method to test above 
	public static void main(String args[]) 
	{ 
        int arr[] = {2, 3, 4, 10, 40};
        int n = arr.length;
        int x = 10;
        int i = search(arr, n, x);

        System.out.println("Element found at index "+ i);

		
	} 

}

/* This code is contributed by Rajat Mishra. */