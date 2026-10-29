class RailFenceCipher {
static String encode(String msg, int depth) {
int rows = depth, cols = msg.length() / depth;
char[][] mat = new char[rows][cols];
int k = 0;
for (int c = 0; c < cols; c++)
for (int r = 0; r < rows; r++)
mat[r][c] = (k < msg.length()) ? msg.charAt(k++) : 'X';
StringBuilder enc = new StringBuilder();
for (int r = 0; r < rows; r++)
for (int c = 0; c < cols; c++)
enc.append(mat[r][c]);
return enc.toString();
}
static String decode(String enc, int depth) {
int rows = depth, cols = enc.length() / depth;
char[][] mat = new char[rows][cols];
int k = 0;
for (int r = 0; r < rows; r++)
for (int c = 0; c < cols; c++)
mat[r][c] = enc.charAt(k++);
StringBuilder dec = new StringBuilder();
for (int c = 0; c < cols; c++)
for (int r = 0; r < rows; r++)
dec.append(mat[r][c]);
return dec.toString();
}
public static void main(String[] args) {
String msg = "Anna University, Chennai";
int depth = 2;
String enc = encode(msg, depth);
String dec = decode(enc, depth);
System.out.println("Simulating Rail Fence Cipher");
System.out.println("Input Message : " + msg);
System.out.println("Encrypted Message : " + enc);
System.out.println("Decrypted Message : " + dec);
}
}
