#include <gpgme.h>
#include <errno.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

#define RED    "\033[1;31m"
#define GREEN  "\033[1;32m"
#define NORMAL "\033[0m"

int main(int argc, char** argv) {

    if (argc != 3) {
        fprintf(stderr, "Invalid usage: %s GPG_SIGNATURE FIRMWARE_OBJ_FILE\n", argv[0]);
        return 1;
    }

    struct stat metadata1, metadata2;
    if (stat(argv[1], &metadata1) || stat(argv[2], &metadata2)) {
        perror("File check");
        return 1;
    }

    // Verify GPG lib (ideally should specify version here but for portability purposes any version is fine)
    gpgme_check_version(NULL);    

    // Create GPG context
    gpgme_ctx_t ctx;
    if (gpgme_new(&ctx) != GPG_ERR_NO_ERROR) {
        fprintf(stderr, "Failed to create GPG Context\n");
        return 1;
    }

    // Read the GPG key and add it to ring (this part can be imported from a trusted host)
    gpgme_data_t keydata;
    if (gpgme_data_new_from_file(&keydata, "public.gpg", 1) != GPG_ERR_NO_ERROR) {
        fprintf(stderr, "Failed to read GPG key from public.gpg\n");
        return 1;
    }

    // Add the key to the context's keyring
    if (gpgme_op_import(ctx, keydata) != GPG_ERR_NO_ERROR) {
        fprintf(stderr, "Failed to import GPG key\n");
        return 1;
    }

    // Read the signature of the firmware 
    gpgme_data_t firmware_keydata;
    if (gpgme_data_new_from_file(&firmware_keydata, argv[1], 1) != GPG_ERR_NO_ERROR) {
        fprintf(stderr, "Failed to read firmware signature\n");
        return 1;
    }

    // Get the signed text
    gpgme_data_t firmware;
    if (gpgme_data_new_from_file(&firmware, argv[2], 1) != GPG_ERR_NO_ERROR) {
        fprintf(stderr, "Failed to read firmware\n");
        return 1;
    }

    if (gpgme_op_verify(ctx, firmware_keydata, firmware, NULL) != GPG_ERR_NO_ERROR) {
        printf(RED "ERROR" NORMAL ": Invalid firmware update...\n");
        return 1;
    }

    printf(GREEN "SUCCESS" NORMAL ": Passed!\n");
    return 0;

}
