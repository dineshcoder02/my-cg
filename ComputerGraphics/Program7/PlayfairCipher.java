import java.awt.Point;
class PlayfairCipher {
static char[][] table = new char[5][5];
static Point[] pos = new Point[26];
static String clean(String s, boolean jToI) {
s = s.toUpperCase().replaceAll("[^A-Z]", "");
return jToI ? s.replace("J", "I") : s.replace("Q", "");
}
static void buildTable(String key, boolean jToI) {
String s = clean(key + "ABCDEFGHIJKLMNOPQRSTUVWXYZ", jToI);
int k = 0;
for (char c : s.toCharArray()) {
if (pos[c - 'A'] == null) {
table[k / 5][k % 5] = c;
pos[c - 'A'] = new Point(k % 5, k / 5);
k++;
}
}
}
static String process(StringBuilder text, int dir) {
for (int i = 0; i < text.length(); i += 2) {
char a = text.charAt(i), b = text.charAt(i + 1);
int r1 = pos[a - 'A'].y, c1 = pos[a - 'A'].x;
int r2 = pos[b - 'A'].y, c2 = pos[b - 'A'].x;
if (r1 == r2) {
c1 = (c1 + dir + 5) % 5;
c2 = (c2 + dir + 5) % 5;
} else if (c1 == c2) {
r1 = (r1 + dir + 5) % 5;
r2 = (r2 + dir + 5) % 5;
} else {
int t = c1; c1 = c2; c2 = t;
}
text.setCharAt(i, table[r1][c1]);
text.setCharAt(i + 1, table[r2][c2]);
}
return text.toString();
}
static String encode(String s) {
StringBuilder sb = new StringBuilder(s);
for (int i = 0; i < sb.length(); i += 2) {
if (i == sb.length() - 1) sb.append('X');
else if (sb.charAt(i) == sb.charAt(i + 1)) sb.insert(i + 1, 'X');
}
return process(sb, 1);
}
static String decode(String s) {
return process(new StringBuilder(s), -1);
}
public static void main(String[] args) {
String key = "CSE", msg = "Security Lab";
buildTable(key, true);
String enc = encode(clean(msg, true));
System.out.println("Simulating Playfair Cipher");
System.out.println("Input Message : " + msg);
System.out.println("Encrypted Message : " + enc);
System.out.println("Decrypted Message : " + decode(enc));
}
}
