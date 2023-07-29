#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int validate(const char* public_key, const char* r, const char* sigma, const char* message, const char* generator, const char* prime) {
    mpz_t g, p, R, publicKey, h, h_inverse, lhs, rhs;

    mpz_init_set_str(g, generator, 16);
    mpz_init_set_str(p, prime, 16);
    mpz_init_set_str(R, r, 16);
    mpz_init_set_str(publicKey, public_key, 16);

    char message_hash[16 * 2 + 1];
    // SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, message, strlen(message));
    SHA256_Final(message_hash, &sha256);

    mpz_init_set_str(h, message_hash, 16);
    mpz_invert(h_inverse, h, p);

    mpz_init(lhs);
    mpz_init(rhs);

    mpz_powm(lhs, g, mpz_get_ui(sigma), p);
    mpz_powm(rhs, publicKey, h_inverse, p);
    mpz_mul(lhs, lhs, rhs);
    mpz_mod(lhs, lhs, p);

    int result = mpz_cmp(lhs, R) == 0;

    mpz_clear(g);
    mpz_clear(p);
    mpz_clear(R);
    mpz_clear(publicKey);
    mpz_clear(h);
    mpz_clear(h_inverse);
    mpz_clear(lhs);
    mpz_clear(rhs);

    return result;
}

int main() {
    const char* public_key = "95073b6e87714370";
    const char* r = "4cc830ddaf370137";
    const char* sigma = "26ca77a6cdf821d5";
    const char* message = "Hash Effect!!!";
    const char* prime = "7c0ed2cd513e0bcf";
    const char* generator = "2";

    if (validate(public_key, r, sigma, message, generator, prime)) {
        printf("Signature is valid.\n");
    }
    else {
        printf("Signature is invalid.\n");
    }

    return 0;
}
