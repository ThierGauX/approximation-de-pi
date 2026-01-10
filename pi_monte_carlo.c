#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <assert.h>

int main() {
    // En C, M_PI est défini dans math.h sur la plupart des systèmes
    double pi_reel = 3.14159265358979323846;
    printf("Pour rappel, Pi = %.15f\n", pi_reel);

    int k = 11;
    // On utilise long long car 10^9 dépasse la capacité d'un simple 'int' (max 2*10^9)
    long long N = pow(10, k);
    long long interieur = 0;
    long long exterieur = 0;

    // Initialisation du générateur de nombres aléatoires
    srand(time(NULL));

    for (long long j = 1; j <= N; j++) {
        // random.uniform(0, 1) en C :
        double x = (double)rand() / RAND_MAX;
        double y = (double)rand() / RAND_MAX;

        // On évite sqrt pour gagner en performance (x^2 + y^2 <= 1^2)
        if (x*x + y*y <= 1.0) {
            interieur++;
        } else {
            exterieur++;
        }

        // Vérification (équivalent du assert)
        assert(interieur + exterieur == j);

        // Affichage tous les 10^7 tirages
        if (j % 10000000 == 0) {
            double approx_Pi = (double)interieur / j * 4.0;
            double delta = fabs(approx_Pi - pi_reel);
            printf("nombre de tirages: %lld; delta= %.10f; Approx de pi = %.10f\n", j, delta, approx_Pi);
        }
    }

   return 0;
}