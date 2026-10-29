public class DiffieHellman {
public static void main(String[] args) {
int p = 23; // publicly known prime
int g = 5; // publicly known primitive root
int x = 4; // Alice's private secret
int y = 3; // Bob's private secret
double aliceSends = Math.pow(g, x) % p;
double bobSends = Math.pow(g, y) % p;
double bobComputes = Math.pow(aliceSends, y) % p;
double aliceComputes = Math.pow(bobSends, x) % p;
double sharedSecret = Math.pow(g, x * y) % p;
System.out.println("Diffie-Hellman Key Exchange\n---------------------------");
System.out.println("Alice Sends : " + aliceSends);
System.out.println("Bob Sends : " + bobSends);
System.out.println("Bob Computes : " + bobComputes);
System.out.println("Alice Computes : " + aliceComputes);
System.out.println("Shared Secret : " + sharedSecret);
if (aliceComputes == sharedSecret && bobComputes == sharedSecret)
System.out.println("Success: Shared Secrets Match! " + sharedSecret);
else
System.out.println("Error: Shared Secrets do not Match");
}
}
