#!usr/bin/env vala

public static int main (string[] args) {
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
    string greeting = "Privet, Mir!"; // eng lang OK (12 bytes)
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
    stdout.printf(@"$str\n", str);
    stdout.printf("%p\n", str);
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

    unichar c2 = greeting[8]; // => 'M'
    stdout.printf(c2.to_string() + "\n");

    bool b2 = bool.parse("false"); // => false
    //  bool b2 = false; // => false
    stdout.printf(@"$b2\n");
    stdout.printf("%b\n", b2);
    //  print("\n");
    int i = int.parse("-52"); // => -52
    stdout.printf(@"$i\n");
    stdout.printf("%d\n", i);
    double d = double.parse("6.67428E-11"); // => 6.67428E-11
    stdout.printf(@"$d\n");
    stdout.printf("%g\n", d);
    //  string s1 = true.to_string(); // => "true"
    //  stdout.printf(s1 + "\n");
    //  string s2 = 21.to_string(); // => "21"
    //  stdout.printf(s2 + "\n");

    bool t1 = true;
	bool t2 = false;
	bool t3 = (10 > 100 || 100 < 10);
	// Output: ``true, false, false``
	print (@"$t1, $t2, $t3\n");

    return 0;
}