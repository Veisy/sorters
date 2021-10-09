#include <stdio.h>
#include <stdlib.h>
 
 
//Function declarations. Functions are defined below the main function.
float *insertion_sort (float A[], int Asize);
float *merge_insertion_sort(float A[], int Asize)
void merge_insertion_based(float A[], int Asize);
float *merge_sort(float A[], int Asize);
void merge_recursive(float A[], int Asize);
void merge(float A[], float L[], float R[], int Asize, int Lsize, int Rsize);


//This function sort the elements of the array.
	/*
	The Algorithm :
	1 - If it is the first element, it is already sorted.
	2 - Pick the next element.
	3 - Compare with all the elements in sorted sub-list.
	4 - Shift all the the elements in sorted sub-list that is greater than the value to be sorted.
	5 - Insert the value.
	6 - Repeat until list is sorted.
	*/
float *insertion_sort (float A[], int Asize) {
	int tempValue;
	
    int i = 1;
	 while (i < Asize) {
		
     	int j = i;

        while (j > 0 &&  (A[j - 1] > A[j])) {	        
			tempValue = A[j];
			A[j]      = A[j - 1];
        	A[j - 1]  = tempValue;
            j--;
        }
        i++;
  	}
  	return A
}

float *merge_insertion_sort(float A[], int Asize) {
    merge_insertion_based(A, Asize);
    return
}

// Insertion Sort based, hybrid algorithm. 
void merge_insertion_based(float A[], int Asize) {
	int mid,i;
	if(Asize < 2) return; // base condition. If the array has less than two element, do nothing. 

	mid = Asize/2;  // find the mid index.
	int Lsize = mid;
	int Rsize = (Asize - mid);
    
    float L[Lsize];
    float R[Rsize];
	
	for(i = 0; i < mid; i++) L[i] = A[i]; // creating left subarray
	for(i = mid; i < Asize; i++) R[i-mid] = A[i]; // creating right subarray

	insertion_sort(L, Lsize);  // sorting the left subarray
	insertion_sort(R, Rsize);  // sorting the right subarray
	merge(A, L, R, Asize, Lsize, Rsize);  // Merging L and R into A as sorted list.
}


float *merge_sort(float A[], int Asize) {
    merge_recursive(A, Asize);
    return A;
}

// Recursive function to sort an array of integers. 
void merge_recursive(float A[], int Asize) {
	int mid,i;
	if(Asize < 2) return; // base condition. If the array has less than two element, do nothing. 

	mid = Asize/2;  // find the mid index.
	int Lsize = mid;
	int Rsize = (Asize - mid);
    
    float L[Lsize];
    float R[Rsize];

	for(i = 0; i < mid; i++) L[i] = A[i]; // creating left subarray
	for(i = mid; i < Asize; i++) R[i-mid] = A[i]; // creating right subarray

	merge_recursive(L, Lsize);  // sorting the left subarray
	merge_recursive(R, Rsize);  // sorting the right subarray
	merge(A, L, R, Asize, Lsize, Rsize);  // Merging L and R into A as sorted list.

}


void merge(float A[], float L[], float R[], int Asize, int Lsize, int Rsize) {
	int i,j,k;

	// i - to mark the index of left sub-array (L)
	// j - to mark the index of right sub-array (R)
	// k - to mark the index of merged sub-array (A)
	i = 0; j = 0; k =0;

	while(i < Lsize && j < Rsize) {
		if(L[i]  < R[j]) A[k++] = L[i++];
		else A[k++] = R[j++];
	}
	while(i < Lsize) A[k++] = L[i++];
	while(j < Rsize) A[k++] = R[j++];
}
