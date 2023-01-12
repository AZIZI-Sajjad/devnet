

#### Comment utilsier le PlayBook:

     1- Cloner le projet

     2- Modifier le ficiher devicebackup/hosts et y ajouter les IP / FQDN et les identifiants des équipements

     3- Aller en SSH dans le dossier devicebackup

     4- Lancer la commande suivante :

     ansible-playbook -i hosts-cisco ansible-cisco.yml 

## Références:

    --> cisco.ios.ios_interfaces:
    https://docs.ansible.com/ansible/latest/collections/cisco/ios/ios_interfaces_module.html



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



--------------------------------
## *Problème de FingerPrint SSH du module *

## *ansible.netcommon.network_cli*

    TASK [ansible-cisco-playbook : Replaces device configuration of listed interfaces with provided configuration] *****************************************************************
    fatal: [sandbox-iosxe-latest-1.cisco.com]: FAILED! => {"changed": false, "msg": "paramiko: The authenticity of host 'sandbox-iosxe-latest-1.cisco.com' can't be established.\nThe ssh-rsa key fingerprint is b'c183a01b4d7fe463e003851a107895aa'."}

    PLAY RECAP *********************************************************************************************************************************************

Solution : 
Créer un fichier *ansible.cfg* à la racine où se trouve le fichier de PlayBook (dans cet exemple devicebackp/test.yml) et y ajouter : 

    [defaults]
    host_key_checking = False

--------------------------------

07/01/2023
- Création du rôle "mikrotik": OK
- Message d'erreur : 


        fatal: [192.168.4.254]: FAILED! => {"changed": false, "msg": "command timeout triggered, timeout value is 30 secs.\nSee the timeout setting options in the Network Debug and Troubleshooting Guide."}


--------------------------------

08/01/2023

- Créer un role test pour effectuer des tests 

- Test de la librérie : 

    community.routeros.routeros

    Réf: https://github.com/ansible-collections/community.routeros
    
    Réf: https://help.mikrotik.com/docs/display/ROS/Command+Line+Interface

    -> le problème de TimeOut ça ne vient pas des identifiants, car lorsque je mets des mouvais identifiants j'ai le message:

        fatal: [192.168.4.254]: FAILED! => {"changed": false, "msg": "Failed to authenticate: Authentication failed."}
    


##     Solution du message Time Out:  =>

        fatal: [192.168.4.254]: FAILED! => {"changed": false, "msg": "command timeout triggered, timeout value is 30 secs.\nSee the timeout setting options in the Network Debug and Troubleshooting Guide."}


    -> Activer le mode BUMB sur le rtouteur OS Mikrotik: 
       En se connectant en SSH à CLI du routeur : 

       Réf: https://docs.ansible.com/ansible/latest/network/user_guide/platform_routeros.html

       Réf: https://help.mikrotik.com/docs/display/ROS/Command+Line+Interface

       Réf: https://wiki.mikrotik.com/wiki/Manual:Console_login_process#Console_login_options

       Réf:  https://jcutrer.com/howto/networking/mikrotik/mikrotik-backup-and-restore


- ## -> *PlayBook MikroTik est opérationnel*

--------------------------------

# 09/01/2023

### Faits: 
-   Activer gather_facts: Afin de récupérer l'heure du serveur Ansible pour pouvoir l'ajouter à la fin du nom des fichiers de backup

        Réf: https://www.unixarena.com/2019/05/using-date-and-timestamp-variable-in-ansible-playbook.html/

        gather_facts: yes
        dest: ./roles/mikrotik/backups/config.{{ ansible_date_time.iso8601 }}.txt

        Exemple:
        "iso8601": "2019-03-11T09:19:33Z",

-   Ajouter l'heure à la fin des fichiers de sauvegardes de CISCO & Mikrotik  .{{ ansible_date_time.iso8601 }}


- Récupérer l'IP de l'équipement à l'aide de gather_facts et sa variable {{ inventory_hostname }}

        Pour les équipements CISCO la librérie "backup" du module "cisco.ios.ios" récupère running-config et le sauvegarde avec IP_TimeStemp dans le dossier "backup"

- Récupérer le chemin du Playbook afin d'écourter le chemin absolut : 
    
        Nom de la varibale système du réperoire du PlayBook: 
        
        {{ playbook_dir }}
        
        
        Par exemple dans le PlayBook "ansible-playbook.yml" dans le fichier mail.yml du role MikroTik, le chemin du fichier de sauvegarde est déifini de cette manière: 

        Chemin : 

        "{{ playbook_dir }}/roles/mikrotik/backups/{{ inventory_hostname }}_config.{{ ansible_date_time.date }}@{{ ansible_date_time.time }}.txt"

        Au lieu de  : /var/git/github/devnet/devicebackup/roles/mikrotik/backups/192.168.4.254_config.2023-01-10@00:12:44.txt


--------------------------------

# 10/01/2023 À Faire: 

PlayBook MikroTik: 
    
### 1- Lorsqu'on envoie la commande "/ip" address print"
    il y a le messaeg d'erreur : 


    fatal: [192.168.4.254]: FAILED! => {"changed": false, "msg": "command timeout triggered, timeout value is 30 secs.\nSee the timeout setting options in the Network Debug and Troubleshooting Guide."}

### 2- Lorsqu'on sauvegarde MikroTik le résltat est en format brut, c'est à dire sans ENTREE avec des "\\n"  
        Réf: https://www.cloudbees.com/blog/ansible-lineinfile-9-ways-to-use-it-to-improve-your-playbooks

### 3- Cacher les identifiants de MikroTik 

### 4- Etant donné que le fichier de sauvegarde de MikroTik contient des MOT DE PASSE 
        À voir quelle solution est faisable et plus sécurisé 

        1- Il va falloir chiffrer le fichier avec un MDP 

        2- Utiliser d'autres commandes ou moyen pour sauvegarder MikroTik, un moyen de ne pas stocker les MDP dans le fichier de config

### 5-  Comment restaurer la config sur MikroTik 

### 6-  Comment restaurer la config sur CISCO 

### 7- Faire une tâche planifier lancer la sauvegarde autoatiquement

### 8- Comment envoyer les sauvegardes vers un FTP et Lire les sauvegardes en cas de Besoin 


### 9- Comment versionner les sauvegardes 

### 10- Comparer la config actulle '{Dernière sauvegarde}' avec les anciennes


--------------------------



# 12/01/2023 

## Trouver un repository pfsense sur Github

        Réf: https://github.com/5h0ckw4v3/pfSense_Playbook.git


