import pygame
import random

pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)

# Définition de la taille de l'écran
largeur_ecran = 800
hauteur_ecran = 600
taille_case = 20

# Création de la fenêtre de jeu
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Snake")

# Fonction principale pour exécuter le jeu
def jeu_snake():
    # Position initiale du serpent
    serpent = [[largeur_ecran // 2, hauteur_ecran // 2]]
    direction = 'gauche'

    # Position initiale de la pomme
    pomme = [random.randrange(1, largeur_ecran // taille_case) * taille_case,
             random.randrange(1, hauteur_ecran // taille_case) * taille_case]

    # Variable pour indiquer si le jeu est en cours ou terminé
    jeu_en_cours = True

    # Boucle principale du jeu
    while jeu_en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu_en_cours = False

            # Détection des touches de direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'droite':
                    direction = 'gauche'
                elif event.key == pygame.K_RIGHT and direction != 'gauche':
                    direction = 'droite'
                elif event.key == pygame.K_UP and direction != 'bas':
                    direction = 'haut'
                elif event.key == pygame.K_DOWN and direction != 'haut':
                    direction = 'bas'

        # Création d'une nouvelle tête pour le serpent
        nouvelle_tete = serpent[0].copy()
        if direction == 'gauche':
            nouvelle_tete[0] -= taille_case
        elif direction == 'droite':
            nouvelle_tete[0] += taille_case
        elif direction == 'haut':
            nouvelle_tete[1] -= taille_case
        elif direction == 'bas':
            nouvelle_tete[1] += taille_case

        # Vérification si le serpent est sorti de la zone de jeu ou s'il a collisionné avec lui-même
        if (nouvelle_tete[0] < 0 or nouvelle_tete[0] >= largeur_ecran or
                nouvelle_tete[1] < 0 or nouvelle_tete[1] >= hauteur_ecran or
                nouvelle_tete in serpent[1:]):
            # Si le serpent est sorti ou a collisionné, on met fin au jeu
            jeu_en_cours = False

        # Ajout de la nouvelle tête au serpent
        serpent.insert(0, nouvelle_tete)

        # Vérification des collisions avec la pomme
        if serpent[0] == pomme:
            # Génération d'une nouvelle position pour la pomme
            pomme = [random.randrange(1, largeur_ecran // taille_case) * taille_case,
                     random.randrange(1, hauteur_ecran // taille_case) * taille_case]
        else:
            # Si le serpent n'a pas mangé de pomme, on supprime la dernière partie du corps
            serpent.pop()

        # Effacement de l'écran
        ecran.fill(NOIR)

        # Dessin du serpent
        for partie in serpent:
            pygame.draw.rect(ecran, VERT, [partie[0], partie[1], taille_case, taille_case])

        # Dessin de la pomme
        pygame.draw.rect(ecran, ROUGE, [pomme[0], pomme[1], taille_case, taille_case])

        # Mise à jour de l'écran
        pygame.display.update()

        # Vitesse du jeu
        pygame.time.Clock().tick(10)

    # Affichage du message de fin
    ecran.fill(NOIR)
    message_fin = pygame.font.Font(None, 36).render("Game Over - Vous êtes éliminé !", True, BLANC)
    ecran.blit(message_fin, (largeur_ecran // 2 - 200, hauteur_ecran // 2))
    pygame.display.update()
    pygame.time.wait(2000)  # Pause de 2 secondes avant de quitter le jeu

    pygame.quit()

jeu_snake()
