import java.security.MessageDigest;
public class SHA1 {
public static void main(String[] args) throws Exception {
MessageDigest md = MessageDigest.getInstance("SHA-1");
System.out.println("Algorithm : " + md.getAlgorithm());
System.out.println("Provider : " + md.getProvider());
String[] inputs = { "", "abc", "abcdefghijklmnopqrstuvwxyz" };
for (String input : inputs) {
byte[] digest = md.digest(input.getBytes());
System.out.println("SHA1(\"" + input + "\") = " + bytesToHex(digest));
}
}
private static String bytesToHex(byte[] bytes) {
StringBuilder sb = new StringBuilder();
for (byte b : bytes) sb.append(String.format("%02X", b));
return sb.toString();
}
}
