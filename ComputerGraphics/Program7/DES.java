import java.security.*;
import javax.crypto.*;
public class DES {
public static void main(String[] args) throws Exception {
System.out.println("Message Encryption Using DES Algorithm\n-------");
KeyGenerator keyGen = KeyGenerator.getInstance("DES");
SecretKey myDesKey = keyGen.generateKey();
Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
byte[] text = "Secret Information".getBytes();
System.out.println("Message : " + new String(text));
cipher.init(Cipher.ENCRYPT_MODE, myDesKey);
byte[] encrypted = cipher.doFinal(text);
System.out.println("Encrypted Message: " + encrypted);
cipher.init(Cipher.DECRYPT_MODE, myDesKey);
byte[] decrypted = cipher.doFinal(encrypted);
System.out.println("Decrypted Message: " + new String(decrypted));
}
}
