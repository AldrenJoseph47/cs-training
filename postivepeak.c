#include <stdio.h>

int findpeak(int arr[], int n) 
{
    int l = 0;
    int r = n - 1;
    int mid;

    while (l <= r) 
    {
        mid = (l + r) >> 1;

        if ((mid == 0 || arr[mid - 1] <= arr[mid]) && (mid == n - 1 || arr[mid + 1] <= arr[mid])) 
        {
            break;
        }

        if (mid > 0 && arr[mid - 1] > arr[mid]) 
        {
            r = mid - 1;
        } else 
        {
            l = mid + 1;
        }
    }
    return mid;
}

int main() {
    int arr[] = {100, -3, 2, 4, 250, 0};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("index of a peak point is %d", findpeak(arr, n));
    return 0;
}