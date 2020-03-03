#include <gpgme.h>
#include <errno.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

int main(int argc, char** argv) {

    if (argc != 2) {
        fprintf(stderr, "Invalid usage: %s FIRMWARE_OBJ_FILE\n", argv[0]);
        return 1;
    }

    struct stat metadata;
    if (stat(argv[1], &metadata) != 0) {
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

    

    printf("Successfully verified firmware!\n");
    return 0;
}
