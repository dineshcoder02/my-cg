class CaesarCipher {
static String encode(String text, int shift) {
shift = ((shift % 26) + 26) % 26;
StringBuilder result = new StringBuilder();
for (char ch : text.toCharArray()) {
if (Character.isUpperCase(ch))
result.append((char) ('A' + (ch - 'A' + shift) % 26));
else if (Character.isLowerCase(ch))
result.append((char) ('a' + (ch - 'a' + shift) % 26));
else
result.append(ch);
}
return result.toString();
}
static String decode(String text, int shift) {
return encode(text, 26 - shift);
}
public static void main(String[] args) {
String msg = "Anna University";
String enc = encode(msg, 3);
String dec = decode(enc, 3);
System.out.println("Simulating Caesar Cipher");
System.out.println("Input Message : " + msg);
System.out.println("Encrypted Message : " + enc);
System.out.println("Decrypted Message : " + dec);
}
}
