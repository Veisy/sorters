#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
 
 
//Function declarations. Functions are defined below the main function.
float *insertion_sort (float A[], int Asize);
float *merge_insertion_sort(float A[], int Asize);
float *merge_sort(float A[], int Asize);
float *quick_sort(float A[], int Asize) ;
float *heap_sort(float A[], int n);

void merge_recursive(float A[], int Asize, bool is_insertion_based);
void merge(float A[], float L[], float R[], int Asize, int Lsize, int Rsize);
void quick_recursive(float A[], int low, int high);
void swap(float *a, float *b);
float partition(float A[], int low, int high);
void heapify(float A[], int n, int i);


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
  	return A;
}


// Insertion Sort based, hybrid algorithm.
float *merge_insertion_sort(float A[], int Asize) {
    merge_recursive(A, Asize, true);
    return A;
}


float *merge_sort(float A[], int Asize) {
    merge_recursive(A, Asize, false);
    return A;
}


// Recursive function to sort an array of integers. 
void merge_recursive(float A[], int Asize, bool is_insertion_based) {
	int mid,i;
	if(Asize < 2) return; // base condition. If the array has less than two element, do nothing. 

	mid = Asize/2;  // find the mid index.
	int Lsize = mid;
	int Rsize = (Asize - mid);
    
    float L[Lsize];
    float R[Rsize];

	for(i = 0; i < mid; i++) L[i] = A[i]; // creating left subarray
	for(i = mid; i < Asize; i++) R[i-mid] = A[i]; // creating right subarray

    if (is_insertion_based) {
        insertion_sort(L, Lsize);  // sorting the left subarray
	    insertion_sort(R, Rsize);  // sorting the right subarray
    } else {
	    merge_recursive(L, Lsize, is_insertion_based);  // sorting the left subarray
	    merge_recursive(R, Rsize, is_insertion_based);  // sorting the right subarray
    }

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

// Function to swap the the position of two elements
void swap(float *a, float *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

float *quick_sort(float A[], int Asize) {
    quick_recursive(A, 0, Asize - 1);
    return A;
}

void quick_recursive(float A[], int low, int high) {
  if (low < high) {

    // find the pivot element such that
    // elements smaller than pivot are on left of pivot
    // elements greater than pivot are on right of pivot
    int pi = partition(A, low, high);

    // recursive call on the left of pivot
    quick_recursive(A, low, pi - 1);

    // recursive call on the right of pivot
    quick_recursive(A, pi + 1, high);
  }
}

// function to find the partition position
float partition(float A[], int low, int high) {

  // select the rightmost element as pivot
  float pivot = A[high];

  // pointer for greater element
  int i = (low - 1);

  // traverse each element of the array
  // compare them with the pivot
  for (int j = low; j < high; j++) {
    if (A[j] <= pivot) {

      // if element smaller than pivot is found
      // swap it with the greater element pointed by i
      i++;

      // swap element at i with element at j
      swap(&A[i], &A[j]);
    }
  }

  // swap the pivot element with the greater element at i
  swap(&A[i + 1], &A[high]);

  // return the partition point
  return (i + 1);
}

// Main function to do heap sort
float *heap_sort(float A[], int n) {
    // Build max heap
    for (int i = n / 2 - 1; i >= 0; i--)
      heapify(A, n, i);

    // Heap sort
    for (int i = n - 1; i >= 0; i--) {
      swap(&A[0], &A[i]);

      // Heapify root element to get highest element at root again
      heapify(A, i, 0);
    }

    return A;
}

void heapify(float A[], int n, int i) {
    // Find largest among root, left child and right child
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && A[left] > A[largest])
      largest = left;

    if (right < n && A[right] > A[largest])
      largest = right;

    // Swap and continue heapifying if root is not largest
    if (largest != i) {
      swap(&A[i], &A[largest]);
      heapify(A, n, largest);
    }
}



