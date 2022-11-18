#!usr/bin/env vala

public static int main (string[] args) {
    stdout.printf("Array\n");

    int[] a = new int[10];
    int[] b = { 2, 4, 6, 8 };
    for (int i=0; i<a.length; i++){
        // stdout.printf(@"$a[i]\n"); // not work
        stdout.printf(a[i].to_string()); // work
        stdout.printf("\n"); // work
    }
    stdout.printf("----------\n");
    for (int i=0; i<b.length; i++){
        // stdout.printf(@"$b[i]\n"); // not work
        stdout.printf(b[i].to_string()); // work
        stdout.printf("\n"); // work
    }

    stdout.printf("----------\n");
    int[] c = b[1:3]; // => { 4, 6 }
    for (int i=0; i<c.length; i++){
        // stdout.printf(@"$c[i]\n"); // not work
        stdout.printf(c[i].to_string()); // work
        stdout.printf("\n"); // work
    }

    stdout.printf("----------\n");
    int[,] c = new int[3,4];
    int[,] d = {{2, 4, 6, 8},
                {3, 5, 7, 9},
                {1, 3, 5, 7}};
    d[2,3] = 42;

    return 0;
}