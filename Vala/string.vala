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

        //  string greeting = "Привет, мир!"; // rus lang BAD (21 bytes)
        //  string greeting = "Привет, мир!".to_string(); // rus lang BAD (21 bytes)
        //  string greeting = """Привет, мир!"""; // rus lang BAD (21 bytes)
        string greeting = "Privet, mir!"; // eng lang OK (12 bytes)
        stdout.printf(greeting); // utf-8
        print("\n"); // not utf-8
        string s1 = greeting[8:12]; // => "мир!"
        string s2 = greeting[-12:-6]; // => "Привет"
        stdout.printf(s1); // utf-8
        print("\n"); // not utf-8
        stdout.printf(s2); // utf-8
        print("\n"); // not utf-8

        string str = "Привет, мир!";
        stdout.printf(str + "\n");
        int letters = str.char_count();
        int bytes = str.length;
        print ("letters: %d, bytes: %d\n", letters, bytes);
        unichar c;
        for (int i = 0; str.get_next_char(ref i, out c);) {
            stdout.printf ("%s size %d\n", c.to_string(), c.to_string().length);
        }

        str = "Privet, mir!";
        stdout.printf(str + "\n");
        letters = str.char_count();
        bytes = str.length;
        print ("letters: %d, bytes: %d\n", letters, bytes);
        for (int i = 0; str.get_next_char(ref i, out c);) {
            stdout.printf ("%s size %d\n", c.to_string(), c.to_string().length);
        }

        return 0;
    }
}