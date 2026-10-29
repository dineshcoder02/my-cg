class HillCipher {
static int[][] key = { {1, 2, 1}, {2, 3, 2}, {2, 2, 1} };
static int[][] invKey = { {-1, 0, 1}, {2, -1, 0}, {-2, 2, -1} };
static String process(char a, char b, char c, int[][] mat) {
int[] in = { a - 'A', b - 'A', c - 'A' };
char[] out = new char[3];
for (int col = 0; col < 3; col++) {
int sum = 0;
for (int row = 0; row < 3; row++)
sum += in[row] * mat[row][col];
out[col] = (char) ('A' + ((sum % 26) + 26) % 26);
}
return new String(out);
}
static String encode(String msg) {
String enc = "";
for (int i = 0; i < msg.length(); i += 3)
enc += process(msg.charAt(i), msg.charAt(i + 1), msg.charAt(i + 2), key);
return enc;
}
static String decode(String msg) {
String dec = "";
for (int i = 0; i < msg.length(); i += 3)
dec += process(msg.charAt(i), msg.charAt(i + 1), msg.charAt(i + 2), invKey);
return dec;
}
public static void main(String[] args) {
String msg = "SecurityLaboratory".toUpperCase();
while (msg.length() % 3 != 0) msg += "X";
String enc = encode(msg);
String dec = decode(enc);
System.out.println("Simulating Hill Cipher");
System.out.println("Padded Message : " + msg);
System.out.println("Encrypted Message : " + enc);
System.out.println("Decrypted Message : " + dec);
}
}
