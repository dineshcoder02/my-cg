class VigenereCipher {
static String encode(String text, String key) {
StringBuilder res = new StringBuilder();
text = text.toUpperCase();
for (int i = 0, j = 0; i < text.length(); i++) {
char c = text.charAt(i);
if (c < 'A' || c > 'Z') continue;
res.append((char) ((c + key.charAt(j) - 2 * 'A') % 26 + 'A'));
j = (j + 1) % key.length();
}
return res.toString();
}
static String decode(String text, String key) {
StringBuilder res = new StringBuilder();
for (int i = 0, j = 0; i < text.length(); i++) {
char c = text.charAt(i);
res.append((char) ((c - key.charAt(j) + 26) % 26 + 'A'));
j = (j + 1) % key.length();
}
return res.toString();
}
public static void main(String[] args) {
String key = "VIGENERECIPHER";
String msg = "SecurityLaboratory";
String enc = encode(msg, key);
String dec = decode(enc, key);
System.out.println("Simulating Vigenere Cipher");
System.out.println("Input Message : " + msg);
System.out.println("Encrypted Message : " + enc);
System.out.println("Decrypted Message : " + dec);
}
}
