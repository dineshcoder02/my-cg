class RowColumnCipher {
static int col = 4;
static String encode(String msg) {
msg = msg.replaceAll("\\s", "");
int row = (int) Math.ceil((double) msg.length() / col);
char[][] mat = new char[row][col];
int k = 0;
for (int r = 0; r < row; r++)
for (int c = 0; c < col; c++)
mat[r][c] = (k < msg.length()) ? msg.charAt(k++) : '#';
StringBuilder enc = new StringBuilder();
for (int c = 0; c < col; c++)
for (int r = 0; r < row; r++)
enc.append(mat[r][c]);
return enc.toString();
}
public static void main(String[] args) {
String msg = "Security Lab";
String enc = encode(msg);
System.out.println("Simulating Row & Column Transposition Cipher");
System.out.println("Input Message : " + msg);
System.out.println("Encrypted Message : " + enc);
}
}
