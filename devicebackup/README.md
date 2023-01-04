# Objectif: 

1- Automatiser la sauvegarde des routeurs et des switchs du DC

2- Récupérer leurs configuration au format txt et les enregistrer sur git

3- Versionner les fichiers 

4- Faire des cron  


# 1- Dans un premier temps:

- Tester une connection ssh sur un switch du DC et tenter d'enregistrer la configuration en enable et avec les commandes cisco.

- Ensuite importer le fichier sur Dev3/GitLab.

- Peut être automatiser l'envoi d'un mail qui informe de cet import ?

- Dupliquer le code qui fonctionne à d'autres équipements.

- Réaliser un copy RS (en enable) tout les jours et à une heure bien précise => ne pas perdre la configuration actuelle en cas de problème.



### Création du playbook:

    ansible-playbook init devicebackup
 
Ajout de dossiers routeurs et switchs afin de pouvoir stocker les scripts et les fichiers concernant les équipements.

Le premier script tente la connexion ssh à un routeur de prêt de cisco: sandbox-iosxe-latest-1.cisco.com 

avec les identifiants: developer/C1sco12345.

La connexion ne fonctionnait pas et le message d'erreur affichait: skipping: no hosts matched.


### test-ssh.yml:

    ---
    hosts: sandbox
        connection: local
        gather_facts: no

    vars:
        default_ssh_user: developer
        default_ssh_pass: C1sco12345
  
    tasks: 
        - name: passer en mode enable à la connection ssh
            ansible.netcommon.cli_command:
            network_os: ansible_network_os
            become_method: sudo
            command: show run


### hosts:

    [sandbox]
    sandbox-iosxe-latest-1.cisco.com

    [sandbox:vars] 
    ansible_connection=ssh
    #ansible_ssh_extra_args='-o PreferredAuthentications=password -o PasswordAuthentication=yes -o "StrictHostKeyChecking no" -o IdentitiesOnly=yes' 
    ansible_port=22


## Création d'un autre dossier pour faire des tests

source: https://github.com/brona/ansible-cisco-ios-example

On a cloné les modules de la source ci-dessus et retravaillé les scripts pour tester la connexion ssh qui ne fonctionnais pas avec le test-ssh.yml.

Le message d'erreur:

    sandbox-iosxe-latest-1.cisco.com : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0 

    "msg": "Unsupported parameters for (cisco.ios.ios_command) module: provider.ansible_password, provider.ansible_user. Supported parameters include: commands, retries, wait_for (waitfor), match, interval, provider."

La connection se fait mais l'authentification ne s'éffectue pas correctement et vu que le dépôt github date de 2016 il est possible que le code ansible ne soit pas bon.

## Création du projet dans GitLab:

source de l'image: https://hub.docker.com/_/debian/tags?page=1&name=bull

Pour palier aux problèmes de connections ssh on utilise le pipeline editor de GitLab afin de se connecter en passant par un container.

Le script est en bash et réalise des commandes.

J'usqu'à présent on rencontre un problème de connection dû au fait que le réseau d'agoravita n'est pas autorisé à se connecter au réseau des équipements du DC.                                 

Création d'une image docker basée sur debian 11 avec tout ce que l'on a à téklécharger dans le conteneur afin d'aller plus vite dans les tests.

Travail sur le test.yml avec le role test.




