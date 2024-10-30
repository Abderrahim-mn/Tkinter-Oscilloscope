Application Oscilloscope
Vue d'ensemble

Cette application est un oscilloscope graphique développé en utilisant la bibliothèque Tkinter de Python. L'oscilloscope permet aux utilisateurs de visualiser des signaux sous forme de formes d'onde en temps réel, avec une interface intuitive et personnalisable.

Le projet a été développé par MOUNOUAR, RAMI et SOTIH.
Fonctionnalités principales

    Affichage X-Y en temps réel
    L'interface principale affiche des graphiques de formes d'onde pour les axes X et Y avec une grille pour faciliter la lecture et l'analyse.

    Contrôle des harmoniques
    L'application permet de choisir d'afficher :
        Toutes les harmoniques
        Seulement les harmoniques impaires à l'aide de boutons radio « All » et « Odd ».

    Contrôle de l'amplitude
    Un curseur permet de régler l'amplitude de la forme d'onde entre 0 et 1 pour ajuster la hauteur du signal.

    Contrôle de la fréquence
    Vous pouvez modifier la fréquence du signal en choisissant parmi plusieurs valeurs prédéfinies via un curseur.

    Ajustement de la phase
    Un curseur permet de décaler la phase du signal entre -90° et 90°.

    Harmoniques ajustables
    L'utilisateur peut régler le nombre d'harmoniques à afficher, de 1 à 46, avec une échelle.

    Contrôle du nombre d'échantillons
    Un curseur permet de modifier le nombre d'échantillons affichés, de 10 à 500.

    Sélecteur de couleur
    Un outil « Color Picker » permet de personnaliser la couleur des formes d'onde pour une meilleure visualisation.

Technologies utilisées

    Python avec Tkinter pour la création de l'interface utilisateur.
    Bibliothèque de traitement de signaux pour la génération et la manipulation des formes d'onde.

Installation

    Assurez-vous que Python est installé sur votre machine.
    Installez Tkinter (si ce n'est pas déjà inclus) en exécutant la commande suivante :

    bash

sudo apt-get install python3-tk

Exécutez le script principal :

bash

    python oscilloscope.py

Utilisation

    Lancez l'application pour commencer à visualiser des signaux en temps réel.
    Ajustez l'amplitude, la fréquence, la phase et le nombre d'échantillons à l'aide des curseurs dans l'interface.
    Utilisez le sélecteur d'harmoniques pour personnaliser l'affichage des formes d'onde.
    Changez la couleur du signal à l'aide de l'outil « Color Picker » pour différencier facilement les courbes.

Développeurs

    - MOUNOUAR Abderrahim
    - RAMI Salah-eddine
    - SOTIH Mohammed Amine