import java.security.*;
import java.util.Scanner;
public class DigitalSignature {
public static void main(String[] args) throws Exception {
Scanner sc = new Scanner(System.in);
System.out.println("Enter some text");
String msg = sc.nextLine();
KeyPairGenerator keyGen = KeyPairGenerator.getInstance("DSA");
keyGen.initialize(2048);
KeyPair pair = keyGen.generateKeyPair();
Signature signer = Signature.getInstance("SHA256withDSA");
signer.initSign(pair.getPrivate());
signer.update(msg.getBytes());
byte[] signature = signer.sign();
System.out.println("Digital signature for given text: " + new String(signature, "UTF-8"));
}
}
