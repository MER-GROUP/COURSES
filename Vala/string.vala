#!usr/bin/env vala

class Demo.String: GLib.Object {
    public static int main(string[] args) {
        stdout.printf("Не изменяемая строка 1\n"); // utf-8

        string text = "Не изменяемая строка 2\n";
        print(text); // not utf-8
        stdout.printf(text); // utf-8

        string verbatim = """Это так называемая дословная строка "verbatim string".
Такие строки не распознают управляющие последовательности, такие как \n, \t, \\, и другие.
Они могут содержать кавычки и состоять из нескольких строк.""";
        stdout.printf(verbatim); // utf-8
        print("\n"); // not utf-8

        int a = 6, b = 7;
        string s = @"$a * $b = $(a * b)"; // => "6 * 7 = 42"
        stdout.printf(s); // utf-8
        print("\n"); // not utf-8

        string greeting = "Привет, мир!";
        string s1 = greeting[8:12]; // => "мир!"
        string s2 = greeting[-12:-6]; // => "Привет"
        stdout.printf(s1); // utf-8
        print("\n"); // not utf-8
        stdout.printf(s2); // utf-8
        print("\n"); // not utf-8

        return 0;
    }
}