import java.security.MessageDigest;
import java.util.Arrays;
import java.util.Base64;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
public class AES {
private static SecretKeySpec secretKey;
private static void setKey(String myKey) throws Exception {
byte[] key = MessageDigest.getInstance("SHA-1").digest(myKey.getBytes("UTF-8"));
key = Arrays.copyOf(key, 16);
secretKey = new SecretKeySpec(key, "AES");
}
public static String encrypt(String data, String secret) throws Exception {
setKey(secret);
Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
cipher.init(Cipher.ENCRYPT_MODE, secretKey);
return Base64.getEncoder().encodeToString(cipher.doFinal(data.getBytes("UTF-8")));
}
public static String decrypt(String data, String secret) throws Exception {
setKey(secret);
Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
cipher.init(Cipher.DECRYPT_MODE, secretKey);
return new String(cipher.doFinal(Base64.getDecoder().decode(data)));
}
public static void main(String[] args) throws Exception {
String key = "annaUniversity";
String url = "www.annauniv.edu";
String encrypted = encrypt(url, key);
String decrypted = decrypt(encrypted, key);
System.out.println("URL Encryption Using AES Algorithm\n------------");
System.out.println("Original URL : " + url);
System.out.println("Encrypted URL : " + encrypted);
System.out.println("Decrypted URL : " + decrypted);
}
}
