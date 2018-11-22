/*
MERGE(A, p, q, r)
    n1 = q - p + 1
    n2 = r - q
    let L[1..n1 + 1] and R[1..n2 + 1] be new arrays
    for i = 1 to n1
        L[i] = A[p + 1 - 1]
    for j = 1 to n2
        R[j] = A[q + j]
    L[n1 + 1] = 'sentinal'
    R[n2 + 1] = 'sentinal'
    i = 1
    j = 1
    for k = p to r
        if L[i] <= R[j]
            A[k] = L[i]
            i = i + 1
        else A[k] = R[j]
            j = j + 1
*/


/* Java program for Merge Sort */
public class MergeSort 
{ 
	// Merges two subarrays of arr[]. 
	// First subarray is arr[l..m] 
	// Second subarray is arr[m+1..r] 
	void merge(int A[], int p, int q, int r) 
	{ 
		// Find sizes of two subarrays to be merged 
		int n1 = q - p + 1; 
		int n2 = r - q; 

		/* Create temp arrays */
		int L[] = new int [n1]; 
		int R[] = new int [n2]; 

		/*Copy data to temp arrays*/
		for (int i=0; i<n1; ++i) 
			L[i] = A[p + i]; 
		for (int j=0; j<n2; ++j) 
			R[j] = A[q + 1+ j]; 


		/* Merge the temp arrays */

		// Initial indexes of first and second subarrays 
		int i = 0, j = 0; 

		// Initial index of merged subarry array 
		int k = p; 
		while (i < n1 && j < n2) 
		{ 
			if (L[i] <= R[j]) 
			{ 
				A[k] = L[i]; 
				i++; 
			} 
			else
			{ 
				A[k] = R[j]; 
				j++; 
			} 
			k++; 
		} 

		/* Copy remaining elements of L[] if any */
		while (i < n1) 
		{ 
			A[k] = L[i]; 
			i++; 
			k++; 
		} 

		/* Copy remaining elements of R[] if any */
		while (j < n2) 
		{ 
			A[k] = R[j]; 
			j++; 
			k++; 
		} 
	} 

	// Main function that sorts arr[l..r] using 
	// merge() 
	void sort(int A[], int p, int r) 
	{ 
		if (p < r) 
		{ 
			// Find the middle point 
			int q = (p+r)/2; 

			// Sort first and second halves 
			sort(A, p, q); 
			sort(A , q+1, r); 

			// Merge the sorted halves 
			merge(A, p, q, r); 
		} 
	} 

	/* A utility function to print array of size n */
	static void printArray(int A[]) 
	{ 
		int n = A.length; 
		for (int i=0; i<n; ++i) 
			System.out.print(A[i] + " "); 
		System.out.println(); 
	} 

	// Driver method 
	public static void main(String args[]) 
	{ 
		int A[] = {12, 11, 13, 5, 6, 7}; 

		System.out.println("Given Array"); 
		printArray(A); 

		MergeSort ob = new MergeSort(); 
		ob.sort(A, 0, A.length-1); 

		System.out.println("\nSorted array"); 
		printArray(A); 
	} 
} 
/* This code is contributed by Rajat Mishra */
