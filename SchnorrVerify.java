import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class SchnorrVerify {

    public static void main(String[] args) {
        BigInteger generator = new BigInteger("2", 16);
        BigInteger primeP = new BigInteger("7c0ed2cd513e0bcf", 16);
        BigInteger hash = new BigInteger("600763bca5936e86", 16);
        BigInteger publicKey = new BigInteger("95073b6e87714370", 16);
        BigInteger r = new BigInteger("4cc830ddaf370137", 16);
        BigInteger sigma = new BigInteger("26ca77a6cdf821d5", 16);
        BigInteger message = new BigInteger("Hash Effect!!!".getBytes());

        if (schnorrVerify(generator, primeP, publicKey, r, sigma, hash)) {
            System.out.println("Signature is valid.");
        } else {
            System.out.println("Signature is invalid.");
        }
    }

    public static boolean schnorrVerify(BigInteger generator, BigInteger primeP, BigInteger publicKey,
                                        BigInteger r, BigInteger sigma, BigInteger hash) {
        try {
            BigInteger hInverse = hash.modInverse(primeP);
            BigInteger leftSide = generator.modPow(sigma, new BigInteger("1")).multiply(publicKey.modPow(hInverse, new BigInteger("1"))).mod(new BigInteger("1"));
            // BigInteger leftSide = generator.pow(sigma.intValue()).multiply(publicKey.pow(hInverse.intValue()));

            BigInteger rightSide = r.mod(new BigInteger("1"));

            // System.out.println(leftSide + " " + rightSide);
            return leftSide.equals(rightSide);
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    public static BigInteger sha256Hash(String message) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] digest = md.digest(message.getBytes());

        return new BigInteger(1, digest);
    }
}
