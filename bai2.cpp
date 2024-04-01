#include <stdio.h>
#include <math.h>

int isPerfectSquare(int n) {
    int sqrt_n = sqrt(n);
    return sqrt_n * sqrt_n == n;
}
void demSoChinhPhuong(int n) {
    int count = 0;
    for (int i = 1; i < n; i++) {
        if (isPerfectSquare(i)) {
            count++;
        }
    }
   printf("Có %d số chính phương nhỏ hơn %d",count,n);
}

// Function to count and print perfect squares less than n
void inSoChinhPhuong(int n) {
    printf("\nCac so chinh phuong nho hon %d:\n", n);
    for (int i = 1; i < n; i++) {
        if (isPerfectSquare(i)) {
            printf("%d ", i);
        }
    }
}

int main() {
    int n;
    printf("Nhap vao mot so nguyen duong: ");
    scanf("%d", &n);
    demSoChinhPhuong(n);
    inSoChinhPhuong(n);
    return 0; // Return 0 to indicate successful completion
}
